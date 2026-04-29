# SOP: Mantenimiento y Actualización del Boilerplate

Este documento define el Procedimiento Operativo Estándar (SOP - Standard Operating Procedure) para gobernar las actualizaciones de la plantilla pública `merci-boilerplate`. 

Dado que `mercedev.es` actúa como la Única Fuente de Verdad (SSOT - Single Source of Truth), **jamás se debe modificar el código directamente en el repositorio del Boilerplate**. Todo parche o mejora se programa en la matriz y se "exporta" siguiendo este ciclo estricto para evitar la Deriva de Configuración (Configuration Drift).

## El Release Pipeline (Paso a Paso)

Para liberar una nueva versión (ej. pasar de `v1.0.0` a `v1.1.0`), ejecuta la siguiente secuencia en tu terminal:

### 1. Preparación en la Matriz
Asegúrate de que `mercedev.es` está auditado, commiteado y subido a GitHub (`git push`).
Si hay un cambio de versión, actualiza el número manualmente en el archivo `README-merci.md`.

### 2. Clonación Efímera
Sal de tu entorno de trabajo actual y clona la versión más reciente desde el servidor a un directorio temporal neutral (ej. tu Escritorio):
```bash
cd ~/Escritorio
git clone git@github.com:MercedesDF/PROYECTO_mercedev.es.git clon-temporal
cd clon-temporal
```

### 3. La Guillotina (Instanciación)
Ejecuta el script destructivo para limpiar la identidad original, purgar el historial documental y ascender los *Shadow Docs* (Documentación en la sombra):
```bash
python3 scripts/merci/merci-init.py
```
*(Cuando te pregunte, introduce "DESTRUIR" y datos genéricos de prueba).*

### 4. Limpieza del Historial
Elimina la memoria de versiones del clon temporal para no arrastrarla al destino:
```bash
rm -rf .git
```

### 5. Sincronización Ágil (Rsync)
Copia los archivos limpios hacia tu directorio local del Boilerplate, ignorando los archivos estructurales que no deben viajar:
```bash
# El flag --delete es CRÍTICO: actúa como un espejo destructivo. 
# Elimina del Boilerplate cualquier "archivo fantasma" de versiones anteriores
# que haya sido purgado en el clon temporal por merci-init.py.
rsync -av --delete --exclude='.git' . ~/Escritorio/merci-boilerplate/
```

### 6. QA y Sello (En el repositorio destino)
Entra en la carpeta del Boilerplate, verifica que no haya errores y empaqueta la nueva versión:
```bash
cd ~/Escritorio/merci-boilerplate/
python3 scripts/merci/merci-total.py
git add .
git commit -m "feat: Release v1.X.X - Descripción breve de la actualización"
git push origin main
```

### 7. Limpieza Final
Borra el directorio efímero de tu escritorio para no dejar basura:
```bash
rm -rf ~/Escritorio/clon-temporal
```