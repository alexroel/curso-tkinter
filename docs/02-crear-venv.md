# Entorno Virutales en Python
Un entorno virtual es una herramienta que ayuda a mantener las dependencias de un proyecto aisladas de otros proyectos. Esto es especialmente útil cuando se trabaja en múltiples proyectos que pueden requerir diferentes versiones de las mismas bibliotecas.

1. [Crear un entorno virtual](#crear-un-entorno-virtual)
2. [Activar el entorno virtual](#activar-el-entorno-virtual)
3. [Desactivar el entorno virtual](#desactivar-el-entorno-virtual)
4. [Instalar dependencias](#instalar-dependencias)
5. [Comandos útiles](#comandos-útiles)
6. [Conclusión](#conclusión)

---
## Crear un entorno virtual
Para crear un entorno virtual en Python, puedes usar el módulo `venv` que viene incluido en la biblioteca estándar.

En linux como ya biene instalado Python, pude que `venv` no esté instalado, para instalarlo puedes usar el siguiente comando:

```bash
sudo apt install python3-venv
```
Para crear un entorno virtual, abre tu terminal y ejecuta el siguiente comando, reemplazando `nombre_del_entorno` con el nombre que deseas darle a tu entorno virtual:

```bash
py -m venv nombre_del_entorno # Windows
python3 -m venv nombre_del_entorno # macOS/Linux
```

Por ejemplo, si quieres crear un entorno virtual llamado `.env`, puedes ejecutar:
```bash
py -m venv .env # Windows
python3 -m venv .env # macOS/Linux
```

---
## Activar el entorno virtual
Una vez que hayas creado el entorno virtual, necesitas activarlo para usarlo. La forma de activar el entorno virtual depende del sistema operativo que estés utilizando.

```bash
# Windows
.\nombre_del_entorno\Scripts\activate
# macOS/Linux
source nombre_del_entorno/bin/activate
```
Después de activar el entorno virtual, verás el nombre del entorno entre paréntesis en tu terminal, lo que indica que estás trabajando dentro de ese entorno.

---
## Desactivar el entorno virtual
Cuando hayas terminado de trabajar en tu proyecto y quieras salir del entorno virtual, simplemente puedes desactivarlo con el siguiente comando:
```bash
deactivate
```
Esto te devolverá a tu entorno global de Python. 

---
## Instalar dependencias
Una vez que el entorno virtual esté activado, puedes instalar las dependencias necesarias para tu proyecto utilizando `pip`. Por ejemplo:
```bash
pip install nombre_de_la_dependencia
```

Recuerda que las dependencias instaladas dentro del entorno virtual no afectarán a otros proyectos ni al entorno global de Python. Esto te permite mantener tus proyectos organizados y evitar conflictos entre diferentes versiones de bibliotecas.

---
## Comandos útiles
- Para listar las dependencias instaladas en el entorno virtual:
```bash
pip list
```
- Para generar un archivo `requirements.txt` con las dependencias instaladas:
```bash
pip freeze > requirements.txt
```
- Para instalar las dependencias desde un archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

- Para desinstalar una dependencia:
```bash
pip uninstall nombre_de_la_dependencia
```
Con estos comandos, puedes gestionar fácilmente las dependencias de tu proyecto y mantener un entorno de desarrollo limpio y organizado.


---
## Conclusión
Crear y usar entornos virtuales es una práctica recomendada en el desarrollo de proyectos en Python. Te permite mantener tus proyectos organizados, evitar conflictos de dependencias y asegurarte de que tu entorno de desarrollo sea reproducible. Asegúrate de activar tu entorno virtual cada vez que trabajes en tu proyecto para aprovechar al máximo sus beneficios.
