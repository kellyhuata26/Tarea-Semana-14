README.md – Restaurante App (Semana 13)
Introducción
Este proyecto corresponde a la Semana 13 de la asignatura Programación Orientada a Objetos y tiene como objetivo iniciar la transición de la aplicación restaurante_app desde una versión basada en consola hacia una versión con interfaz gráfica de usuario utilizando Tkinter.

La finalidad de esta etapa no es trasladar todas las funcionalidades de la aplicación de consola, sino comprender cómo se integran la ventana principal, las vistas gráficas y los servicios. A partir de esta base, el sistema se ampliará progresivamente en las siguientes semanas.

Estructura del proyecto
La organización sigue el mismo principio del proyecto docente Biblioteca App, adaptado al contexto del restaurante:

Código
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
datos/: contiene los archivos JSON con información de productos y usuarios.

modelos/: define las clases Producto y Usuario.

servicios/: implementa la lógica de lectura de archivos y operaciones del restaurante.

ui/: incluye las vistas gráficas LoginView y MainView.

main.py: punto de entrada que inicializa Tkinter, carga servicios y controla el flujo de vistas.

README.md: documentación del sistema.

Flujo de la aplicación
Inicio de la aplicación → ejecución de main.py.

LoginView → pantalla de acceso con usuario y contraseña.

Validación → RestauranteServicio comprueba credenciales.

MainView → interfaz principal con productos y usuarios registrados.

Cerrar sesión → regresa al login dentro de la misma ventana.

Funcionalidades implementadas
LoginView: permite ingresar usuario y contraseña, valida credenciales y muestra mensajes de error en caso de datos incorrectos.

MainView: muestra la lista de usuarios y productos cargados desde archivos JSON.

Servicios: toda la lógica de validación y carga de datos se concentra en RestauranteServicio, evitando que las vistas accedan directamente a los archivos.

Flujo completo: login → interfaz principal → consulta de información → cierre de sesión.

Ejecución del proyecto
Clonar el repositorio desde GitHub.

Instalar Python 3.x en el sistema.

Ejecutar el archivo principal:

bash
python main.py
Ingresar credenciales válidas (ejemplo: usuario admin, contraseña 1234).

Visualizar la interfaz principal con usuarios y productos.

Observaciones
El acceso es una simulación pedagógica, no representa un sistema real de autenticación segura.

Las funcionalidades avanzadas (ventas, reportes, etc.) se incorporarán en semanas posteriores.

Se mantienen una única ventana principal y un único ciclo de ejecución (mainloop).

Conclusión
Este proyecto constituye la base gráfica inicial del sistema restaurante_app, adaptada al modelo docente de la Semana 13. Permite comprender la separación de responsabilidades entre modelos, servicios y vistas, así como el flujo de interacción entre login y la interfaz principal.