---
titulo: "SOS Terminal: Sincronización de requirements.txt sin instanciar"
descripcion: "Comando salvavidas para parchear la deriva de dependencias seguras en el Boilerplate público directamente desde la matriz."
tipo: "art-de-cote"
tema: "SOS Terminal"
estado: "borrador"
alt_portada: "Consola de terminal ejecutando comandos de copia y git push"
---

### El Desafío (Síntoma)
Dependabot puede lanzar alertas de vulnerabilidad en el repositorio público del Boilerplate si este viajó a la nube con un `requirements.txt` obsoleto antes de que la matriz fuera asegurada. El flujo oficial dicta volver a instanciar el proyecto completo con `merci-init.py`, lo cual es un proceso lento para un solo archivo de configuración.

### La Maniobra (Lógica)
Para vulnerabilidades críticas en la cadena de suministro (Supply Chain) de un solo archivo plano, podemos inyectar el archivo saneado de la matriz directamente en el clon temporal del Boilerplate, saltándonos la instanciación destructiva.

```bash
# 1. Copia el archivo sano de tu matriz al boilerplate
cp <ruta-matriz>/requirements.txt <ruta-boilerplate>/

# 2. Entra en la carpeta del boilerplate
cd <ruta-boilerplate>/

# 3. Guarda y sube el parche de seguridad
git add requirements.txt
git commit -m "Fix: Sincronización de dependencias seguras (Supply Chain)"
git push
```

### El Aprendizaje/Deuda Técnica
*Bypass Controlado*. Los atajos operativos en DevSecOps están permitidos si, y solo si, la acción **mantiene la paridad exacta** entre la matriz y el Boilerplate. Al copiar literalmente el archivo saneado, garantizamos que ambos ecosistemas operen bajo la misma política de "Zero Vulnerabilities" sin fricción operativa.