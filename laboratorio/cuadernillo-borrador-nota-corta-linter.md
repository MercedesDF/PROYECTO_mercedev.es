Here is the output:

```
---
titulo: "Optimización de RAG (Filtrado Semántico) para LLM Local"
descripcion: "Solución técnica para evitar la saturación del modelo local al enviar entradas de bitácora con contexto masivo."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-08"
fase: ""
estado: "borrador"
alt_portada: "Descripción visual de la imagen de portada para accesibilidad WAI-ARIA."
---

## El Desafío (Síntoma)
Se detectó que el sistema RAG anterior enviaba 6000 caracteres ciegos de historial al modelo local (Llama 3), saturando su ventana de atención (*Context Window Stuffing*) y provocando alucinaciones.

## La Maniobra (Lógica)
Explicación: Se refactorizó `get_bitacora_context` en `merci-librarian.py`. El script ahora extrae palabras clave (>4 letras) de la nota cruda y las utiliza para escanear y enviar únicamente las entradas de bitácora que contengan esas palabras, limitando el tamaño a 3000 caracteres.

## El Aprendizaje / Deuda Técnica
La solución técnicamente optimiza el envío de entradas de bitácora al modelo local, evitando la saturación y garantizando la robustez del comportamiento de contingencia (Fallback) cuando la IA en la nube no está disponible.