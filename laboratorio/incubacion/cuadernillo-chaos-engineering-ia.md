---
titulo: "Implementación de Rollback Robusto con Qwen 2.5 Coder"
descripcion: "Se implementó un rollback robusto utilizando git restore dentro de un bloque try...finally para prevenir la infección del código durante pruebas de Chaos Monkey."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-12"
fase: "Épica 2 - Fase 4"
estado: "borrador"
alt_portada: "Diagrama de flujo mostrando el proceso de rollback robusto con git restore dentro de un bloque try...finally."
---

**linkedin:
Implementamos un rollback robusto utilizando git restore dentro de un bloque try...finally para prevenir la infección del código durante pruebas de Chaos Monkey. #DevSecOps #Gobernanza
**

## El Desafío (Síntoma)
Se detectó que el mecanismo de Rollback en nuestro script `merci-chaos.py` no estaba protegido contra interrupciones manuales, lo que podía dejar el código envenenado.

## La Maniobra (Lógica)
Implementamos un bloque `try...finally` alrededor del comando `git restore` para asegurar que el rollback se ejecute incluso si ocurre una interrupción manual como Ctrl+C. Esto garantiza que el código no quede en estado inestable.

```python
try:
    # Código susceptible a vulnerabilidades
    pass
finally:
    git.restore('ruta/a/archivo')
```

## El Aprendizaje / Deuda Técnica
Aprendimos la importancia de proteger contra interrupciones manuales durante pruebas de Chaos Monkey. Esta solución evita dejar el código envenenado y asegura que las barreras Shift-Left sean infranqueables.