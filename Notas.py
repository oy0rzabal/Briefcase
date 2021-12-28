-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Instalacion y Activacion de Cookiecutter
mkdir "Creamos la carpeta donde queremos instalar Cookiecutter"

cd #Ingresamos a la carpeta creada anteriormente

conda config --add channels conda-forge #Configurar para que se vaya directamente la intalacion a esa carpeta y a conda global

#Crear ambiente
conda create --name "Nombre de la carpeta" cookiecutter=1.7.3

#Ir al ambiente
conda activate "Nombre de la carpeta"
#o salir del ambiente
conda descativate "Nombre de la carpeta"
#Exportar el ambiente
conda env export --from-history --file environment.yaml#Vamos hacer que los pasos anteriormente echos se pasen a ese archivo llamado "enviromment.yaml"

#Ver el archivo 
cat environment.yaml

#Crear la plantilla con cookiecutter
cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi

#Se puede ir directo al git para mas informacion sobre la cracion de plantillas

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Intalacion en pip dentro de nuestro entorno creado anteriormente
pip intall cookiecutter

#Despues Iniciamos el proyecto:
python3 -m cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout estate_project
------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Estructura Exacta de la plantilla de cookiecutter:

├── LICENSE
├── Makefile           <- Makefile con comandos como `make data` o` make train`
├── README.md          <- El archivo README de nivel superior para desarrolladores que utilizan este proyecto.
├── data
│   ├── external       <- Datos de fuentes de terceros.
│   ├── interim        <- Datos intermedios que se han transformado.
│   ├── processed      <- Los conjuntos de datos canónicos finales para el modelado.
│   └── raw            <- El volcado de datos original e inmutable.
│
├── docs               <- Un proyecto Sphinx predeterminado; consulte sphinx-doc.org para obtener más detalles
│
├── models             <- Modelos entrenados y serializados, predicciones de modelos o resúmenes de modelos
│
├── notebooks          <- Cuadernos Jupyter. La convención de nomenclatura es un número (para ordenar), 
│						  las iniciales del creador y una breve descripción delimitada por "-", p. 
│						  Ej. `1.0-jqp-initial-data-explore`.
│
├── references         <- Diccionarios de datos, manuales y todos los demás materiales explicativos.
├── reports            <- Análisis generado como HTML, PDF, LaTeX, etc.
│   └── figures        <- Gráficos y figuras generados para su uso en informes.
│
├── requirements.txt   <- El archivo de requisitos para reproducir el entorno de análisis, p. Ej.                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Haga que este proyecto pip se pueda instalar con `pip install -e`
├── src                <- Código fuente para usar en este proyecto.
│   ├── __init__.py    <- Hace que src sea un módulo de Python
│   │
│   ├── data           <- Scripts para descargar o generar datos
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts para convertir datos sin procesar en características para modelar
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts para entrenar modelos y luego usar modelos entrenados para hacer
│   │   │                 predicciones
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts para crear visualizaciones exploratorias y orientadas a resultados
│       └── visualize.py
│
└── tox.ini            <- archivo tox con configuraciones para ejecutar tox; ver tox.readthedocs.io


------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------------