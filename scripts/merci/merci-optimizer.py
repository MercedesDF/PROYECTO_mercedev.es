#!/usr/bin/env python3
import os
import glob
from PIL import Image

# Sistema Merci - Optimizador Multimedia (Fase 3)
# Busca imágenes en bruto (.assets-raw/) y las optimiza proporcionando
# un formato moderno WebP a menor tamaño y mayor rendimiento hacia /assets

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '.assets-raw')
OUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'assets')

# Definimos los breakpoints en los que exportar. sm para móviles (Fase Mobile-First), lg para escritorio
SIZES = {
    'sm': 640,
    'lg': 1920
}

def resize_and_convert():
    """Busca imágenes en formatos base y las transiciona al formato final WebP"""
    # Verifica y crea directorio si no lo hay
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
        
    print("Merci: Evaluando imágenes crudas (RAW) en el directorio .assets-raw...")
    
    # Recoge todos los medios gráficos base jpg y png admitidos
    raw_images = glob.glob(os.path.join(RAW_DIR, '*.jpg')) + glob.glob(os.path.join(RAW_DIR, '*.png'))
    
    # Prevenir si está vacío el directorio origen (-raw solo tiene .gitkeep temporal)
    if not raw_images:
        print("Merci: No se encontraron originales multimedia para procesar.")
        return

    # Procesa cada imagen detectada
    for img_path in raw_images:
        filename_ext = os.path.basename(img_path)
        base_name, _ = os.path.splitext(filename_ext)
        
        try:
            # Abrir el objeto en memoria utilizando el módulo Pillow Image
            img = Image.open(img_path)
            
            # Algunos PNG tienen un canal alfa transparente temporal, se quitan transiciones a RGB
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Por cada medida parametrizada, hacer los recortes y salvar en disco duro
            for size_label, target_width in SIZES.items():
                
                # Asegura no escalar una imagen pequeña al revés si mide menos que nuestro corte
                ratio = target_width / float(img.size[0])
                if ratio < 1:  
                    # Determina alto proporcional en base a ancho deseado
                    target_height = int((float(img.size[1]) * float(ratio)))
                    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                else: # Si el origen ya es chico
                    resized_img = img
                
                # Define el enrutamiento con el sufijo (ej: imagen1-sm.webp)
                out_path = os.path.join(OUT_DIR, f"{base_name}-{size_label}.webp")
                
                # Codificar en modo 'webp' con calidad 85 (el mejor equilibrio rendimiento-visual)
                resized_img.save(out_path, 'webp', quality=85)
                print(f"Merci: Procesamiento finalizado, imagen volcada -> {out_path}")
                
        except Exception as e:
            print(f"Merci Error: Imposible procesar la fotografía {filename_ext}. Motivo de Python: {e}")

if __name__ == "__main__":
    resize_and_convert()
