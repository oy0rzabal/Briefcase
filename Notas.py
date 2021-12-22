-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Instalacion y Activacion de Cookiecutter
mkdir "Creamos la carpeta donde queremos instalar Cookiecutter"

cd #Ingresamos a la carpeta creada anteriormente

conda config --add channels conda-forg #Configurar para que se vaya directamente la intalacion a esa carpeta y a conda global

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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------------------------------------------