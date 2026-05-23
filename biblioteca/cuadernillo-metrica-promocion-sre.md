---
titulo: "Métrica SRE Exacta para Documentos en Promoción"
descripcion: "Se implementó la métrica merci_documentos_promocion_total en merci-sre.py para alinear la telemetría con la realidad operativa."
tipo: "cuadernillo"
tema: "DevSecOps y Gobernanza"
fecha: "2026-05-12"
fase: "Epic 2 - Fase 4"
estado: "publicado"
alt_portada: "Métrica SRE para contar documentos en promoción en el laboratorio."
---
<!-- linkedin:
Se implementó una métrica SRE exacta para contar documentos en promoción en el laboratorio, alineando la telemetría con la realidad operativa. 📊 #DevSecOps #Gobernanza
-->

## El Desafío (Síntoma)
Se detectó que Grafana y nuestro CLI hablaban idiomas distintos. `merci-promote.py` escanea todo el laboratorio buscando archivos con estado 'borrador', pero nuestra métrica SRE antigua solo contaba archivos físicos en la carpeta incubacion/. Para lograr una observabilidad perfecta, era necesario contar con una métrica que reflejara los archivos reales listos para ser promovidos.

## La Maniobra (Lógica)
Se implementó la métrica `merci_documentos_promocion_total` en `scripts/merci/merci-sre.py`. Esta nueva métrica utiliza `rglob` y Expresiones Regulares (`re.search`) para buscar recursivamente la firma YAML `estado: "borrador"` en cualquier subcarpeta del laboratorio. Esto alinea la telemetría exacta con la realidad operativa, permitiendo ver en el Dashboard DevSecOps cuántos archivos están realmente listos para ser promovidos.

## El Aprendizaje / Deuda Técnica
La solución es la óptima porque utiliza el mismo criterio de filtrado que `merci-promote.py`, garantizando consistencia y precisión en la medición. No se ha asumido ninguna deuda técnica significativa para el futuro, ya que la implementación es directa y no requiere cambios adicionales en otros sistemas.