---
titulo: "Cierre Estratégico de Épica 9: Antigravity SRE, Chaos Engineering y Refinamiento CSS"
descripcion: "Compendio de decisiones arquitectónicas clave para el cierre de la Épica 9, abarcando la sustitución de Ollama, la evolución del Chaos Engineering, la expansión SRE y la preservación de herramientas estériles."
tipo: "compendio"
tema: "DevSecOps e Infraestructura"
fecha: "2026-06-18"
fase: "Epic 9 - Cierre"
estado: "publicado"
alt_portada: "Representación visual abstracta de un sistema distribuido con nodos interconectados, algunos con iconos de gravedad cero (Antigravity), otros con símbolos de caos o fallos controlados, y un panel de métricas de rendimiento y accesibilidad, todo ello sobre un fondo que sugiere código CSS optimizado."
---
## El Desafío (Síntoma)
Se detectó la necesidad de consolidar y formalizar las decisiones arquitectónicas clave tomadas durante la Épica 9, la cual se centró en la fiabilidad avanzada del sistema (SRE - Site Reliability Engineering), la resiliencia mediante Chaos Engineering y la optimización del front-end a través del refinamiento de CSS (Cascading Style Sheets - Hojas de Estilo en Cascada). El objetivo era destilar las lecciones aprendidas y las implementaciones estratégicas para asegurar un cierre de epic coherente y documentado.

## La Maniobra (Lógica)
Para abordar el desafío, se ejecutaron varias maniobras arquitectónicas fundamentales:

*   **Sustitución de Ollama por Enrutamiento Híbrido hacia Gemini Proxy (Antigravity):** Se implementó una estrategia de enrutamiento híbrido para las capacidades de inteligencia artificial, migrando la dependencia de Ollama hacia Gemini Proxy. Esta decisión se tomó para optimizar la gestión de recursos de IA, mejorar la flexibilidad y aumentar la resiliencia del sistema, alineándose con los principios de Antigravity SRE.
*   **Evolución del Chaos Engineering y Validación del Fallback:** Se expandió la aplicación de técnicas de Chaos Engineering para someter el sistema a pruebas de estrés controladas. Se puso un énfasis particular en la validación exhaustiva de los mecanismos de fallback, asegurando que el sistema pudiera recuperarse de fallos simulados de manera predecible y eficiente, minimizando el impacto en la disponibilidad.
*   **Expansión SRE (Zero-Bloat en el peso de `public/` y Métricas de Accesibilidad):** Se llevó a cabo una expansión de las prácticas de SRE, con un enfoque primordial en la optimización del rendimiento y la reducción del "bloat" (exceso de peso) en el directorio `public/`. Paralelamente, se establecieron y monitorearon métricas estrictas de accesibilidad para garantizar una experiencia de usuario inclusiva y de alto rendimiento.
*   **Preservación de Herramientas Estériles:** Se identificaron y preservaron aquellas herramientas consideradas "estériles" o de bajo impacto en la huella de dependencia del proyecto. Esta medida se adoptó para mantener la simplicidad del stack tecnológico y evitar la introducción de complejidades innecesarias, contribuyendo a la estrategia de cero dependencias y a la eficiencia operativa.

## El Aprendizaje / Deuda Técnica
Se ha consolidado la comprensión de que la resiliencia y la eficiencia de un sistema no solo se logran mediante la implementación de tecnologías avanzadas, sino también a través de una gestión proactiva de las dependencias y una validación continua de los mecanismos de recuperación. La adopción de un enrutamiento híbrido para la IA y la expansión del Chaos Engineering han demostrado ser fundamentales para construir un sistema robusto y adaptable. La atención al "Zero-Bloat" y a las métricas de accesibilidad subraya la importancia de un enfoque holístico en SRE, donde el rendimiento y la experiencia del usuario son tan críticos como la fiabilidad. No se identificó deuda técnica significativa, ya que las decisiones se orientaron a la simplificación y la robustez a largo plazo.

### 💡 En resumen (Merci Explica):
Para finalizar una etapa importante del proyecto, se decidió cambiar la forma en que el sistema utiliza la inteligencia artificial, optando por una solución más flexible que puede usar diferentes servicios. También se realizaron pruebas intensivas para ver cómo reacciona el sistema cuando algo falla, asegurándose de que siempre tenga un "plan B" para seguir funcionando sin interrupciones. Además, se trabajó para que la página web cargue muy rápido y sea fácil de usar para todas las personas, eliminando elementos innecesarios y cuidando la accesibilidad. Finalmente, se decidió mantener solo las herramientas esenciales para no complicar el sistema. Todo esto se hizo para que el proyecto sea más fuerte, rápido y fácil de mantener en el futuro.