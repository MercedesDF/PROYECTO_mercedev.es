#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
merci-linkcheck.py — Rastreador dinámico de enlaces rotos.

Recorre el proyecto de forma local (vía HTTP) para asegurar que ninguna 
ruta devuelve error 404, validando la integración real de Nginx y WordPress.
"""

import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed


class LinkParser(HTMLParser):
    links: list[str]
    a_tags: list[tuple[str, str]]
    in_a_tag: bool
    current_href: str
    current_aria_label: str
    current_text: list[str]

    def __init__(self) -> None:
        """
        QUÉ HACE: Inicializa el parser de enlaces con listas vacías y banderas de estado.
        POR QUÉ: Prepara la acumulación de rutas y textos descriptivos durante el procesamiento HTML.
        """
        super().__init__()
        self.links = []
        self.a_tags = []
        self.in_a_tag = False
        self.current_href = ""
        self.current_aria_label = ""
        self.current_text = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """
        QUÉ HACE: Intercepta las etiquetas HTML a, link e img para capturar sus respectivos atributos href o src.
        POR QUÉ: Permite extraer de forma sistemática todas las dependencias y enlaces internos/externos de la página.
        """
        attrs_dict = dict(attrs)
        # Extraer URLs de anclas, estilos e imágenes
        if tag == "a":
            self.in_a_tag = True
            self.current_href = attrs_dict.get("href", "") or ""
            self.current_aria_label = attrs_dict.get("aria-label", "") or ""
            self.current_text = []
            if self.current_href:
                self.links.append(self.current_href)
        elif tag == "link":
            href = attrs_dict.get("href")
            if href:
                self.links.append(href)
        elif tag == "img":
            src = attrs_dict.get("src")
            if src:
                self.links.append(src)
            
    def handle_data(self, data: str) -> None:
        """
        QUÉ HACE: Acumula el texto visible que está dentro del enlace.
        POR QUÉ: Ayuda a calcular el nombre accesible del enlace para cumplir con el estándar WCAG.
        """
        if self.in_a_tag:
            self.current_text.append(data)
            
    def handle_endtag(self, tag: str) -> None:
        """
        QUÉ HACE: Al cerrar la etiqueta de ancla, calcula el Nombre Accesible del enlace y lo añade a la lista.
        POR QUÉ: Simula el comportamiento de lectores de pantalla (WAI-ARIA). Si no hay un aria-label explícito, se utiliza el texto visible.
        """
        if tag == "a" and self.in_a_tag:
            self.in_a_tag = False
            # Calcula el "Nombre Accesible" real del enlace.
            # Simula el comportamiento de un lector de pantalla (WAI-ARIA). 
            # Si no hay un aria-label explícito, se utiliza el texto visible.
            accessible_name = self.current_aria_label.strip() or "".join(self.current_text).strip()
            
            if accessible_name and self.current_href:
                self.a_tags.append((accessible_name, self.current_href))


def fetch_and_parse(url_info: tuple[str, str], base_url: str):
    clean_url, source_url = url_info
    new_urls = []
    wcag_errors = []
    broken_link = None
    
    try:
        req = urllib.request.Request(clean_url, headers={'User-Agent': 'Merci-Bot/1.0'})
        with urllib.request.urlopen(req) as response:
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                html = response.read().decode('utf-8', errors='ignore')
                parser = LinkParser()
                parser.feed(html)
                
                name_to_hrefs = {}
                for name, href in parser.a_tags:
                    if not name:
                        continue
                    full_href = urljoin(clean_url, href)
                    if name not in name_to_hrefs:
                        name_to_hrefs[name] = set()
                    name_to_hrefs[name].add(full_href)
                    
                for name, hrefs in name_to_hrefs.items():
                    if len(hrefs) > 1:
                        wcag_errors.append((clean_url, name, hrefs))
                        
                for link in parser.links:
                    full_url = urljoin(clean_url, link)
                    parsed_full = urlparse(full_url)
                    parsed_base = urlparse(base_url)
                    
                    if parsed_full.netloc == parsed_base.netloc:
                        new_clean = parsed_full._replace(fragment="").geturl()
                        new_urls.append((new_clean, clean_url))
                        
    except urllib.error.HTTPError as e:
        broken_link = (clean_url, source_url, str(e.code))
    except urllib.error.URLError as e:
        broken_link = (clean_url, source_url, str(e.reason))
    except Exception as e:
        broken_link = (clean_url, source_url, str(e))
        
    return clean_url, new_urls, wcag_errors, broken_link


def main() -> None:
    """
    QUÉ HACE: Escanea de forma recursiva (vía HTTP) todas las páginas internas a partir del localhost o URL indicada.
    POR QUÉ: Valida mecánicamente que no existan enlaces rotos (404) ni violaciones de accesibilidad WCAG (enlaces idénticos apuntando a destinos diferentes).
    """
    # Por defecto, probamos el entorno de integración local
    base_url = "http://localhost"
    
    if len(sys.argv) > 1:
        base_url = sys.argv[1].rstrip('/')

    # Cola de URLs por visitar (set de tuplas)
    to_visit = {(base_url, "Punto de entrada (Manual)")}
    visited = set()
    broken_links = []
    wcag_errors = []
    
    print(f"🚀 [Merci LinkCheck] Iniciando rastreo profundo en: {base_url}")
    
    # 50 trabajadores es un número seguro para un Nginx local sin riesgo de denegación de servicio.
    with ThreadPoolExecutor(max_workers=50) as executor:
        while to_visit:
            futures = []
            for url_info in to_visit:
                clean_url = urlparse(url_info[0])._replace(fragment="").geturl()
                
                if clean_url in visited or clean_url.startswith(('mailto:', 'tel:', 'javascript:')):
                    continue
                visited.add(clean_url)
                futures.append(executor.submit(fetch_and_parse, (clean_url, url_info[1]), base_url))
                
            to_visit = set()
            for future in as_completed(futures):
                clean_url, new_urls, errors, broken = future.result()
                
                if broken:
                    broken_links.append(broken)
                    c_url, s_url, reason = broken
                    if reason.isdigit():
                        print(f"❌ Roto: {c_url} (HTTP {reason})\n   ↳ Encontrado en: {s_url}\n")
                    else:
                        print(f"❌ Error conexión: {c_url}\n   ↳ {reason}\n")
                        
                for err in errors:
                    wcag_errors.append(err)
                    print(f"♿❌ Error WCAG: {err[0]}\n   ↳ El enlace con texto/label '{err[1]}' apunta a múltiples destinos distintos.\n")
                    
                for n_url, source in new_urls:
                    if n_url not in visited:
                        to_visit.add((n_url, source))
            
    print("--- Resumen del Rastreo ---")
    print(f"🔗 URLs únicas validadas: {len(visited)}")
    
    if broken_links or wcag_errors:
        if broken_links:
            print(f"⚠️  Se encontraron {len(broken_links)} enlaces rotos.")
        if wcag_errors:
            print(f"⚠️  Se encontraron {len(wcag_errors)} violaciones WAI-ARIA (Enlaces ambiguos).")
        sys.exit(1)
    else:
        print("✅ Estado: Perfecto. Arquitectura unificada sin enlaces rotos.")
        sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 [Merci LinkCheck] Rastreo interrumpido por el usuario.")
        sys.exit(130)