# Bienvenidos al espacio de integración de la actividad N02 de analisis numerico

Para empezar es necesario que tengas instalado una version de python 3.10 > actual y del editor de texto ``Visual studio code`` para poder inciar, posteriormente requieres de clonar el repositorio para realizar los siguientes pasos.

### Instalación del entorno virtual
----
Se requiere de un espacio virtualizado como es el caso del ``.venv`` para no manchar tu entorno global, a continuación puede observar los siguientes comandos.


en la consola del VScode escribe
```PowerShell
python -m venv .venv
```
Esta instrucción permite generar el archivo ``.venv``, se recomienda que espere unos minutos hasta que termine de cargar el entorno.

Seguidamente ejecute este comando para activar el entorno virtual
```PowerShell
.venv/Scripts/activate
```

- Para desactivar el entorno virtual ejecute el comando 
```PowerShell
deactivate
```

Seguirdamente requiere de instalar las dependencias con el siguiente comando, no es necesario que usted instale de forma manual las dependencias que exige el proyecto.

(ADVERTENCIA): Antes de ejecutar este comando verifique que el entorno virtual este habilitado.

```PowerShell
pip install -r requirements.txt
```

### Linkerd de las dependencias, rutas y archivos 
----
Este es importante, ya que permite reconocer las rutas, directorios y archivos al interprete de python (como tal python no es muy bueno al momento de implementar elementos de otras dependencias), asi que este medio es una solución a los problemas de ejecución presentes. A continuación, los siguientes comandos:

Este comando nos asegura establecer el espacio para la caché de los linkerds 

(ADVERTENCIA): Antes de ejecutar el siguiente comando verifique que usted se encuentra en la ruta raiz de este proyecto 

```PowerShell
pip install -e .
```

Despues de ejecutar la instrucción, ustede verá algo como esto:

![linked_n01](public/Captura%20de%20pantalla%202026-09-16%20135525.png)

el directorio llamado `` trabajo_n02.egg-info`` significa que se ha realizado de forma exitosa

### IMPORTANTE
----
El boton de ejecución que aparece en el panel superior de VScode no servirá para ejecutar los algoritmos de este proyecto

muestra del error: 
![linked_n02_error](public/Captura%20de%20pantalla%202026-09-16%20140141.png)

esto se debe a que el compilador de python no ejecuta el codigo con el caché, esto probocando el error ``No module named 'core'``

Por eso es necesario que usted realice el siguiente paso:
- Cuando usted se situe en un algoritmo, presione click derecho, seguidamente selecciones la opción ``Run Python``, usted encontrará 2 opciones seleccione ``Run Python File in Terminal`` para ejecutarlo en la terminal 

![linked_n03_options](public/Captura%20de%20pantalla%202026-09-16%20140350.png)

Al finalizar te arrojará la tabla con los datos preseleccionados, segun el ejercicio que hayas preseleccionado.

![linked_n04_result](public/Captura%20de%20pantalla%202026-09-16%20140424.png)



