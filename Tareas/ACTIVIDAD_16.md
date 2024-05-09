### Actividad 16: Fundamentos Tecnológicos de la Computación en la Nube

#### Objetivos:
La computación en la nube ofrece elasticidad al compartir recursos entre usuarios con diferentes necesidades informáticas. ¿Cómo logra esto y cuáles son las tecnologías clave que la hacen posible? El objetivo de esta actividad es abordar estas preguntas.

#### Caso de Estudio 6: Startup de IoT - IoT Innovations
- *Empresa:* IoT Innovations
- *Qué hace:* Desarrolla soluciones para conectar y gestionar dispositivos IoT en diversas industrias.
- *Servicios AWS utilizados:* AWS IoT Core, Amazon Kinesis, AWS Greengrass.
- *Beneficios de AWS:* Integración segura y gestión de dispositivos IoT, análisis en tiempo real de datos, capacidad para operar localmente en dispositivos.

#### Preguntas:
1. ¿Te resulta claro cómo AWS IoT Core ayuda a gestionar dispositivos IoT? ¿Qué áreas necesitan más claridad?
2. Si IoT Innovations decidiera no usar la nube, ¿qué desafíos enfrentaría en la gestión de dispositivos IoT y en el procesamiento de datos?
3. ¿Qué ventajas adicionales crees que AWS proporciona a las startups de IoT que no se mencionaron?

---

### Proyecto: Prototipo Clasificador de Agua para IoT

#### Contexto del Proyecto:
Nuestro equipo está desarrollando un prototipo de clasificador de agua basado en IoT. Este dispositivo utiliza sensores de pH, turbidez y conectividad eléctrica para analizar el agua y separarla en depósitos destinados al riego de plantas y al uso cotidiano. El objetivo es proporcionar una solución eficiente y automatizada para la gestión del agua en entornos domésticos y agrícolas.

#### Respuestas a las Preguntas:
1. *¿Te resulta claro cómo AWS IoT Core ayuda a gestionar dispositivos IoT? ¿Qué áreas necesitan más claridad?*
   Sí, AWS IoT Core facilita la gestión y la comunicación segura entre los dispositivos IoT y la nube. Para nuestro proyecto, AWS IoT Core nos permitiría conectar los sensores de nuestro clasificador de agua y enviar los datos recopilados de forma segura a la nube para su procesamiento y análisis. Sin embargo, podríamos necesitar más claridad sobre cómo configurar y gestionar las reglas de enrutamiento de mensajes en AWS IoT Core para garantizar un flujo eficiente de datos y una respuesta rápida a eventos específicos.

2. *Si IoT Innovations decidiera no usar la nube, ¿qué desafíos enfrentaría en la gestión de dispositivos IoT y en el procesamiento de datos?*
   Si optamos por no utilizar la nube, enfrentaríamos varios desafíos en la gestión de dispositivos IoT y en el procesamiento de datos. Tendríamos que desarrollar nuestra propia infraestructura de servidor para almacenar y procesar los datos de los sensores, lo que implicaría una inversión significativa en hardware y recursos humanos. Además, tendríamos que implementar medidas de seguridad y redundancia por nuestra cuenta para proteger los datos y garantizar la disponibilidad del sistema.

3. *¿Qué ventajas adicionales crees que AWS proporciona a las startups de IoT que no se mencionaron?*
   Además de las ventajas mencionadas, AWS proporciona a las startups de IoT acceso a una amplia gama de servicios adicionales que pueden mejorar la escalabilidad, la fiabilidad y la seguridad de sus soluciones. Por ejemplo, con servicios como Amazon Kinesis, podríamos procesar y analizar grandes volúmenes de datos en tiempo real para obtener información valiosa sobre la calidad del agua y el rendimiento del sistema. Además, AWS Greengrass nos permitiría ejecutar código en dispositivos edge para una mayor eficiencia y capacidad de respuesta en entornos desconectados o con ancho de banda limitado. En resumen, AWS ofrece un ecosistema completo de servicios en la nube que puede impulsar la innovación y el crecimiento de las startups de IoT.
