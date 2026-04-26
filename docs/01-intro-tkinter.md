# Introducción a Tkinter
Tkinter es la biblioteca de interfaces gráficas de usuario (GUI) estándar para Python. Proporciona una forma sencilla de crear aplicaciones con interfaces gráficas utilizando el lenguaje de programación Python. Tkinter es una envoltura alrededor de la biblioteca gráfica Tcl/Tk, lo que permite a los desarrolladores crear aplicaciones GUI de manera rápida y eficiente.

1. [Instalación](#instalación)
2. [Tu Primera Ventana en Python](#tu-primera-ventana-en-python)


---
## Instalación
Tkinter generalmente viene preinstalado con Python, por lo que no es necesario instalarlo por separado. Sin embargo, si estás utilizando una distribución de Python que no incluye Tkinter, puedes instalarlo utilizando el siguiente comando:

```bash
pip install tk
```
Para verificar si Tkinter está instalado correctamente, ver la versión de Python y asegurarse de que Tkinter esté disponible:

```python
import tkinter as tk
print(tk.TkVersion)
```

---
## Tu Primera Ventana en Python

¡Bienvenido al mundo de las interfaces gráficas! En esta guía del Módulo 1, dejaremos atrás la aburrida pantalla negra de la consola (terminal) y aprenderemos a crear nuestra primera ventana real de computadora usando Tkinter.

No te preocupes si nunca has hecho esto antes, te lo explicaré paso a paso y con ejemplos muy sencillos.

### 1. ¿Qué es una Interfaz Gráfica (GUI)? 🤔

Antes de programar, imagina que vas a un restaurante.

El código (Python normal): Es como la cocina. Hay instrucciones paso a paso para hacer la comida, pero los clientes no entran ahí.

La GUI (Interfaz Gráfica): Es el menú y el camarero. Es la forma bonita y fácil en la que el cliente interactúa con la cocina sin tener que saber cocinar.

Una GUI (Graphical User Interface) son las ventanas, botones y textos que ves en cualquier programa de tu computadora. Tkinter es la herramienta de Python que nos ayuda a construir ese "menú" visual.

### 2. El primer paso: Importar las herramientas 🧰

Para construir una casa, primero necesitamos traer nuestra caja de herramientas. En Python, hacemos esto "importando" Tkinter.

```python
import tkinter as tk
```

Explicación simple: Le decimos a Python: "Oye, trae la caja de herramientas de Tkinter, pero para no escribir 'tkinter' a cada rato, la llamaremos simplemente 'tk'."

### 3. La Ventana Raíz (`Tk`): Tu terreno en blanco 🏗️

Todo programa visual necesita un lugar donde existir. A esto lo llamamos la Ventana Raíz. Es el rectángulo principal de tu aplicación.

```python
# Creamos nuestra ventana principal
ventana = tk.Tk()
```


Explicación simple: Es como comprar un terreno vacío. Aquí es donde pondremos nuestros botones, textos e imágenes más adelante. Al guardarlo en la variable llamada `ventana`, podemos darle órdenes a ese terreno.

### 4. Personalizando nuestra ventana 🎨

Un terreno vacío es aburrido. Vamos a ponerle un nombre, un tamaño y pintar las paredes.

- *El Título (`title`)*

Para poner el texto que aparece en la parte superior de la ventana (la barra de título).

```python
ventana.title("Mi Primera App")
```

Aplicación real: Sirve para que el usuario sepa qué programa está usando, como "Calculadora" o "Block de Notas".

- *El Tamaño (`geometry`)*

Le decimos de qué tamaño queremos que sea la ventana al abrirse. Se escribe en píxeles con el formato "AnchoxAlto".

```python
ventana.geometry("400x300")
```


Aplicación real: Un programa de calculadora necesita poco espacio (ej: 300x400), pero un programa para editar fotos necesitará mucho espacio (ej: `1024x768`).

- Bloquear el tamaño (`resizable`)

A veces no queremos que el usuario estire o encoja nuestra ventana para que no se arruine nuestro diseño.

```python
# (Ancho_modificable?, Alto_modificable?)
ventana.resizable(False, False)
```


Aplicación real: Piensa en la calculadora de Windows. Si la estiras demasiado, los botones se ven raros. Con esto, bloqueas el tamaño para que sea fijo.

- Color de fondo (`background` o `bg`)

Podemos cambiar el color de nuestra ventana usando el nombre del color en inglés o su código hexadecimal (como los de la web).

```python
ventana.configure(bg="lightblue")
```


### 5. El Ciclo de Vida: Manteniendo la luz encendida (`mainloop`) 🔄

Este es el paso más importante. Si solo escribes el código anterior, la ventana aparecerá y se cerrará tan rápido que ni la verás.

```python
ventana.mainloop()
```


Explicación simple: Imagina que abres tu restaurante. Si no le dices al personal que se quede esperando a los clientes, cerrarán la puerta inmediatamente. `mainloop()` es un ciclo infinito que le dice al programa: "Quédate abierto y espera a que el usuario haga algo (como mover el ratón o hacer clic)".

Regla de oro: Esta instrucción siempre debe ir al final de tu código.

🛠️ Juntando todo: Tu primer programa completo

Aquí tienes cómo se ve todo el código junto. Cópialo, pégalo en tu editor de código (como VS Code, PyCharm o IDLE) y ejecútalo.

```python
import tkinter as tk

# 1. Crear la ventana principal (el terreno)
ventana = tk.Tk()

# 2. Personalizar la ventana
ventana.title("Mi Primera App")        # Título
ventana.geometry("400x300")            # Tamaño (400 píxeles de ancho x 300 de alto)
ventana.resizable(False, False)        # No permitimos cambiar el tamaño
ventana.configure(bg="lightgreen")     # Color de fondo verde claro

# 3. Mantener la ventana abierta (siempre va al final)
ventana.mainloop()
```

*¡Felicidades! 🎉*

Acabas de crear tu primera ventana en Python. En el siguiente módulo, aprenderemos cómo organizar elementos (botones y textos) dentro de esta ventana para que tenga utilidad real.

---
## Elementos de la GUI (Widgets)
Ahora es el momento de comprar esos muebles. En el mundo de Tkinter, a estos elementos interactivos (botones, textos, imágenes) se les llama Widgets.

Vamos a conocer los 5 widgets más importantes que usarás en casi todos tus programas.

### 1. El Widget `Label`: Las etiquetas y letreros 🏷️

Un `Label` (etiqueta) es simplemente un texto o una imagen que pones en la pantalla. El usuario no puede modificarlo, solo leerlo o verlo.

- **Explicación simple:** Piensa en un `Label` como un cartel de "Se Vende" o una nota adhesiva (Post-it) que pegas en la pared. Sirve para dar instrucciones o mostrar información.

*Ejemplo de uso:*

```python
import tkinter as tk

ventana = tk.Tk()

# Crear un Label para texto o imágenes
texto = tk.Label(
    ventana,
    text="¡Hola! Soy un letrero",
    font=("Arial", 14),
    bg="green",
    fg="white",
    padx=20,
    pady=20,
    border=2,
    relief="raised", # Valoere = flat, groove, raised, ridge, solid, sunken, or ridge
)

texto.pack()

ventana.mainloop()
```


### 2. El Widget `Button`: Los botones de acción 🔘

Un `Button` es exactamente lo que imaginas: un botón que el usuario puede presionar. Pero un botón no sirve de nada si no hace algo, ¿verdad? Para darle una función, usamos el parámetro especial `command`.

- **Explicación simple:** Es como el timbre de una casa. Cuando alguien lo presiona (`clic`), suena la campana en el interior (se ejecuta una `función` en el código).

*Ejemplo de uso:*
```python
import tkinter as tk

ventana = tk.Tk()

# Función que se ejecuta cuando se hace clic en el botón
def saludar():
    print("Hola")

boton = tk.Button(
    ventana,
    text="Saludar",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    padx=20,
    pady=10,
    cursor="hand1", # Valores = hand1, hand2, arrow, crosshair, etc
    activebackground="green",
    activeforeground="blue",
    command=saludar, # Se ejecuta cuando se hace clic en el botón
)
boton.pack(pady=10)

ventana.mainloop()
```


(Ojo: Cuando usas command=saludar, no le pongas paréntesis a la función al final, ¡solo el nombre!)

### 3. El Widget Entry: La caja de texto corta 📝

El `Entry` (entrada) es una caja rectangular donde el usuario puede escribir texto con su teclado. Ojo: Solo permite escribir una sola línea.

- **Aplicación real:** Es lo que usas cuando escribes tu nombre de usuario, tu correo electrónico o tu contraseña en cualquier página web.

*Ejemplo de uso:*
```python
import tkinter as tk

# Entry para ingresar un nombre
nombre_entry = tk.Entry(
    ventana,
    font=("Arial", 12),
    justify="center",
    highlightbackground="blue",
    highlightcolor="blue",
    highlightthickness=2,
    fg="blue",
    
)
nombre_entry.pack(pady=20, padx=20)

def saludar():
    nombre = nombre_entry.get()    
    tk.Label(ventana, text=f"Hola {nombre}", font=("Arial", 14)).pack()

boton = tk.Button(
    ventana,
    text="Saludar",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    padx=20,
    pady=10,
    cursor="hand1",
    activebackground="green",
    activeforeground="blue",
    command=saludar,
)
boton.pack(pady=10)

ventana.mainloop()
```


### 4. El Widget `Text`: El cuaderno de notas 📖

Si `Entry` es para una sola línea (como un nombre), `Text` es para cuando necesitas que el usuario escriba muchas líneas, como un párrafo entero.

- **Aplicación real:** La sección de "Comentarios" en un blog, o un programa para escribir notas o poesía.

*Ejemplo de uso:*
```python
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Escribe un cuento corto:").pack()

# Creamos un área de texto grande (alto de 5 líneas, ancho de 30 caracteres)
area_texto = tk.Text(ventana, height=5, width=30)
area_texto.pack(pady=10)

ventana.mainloop()
```

*🏆 Resumen del Módulo*

- `Label`: Para mostrar texto o instrucciones (letreros).
- `Button`: Para que el usuario ejecute acciones (clics).
- `Entry`: Para que el usuario escriba un dato corto (una línea).
- `Text`: Para que el usuario escriba textos largos (párrafos).

---
## Variables de Control
Hasta ahora, hemos creado ventanas, organizado elementos y puesto botones y cajas de texto. Pero hay un pequeño problema: ¿cómo hacemos que nuestra interfaz se comunique fluídamente con el código detrás de ella?

Aquí es donde entran las Variables de Control.

### 1. ¿Por qué necesitamos "Variables Especiales"? 🤔

En Python normal, si creas una variable `nombre = "Juan"` y luego cambias `nombre = "Pedro"`, el valor cambia en la memoria, pero la pantalla no se entera. Los textos y cajas de Tkinter no se actualizan mágicamente.

- **Explicación simple:** Imagina que Python y tu Interfaz Gráfica (GUI) están en habitaciones separadas. Si Python cambia un número, la interfaz no lo sabe.

- **La solución:** Las Variables de Control son como un par de Walkie-Talkies. Si Python dice "cambió el valor", el walkie-talkie le avisa inmediatamente a la pantalla para que se actualice solita.

2. **Los 4 Tipos de Variables en Tkinter 🗂️**

Tkinter tiene sus propias variables específicas, dependiendo del tipo de dato que quieras guardar:

- `StringVar():` Para guardar textos (palabras, letras, frases). Es la más usada.
- `IntVar():` Para guardar números enteros (1, 5, 100, -4).
- `DoubleVar():` Para guardar números con decimales (3.14, 5.5).
- `BooleanVar():` Para guardar valores de "verdadero o falso" (True / False). Ideal para casillas de verificación (Checkbuttons).

*¿Cómo se crean?*

```python
import tkinter as tk
ventana = tk.Tk()

# Tienes que crear la ventana de Tkinter ANTES de crear estas variables
mi_texto = tk.StringVar()
mi_numero = tk.IntVar()
```


### 3. Leer y Escribir: `.get()` y `.set()` 📬

Como estas variables son especiales, no podemos simplemente poner `mi_texto = "Hola"`. Tenemos que usar comandos especiales.

- `.set(valor):` Es como escribir un mensaje nuevo y mandarlo por el walkie-talkie. Sirve para cambiar el valor.
- `.get():` Es como escuchar el walkie-talkie para saber cuál es el mensaje actual. Sirve para leer el valor.

Ejemplo Práctico: El botón que cambia el texto
En este ejemplo, enlazamos un `Label` a nuestra variable usando el parámetro `textvariable`. ¡Mira la magia!
```python
import tkinter as tk

def cambiar_mensaje():
    # Usamos .set() para cambiar el valor de la variable mágica
    variable_mensaje.set("¡El botón fue presionado!")

ventana = tk.Tk()
ventana.geometry("300x150")

# 1. Creamos la variable de control
variable_mensaje = tk.StringVar()
variable_mensaje.set("Esperando...") # Valor inicial

# 2. Conectamos la etiqueta a la variable usando 'textvariable'
# ¡Ojo! Usamos textvariable en lugar de text
etiqueta = tk.Label(ventana, textvariable=variable_mensaje, font=("Arial", 14))
etiqueta.pack(pady=20)

# 3. Un botón que ejecuta nuestra función
boton = tk.Button(ventana, text="Haz clic", command=cambiar_mensaje)
boton.pack()

ventana.mainloop()
```

*¿Lo ves? Nunca le dijimos a la etiqueta "cambia tu texto". Solo cambiamos la variable, y la etiqueta, al estar conectada, se actualizó automáticamente.*

### 4. Modo Espía: Rastrear cambios con `trace` 🕵️‍♂️

A veces queremos que algo suceda exactamente en el momento en que el usuario escribe algo, sin necesidad de que presione ningún botón de "Enviar".

Para eso usamos `.trace()`.

- **Explicación simple:** Es como ponerle un sensor de movimiento a una puerta. En cuanto la puerta se mueve (la variable cambia), el sensor enciende una luz (ejecuta una función).

Para que funcione cuando alguien escribe, usamos el modo `"w"` (que significa write o escribir).

Ejemplo Práctico: El texto de espejo
Lo que escribas en la caja de texto aparecerá instantáneamente en la etiqueta de arriba, letra por letra.
```python
import tkinter as tk

# Esta función se ejecutará cada vez que la variable cambie
# Nota: trace siempre envía 3 argumentos ocultos a la función, por eso usamos *args
def actualizar_etiqueta(*args):
    texto_actual = variable_entrada.get()
    print("El usuario está escribiendo: " + texto_actual)

ventana = tk.Tk()
ventana.geometry("300x150")

# Creamos la variable
variable_entrada = tk.StringVar()

# Le ponemos el "sensor de movimiento". 
# Cuando se escriba ("w"), ejecutará 'actualizar_etiqueta'
variable_entrada.trace("w", actualizar_etiqueta)

# Conectamos la variable a la etiqueta para que sea un "espejo"
espejo = tk.Label(ventana, textvariable=variable_entrada, font=("Arial", 16, "bold"))
espejo.pack(pady=10)

# Conectamos la misma variable a la caja de texto
caja = tk.Entry(ventana, textvariable=variable_entrada)
caja.pack(pady=10)

ventana.mainloop()
```


*🏆 Resumen del Módulo*

- Las variables normales de Python no actualizan la pantalla. Por eso usamos las variables de Tkinter.
- Usa StringVar para texto, IntVar para enteros, y BooleanVar para True/False.
- Para cambiar el valor guardado usa .set("nuevo valor"). Para leerlo, usa .get().
- Usa el parámetro textvariable en Labels o Entries para conectarlos a tu variable.
- El método .trace("w", funcion) es tu mejor amigo para reaccionar al instante cada vez que el usuario teclea algo.

---
## Escuchando al Usuario (Eventos)
Hasta ahora, la única forma que teníamos de que nuestro programa hiciera algo era cuando el usuario hacía clic en un Botón (usando `command=mi_funcion`).

Pero, ¿qué pasa si queremos que pase algo cuando el usuario presiona la tecla "Enter"? ¿O cuando mueve el ratón por la pantalla? ¿O cuando hace clic derecho?

Para todo eso, necesitamos aprender sobre los Eventos.

### 1. ¿Qué es un Evento y qué es el método `.bind()`? 🎧

Imagina que tu programa es un guardia de seguridad. Usar un `Button` normal es como darle al guardia un botón rojo en su escritorio: solo actúa cuando lo presionan.

Pero usar **Eventos** es darle al guardia un sistema de cámaras y micrófonos. Le dices: *"Si escuchas un ruido (teclado), o ves movimiento (ratón), haz esto".*

Para darle estas instrucciones al programa usamos la palabra mágica .bind(), que en inglés significa "atar" o "enlazar". Vamos a "atar" una acción del usuario con una función nuestra.

La fórmula mágica: `widget.bind("<El_Evento>", mi_funcion)`

### 2. Los Eventos más Comunes 📜

Tkinter tiene nombres específicos (escritos entre los símbolos `<` y `>`) para cada cosa que el usuario puede hacer. Aquí están los más útiles:

*Del Ratón (Mouse):*

- `<Button-1>`: Clic izquierdo normal.
- `<Button-2>`: Clic con la rueda del ratón.
- `<Button-3>`: Clic derecho.
- `<Motion>`: Mover el ratón por encima.
- `<Enter>`: Cuando el puntero del ratón entra en el área del elemento.
- `<Leave>`: Cuando el puntero del ratón sale del área.

**Del Teclado:**

- `<Return>`: La tecla "Enter" (¡Cuidado! En Tkinter, el evento se llama Return, no Enter).
- `<Escape>`: La tecla "Esc".
- `<Key>`: Cualquier tecla en general.

### 3. El misterioso paquete `event` 📦 (¡Muy Importante!)

Aquí hay una regla de oro que confunde a muchos principiantes: Cuando usas `.bind()`, Tkinter siempre le lanza un "paquete de información" a tu función.

Ese paquete contiene detalles de lo que acaba de pasar (dónde estaba el ratón, qué tecla exacta se presionó). Por lo tanto, tu función debe estar preparada para atrapar ese paquete.

Mira la diferencia:

Forma Antigua (Botón normal con command):

```python
def saludar():  # <--- Los paréntesis están vacíos
    print("Hola")
```


Forma Nueva (Con `.bind()`):
`
````py
def saludar(event): # <--- ¡Debemos poner 'event' aquí para atrapar el paquete!
    print("Hola")
````


*Nota: Puedes llamarlo `e`, `paquete` o como quieras, pero por convención siempre lo llamamos `event`.*

### 4. Ejemplos Prácticos 🚀

**Ejemplo A: Reaccionar a la tecla "Enter"**

Imagina un cuadro de texto (Entry) donde escribes tu contraseña. Quieres que al presionar la tecla "Enter" en tu teclado, el programa la revise, sin tener que usar el ratón para hacer clic en un botón.

```py
import tkinter as tk

def revisar_clave(event): # <-- Atrapamos el paquete del evento
    # Leemos lo que hay en la caja
    clave = caja.get()
    print("Revisando contraseña:", clave)

ventana = tk.Tk()
ventana.geometry("300x150")

tk.Label(ventana, text="Escribe y presiona la tecla Enter:").pack(pady=10)

caja = tk.Entry(ventana)
caja.pack()

# "Atamos" la tecla <Return> a nuestra función revisar_clave
caja.bind("<Return>", revisar_clave)

ventana.mainloop()
```


**Ejemplo B: Averiguar DÓNDE hizo clic el usuario**

Aquí es donde el "paquete" event se vuelve súper útil. Si abrimos el paquete, podemos saber las coordenadas (x, y) exactas donde el usuario hizo clic.

````py
import tkinter as tk

def atrapar_clic(event):
    # event.x y event.y nos dicen las coordenadas exactas del clic
    mensaje = f"¡Hiciste clic en la posición X: {event.x}, Y: {event.y}!"
    print(mensaje)
    etiqueta.config(text=mensaje) # Cambiamos el texto del letrero

ventana = tk.Tk()
ventana.geometry("400x300")

# Un letrero grande que funciona como área de clics
etiqueta = tk.Label(ventana, text="Haz clic izquierdo en cualquier parte de este gran recuadro", bg="lightblue")
# Usamos fill y expand para que el letrero ocupe toda la ventana
etiqueta.pack(fill=tk.BOTH, expand=True)

# "Atamos" el clic izquierdo (<Button-1>) a la función
etiqueta.bind("<Button-1>", atrapar_clic)

ventana.mainloop()

````


### 5. El evento `<Key>`: Un Keylogger simple ⌨️

Si usamos el evento general `<Key>`, el paquete `event` nos dirá exactamente qué letra presionó el usuario mirando dentro de `event.char` (el carácter o letra).
````py
import tkinter as tk

def tecla_presionada(event):
    print("Presionaste la tecla:", event.char)

ventana = tk.Tk()
ventana.geometry("200x100")

tk.Label(ventana, text="Escribe cualquier cosa...").pack(pady=20)

# "Atamos" cualquier tecla a la ventana principal entera
ventana.bind("<Key>", tecla_presionada)

ventana.mainloop()
````


🏆 Resumen del Módulo

- Usa .bind(`"<Evento>"`, funcion) cuando necesites reaccionar a algo más que un simple clic de botón -(como movimientos del ratón o teclas presionadas).
- Los eventos van siempre entre símbolos de menor y mayor: `<Return>`, `<Button-1>`, `<Motion>`.
- Tu función siempre debe recibir un parámetro (usualmente llamado `event`) para atrapar la información que envía Tkinter.
- Dentro de tu función, puedes usar `event.x `y `event.y` para saber las coordenadas del ratón, o `event.char` para saber qué letra se tecleó.

---
## Organizando el Caos (Frames y Ventanas)
Hasta ahora, hemos estado poniendo todos nuestros botones y textos directamente sobre nuestra ventana principal (el terreno vacío).

Pero, ¿qué pasa cuando hacemos un programa grande con 20 botones, 5 cajas de texto y 3 listas? Si ponemos todo en la ventana principal, se volverá un desastre total y organizar todo con `grid()` o `pack()` será una pesadilla.

La solución es usar contenedores y ventanas secundarias. ¡Vamos a ordenar la casa!

### 1. El Widget `Frame`: Las cajas invisibles 📦

Un `Frame` (Marco) es un widget muy especial porque no hace nada por sí solo. Es simplemente un contenedor, una caja vacía donde puedes guardar otros widgets.

- **Explicación simple:** Imagina el cajón de tus cubiertos. Tienes un compartimento para cucharas, otro para tenedores y otro para cuchillos. Un Frame es uno de esos compartimentos.
- **El súper poder del Frame:** ¿Recuerdas que en el Módulo 2 dijimos que NO puedes mezclar pack() y grid()? Bueno, con los Frames puedes "hacer trampa". Puedes poner un Frame arriba usando pack(), y dentro de ese Frame usar grid(). ¡Cada Frame tiene su propio espacio independiente!

**Ejemplo Práctico: El panel de botones** Vamos a crear una ventana donde el título está arriba, pero abajo hay un grupo de botones perfectamente ordenados en su propia "caja".

````py
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

# 1. Título principal directamente en la ventana
tk.Label(ventana, text="Panel de Control", font=("Arial", 16)).pack(pady=10)

# 2. Creamos nuestro Frame (la caja invisible) y lo ponemos en la ventana
caja_botones = tk.Frame(ventana)
caja_botones.pack(pady=20)

# 3. Metemos botones DENTRO del Frame (nota que el primer parámetro es 'caja_botones', no 'ventana')
# Usamos grid() dentro de la caja para que estén uno al lado del otro
btn1 = tk.Button(caja_botones, text="Botón 1")
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(caja_botones, text="Botón 2")
btn2.grid(row=0, column=1, padx=5)

ventana.mainloop()
````


### 2. El Widget `LabelFrame`: La caja con etiqueta 🏷️

El `LabelFrame` es exactamente igual que un `Frame` normal, pero viene con un borde visible y un título en la parte superior.

- **Aplicación real:** Es perfecto para agrupar opciones que tienen relación entre sí. Piensa en el menú de "Configuración" de cualquier programa: suele haber un recuadro que dice "Opciones de Pantalla" y otro que dice "Opciones de Sonido".

*Ejemplo Práctico: Agrupando opciones*

````py
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x250")
ventana.config(padx=20, pady=20) # Para dar un margen general

# Creamos el LabelFrame
grupo_opciones = tk.LabelFrame(ventana, text=" Elige tus extras ", padx=10, pady=10)
grupo_opciones.pack(fill="both", expand="yes")

# Ponemos elementos DENTRO del LabelFrame
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

tk.Checkbutton(grupo_opciones, text="Extra Queso", variable=var1).pack(anchor="w")
tk.Checkbutton(grupo_opciones, text="Borde Relleno", variable=var2).pack(anchor="w")
tk.Checkbutton(grupo_opciones, text="Extra Pepperoni", variable=var2).pack(anchor="w")

ventana.mainloop()
````


Si ejecutas este código, verás una línea muy elegante que encierra a las casillas, con el título "Elige tus extras" incrustado en el borde superior.

### 3. El Widget `Toplevel`: Abriendo nuevas ventanas 🚪

Llegará el momento en que una sola ventana no sea suficiente. Querrás un botón que, al ser presionado, abra otra ventana completamente nueva (como cuando haces clic en "Acerca de..." o "Configuración avanzada").

Para hacer ventanas secundarias, NO creamos otro `tk.Tk()`. Solo puede haber un `Tk()` (la ventana raíz) en todo el programa. Para las ventanas hijas usamos `Toplevel`.

- **Explicación simple:** `Tk()` es la puerta principal del edificio. Las `Toplevel` son las puertas de las habitaciones de adentro. Si cierras la habitación (`Toplevel`), el edificio sigue abierto. Si cierras la puerta principal (`Tk()`), se cierra todo.

*Ejemplo Práctico: El botón que abre un pop-up*

```py
import tkinter as tk

def abrir_nueva_ventana():
    # Creamos la ventana secundaria
    ventana_hija = tk.Toplevel(ventana_principal)
    ventana_hija.title("Ventana Secreta")
    ventana_hija.geometry("250x100")
    ventana_hija.config(bg="lightyellow")
    
    # Ponemos cosas en la ventana secundaria
    tk.Label(ventana_hija, text="¡Me encontraste!", bg="lightyellow").pack(pady=10)
    
    # Botón para cerrar SOLO esta ventanita (usamos .destroy)
    tk.Button(ventana_hija, text="Cerrar esto", command=ventana_hija.destroy).pack()

# 1. Ventana Principal
ventana_principal = tk.Tk()
ventana_principal.title("App Principal")
ventana_principal.geometry("300x200")

tk.Label(ventana_principal, text="Esta es la ventana principal").pack(pady=20)

# Botón que llama a la función para abrir la otra ventana
btn_abrir = tk.Button(ventana_principal, text="Abrir Configuración", command=abrir_nueva_ventana)
btn_abrir.pack()

ventana_principal.mainloop()
```

*(Nota importante: Para cerrar una ventana desde el código usamos el comando .destroy() o simplemente .destroy si va directo en el command de un botón).*

**🏆 Resumen del Módulo**

- Usa Frame para agrupar widgets invisibles. Es la mejor forma de organizar tu diseño y evitar que todo quede amontonado. Te permite combinar pack() y grid() de forma segura en diferentes zonas de la pantalla.
- Usa LabelFrame cuando quieras agrupar elementos y dejar claro visualmente de qué tratan, mostrando un recuadrito con título.
- Usa Toplevel para crear pop-ups o ventanas secundarias (como diálogos de confirmación o menús de ajustes). ¡Nunca crees más de un Tk()!

---
## Toques Finales, Alertas y Estética
Hasta ahora hemos construido la estructura de nuestra casa, hemos puesto los muebles (widgets) y organizado todo. Pero, ¿qué pasa si queremos mostrar un mensaje de "¡Guardado con éxito!" o pedirle al usuario que busque una foto en su computadora? ¿Y si queremos que nuestra aplicación no se vea como un programa viejo de los años 90?

En este módulo aprenderemos a usar los diálogos del sistema y a darle un toque más moderno a nuestra aplicación.

### 1. El Módulo `messagebox`: Las ventanas de alerta 🚨

Seguramente has visto esas ventanitas que saltan diciendo "Ocurrió un error" o "¿Estás seguro de que quieres salir?". En lugar de crear nosotros mismos un `Toplevel` y diseñarlo desde cero, Tkinter ya tiene estas ventanas prefabricadas.

- **El secreto:** Estas ventanas viven en un submódulo especial que debes importar por separado.

Tipos de mensajes más comunes:

- Información: `messagebox.showinfo("Título", "Mensaje")`
- Advertencia: `messagebox.showwarning("Título", "Mensaje")`
- Error: `messagebox.showerror("Título", "Mensaje")`
- Pregunta (Sí/No): `messagebox.askyesno("Título", "Mensaje")`

**Ejemplo Práctico: El botón de salir cuidadoso**

```py
import tkinter as tk
from tkinter import messagebox # ¡Paso crucial! Hay que importarlo aparte

def confirmar_salida():
    # askyesno devuelve True (Sí) o False (No)
    respuesta = messagebox.askyesno("Confirmar", "¿De verdad quieres cerrar el programa?")
    
    if respuesta == True:
        ventana.destroy() # Cierra el programa
    else:
        messagebox.showinfo("Genial", "¡Qué bueno que te quedas!")

ventana = tk.Tk()
ventana.geometry("300x150")

tk.Label(ventana, text="Mi Programa Súper Importante").pack(pady=20)
tk.Button(ventana, text="Salir", command=confirmar_salida).pack()

ventana.mainloop()

```


### 2. El Módulo `filedialog`: Explorando el sistema 📂

Si tu programa es un editor de texto, vas a necesitar que el usuario abra un archivo .txt. Para no hacer que el usuario escriba la ruta exacta a mano (como `C:\Usuarios\Juan\Documentos\archivo.txt`), usamos el explorador de archivos nativo de su computadora.

- **Analogía**: Es decirle a tu programa: "Abre el cajón de la computadora del usuario y deja que él mismo me entregue el archivo".

*Ejemplo Práctico: El botón para buscar archivos*

```py
import tkinter as tk
from tkinter import filedialog # También se importa por separado

def buscar_archivo():
    # Esto abre la ventana típica de "Abrir archivo" de Windows/Mac
    # La variable 'ruta' guardará la dirección del archivo que elija el usuario
    ruta = filedialog.askopenfilename(title="Selecciona una imagen o texto")
    
    if ruta: # Si el usuario eligió algo y no le dio a 'Cancelar'
        print("El usuario eligió el archivo que está en:", ruta)
        etiqueta_ruta.config(text=ruta)

ventana = tk.Tk()
ventana.geometry("400x200")

tk.Button(ventana, text="Buscar Archivo...", command=buscar_archivo).pack(pady=20)

# Aquí mostraremos la dirección del archivo que eligió
etiqueta_ruta = tk.Label(ventana, text="Ningún archivo seleccionado")
etiqueta_ruta.pack()

ventana.mainloop()
```


### 3. Introducción a `ttk` (Themed Tkinter): Adiós a los años 90 👔

Quizás hayas notado que los botones y casillas que hemos hecho hasta ahora se ven un poco anticuados, como si fueran de una versión muy vieja de Windows.

Esto se debe a que Tkinter es muy antiguo. Para solucionar esto, los creadores añadieron un paquete llamado `ttk` (Themed Tkinter). Es básicamente una versión actualizada de los widgets clásicos que toma el diseño moderno del sistema operativo que estés usando (sea Windows 10, Windows 11, Mac o Linux).

- **Analogía:** Usar Tkinter normal es salir en pijama. Usar `ttk` es ponerle un traje elegante a tu programa.
- **El cambio es muy fácil:** Solo cambiamos `tk.Button` por `ttk.Button.`

*Ejemplo Práctico: Comparando lo viejo y lo nuevo*
```py
import tkinter as tk
from tkinter import ttk # Importamos la caja de ropa elegante

ventana = tk.Tk()
ventana.geometry("300x200")

tk.Label(ventana, text="Comparación de Botones").pack(pady=10)

# Botón Clásico (Se ve cuadrado y antiguo)
boton_viejo = tk.Button(ventana, text="Botón Clásico (tk)")
boton_viejo.pack(pady=10)

# Botón Moderno (Se ve redondeado, cambia al pasar el ratón)
boton_nuevo = ttk.Button(ventana, text="Botón Moderno (ttk)")
boton_nuevo.pack(pady=10)

# ¡También funciona con otros elementos!
# ttk.Entry(ventana)
# ttk.Label(ventana)
# ttk.Checkbutton(ventana)

ventana.mainloop()
```


*💡 Consejo Pro: A partir de ahora, acostúmbrate a importar siempre ttk y usar sus widgets para que tus aplicaciones se vean profesionales.*

🎉 ¡Felicidades! Has completado el temario

---
## Organizando tu Ventana (Layouts)

En el módulo anterior compramos nuestro "terreno vacío" (la ventana principal). Ahora es el momento de construir y acomodar los muebles (los botones, textos y cuadros de entrada).

Acomodar elementos en Tkinter se llama Gestión de Diseño (Layout Management). Tkinter nos ofrece tres formas diferentes de organizar nuestros elementos: `pack()`, `grid()` y `place()`.

¡Vamos a conocer a los tres organizadores!

🛑 REGLA DE ORO ANTES DE EMPEZAR

Nunca, jamás, mezcles `pack()` y `grid()` en la misma ventana o contenedor. Si lo haces, Tkinter se confundirá tanto tratando de calcular los espacios que tu programa se quedará congelado o se cerrará. ¡Elige solo a un organizador para cada área!

### 1. El método `pack()`: El apilador automático 📚

Imagina que estás guardando libros en una caja. Simplemente los pones uno encima del otro. Así funciona `pack()` (que significa "empacar").

Por defecto, si usas `pack()`, Tkinter pondrá el primer elemento arriba, el siguiente justo debajo, y así sucesivamente, centrándolos en la ventana.

*Personalizando `pack()`:*

- **`side` (Lado):** ¿Hacia dónde quieres empujar el elemento? Puedes usar `tk.TOP` (arriba, por defecto), t`k.BOTTOM` (abajo), `tk.LEFT` (izquierda) o `tk.RIGHT` (derecha).

- **`padx` y `pady` (Espacio exterior):** Es como darle "espacio personal" a tu elemento para que no se pegue con los demás. `padx` da espacio a los lados, `pady` da espacio arriba y abajo.

- **`fill` (Rellenar):** Si quieres que tu botón se estire como una liga de goma para ocupar todo el espacio horizontal, usas f`ill=tk.X`.

*Ejemplo de uso:*
```python
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

# Creamos dos botones (¡Aún no aparecerán hasta usar pack!)
boton1 = tk.Button(ventana, text="Botón Arriba")
boton2 = tk.Button(ventana, text="Botón Abajo")

# Los organizamos
boton1.pack(side=tk.TOP, pady=10) # Se pone arriba, con 10 píxeles de separación vertical
boton2.pack(side=tk.BOTTOM, pady=10) # Se pone hasta abajo

ventana.mainloop()
```


### 2. El método `grid()`: La hoja de cálculo (El favorito) 🏁

Este es el estándar de la industria y el que más vas a usar. Imagina que tu ventana es una hoja de Excel o un tablero de ajedrez gigante. Está dividida en filas (`rows`) y columnas (`columns`).

La primera fila es la `0` y la primera columna es la `0`.

*Personalizando `grid()`:*

- **`row` y `column`:** Le dices exactamente en qué casilla del tablero quieres poner tu elemento.

- **`columnspan` y `rowspan` (Combinar celdas):** Al igual que en Excel, a veces quieres que un título o una caja de texto ocupe dos o tres columnas de ancho. Si le pones `columnspan=2`, ocupará dos casillas.

- **`sticky` (Pegajoso):** Si la casilla del tablero es muy grande pero tu botón es pequeño, se quedará en el centro. Con `sticky` lo "pegas" a los bordes usando puntos cardinales: `N` (Norte/Arriba), `S` (Sur/Abajo), `E` (Este/Derecha), `W` (Oeste/Izquierda). Para que se estire a todos lados, usas `sticky="nsew"`.

*Ejemplo de uso:*

```python
import tkinter as tk

ventana = tk.Tk()

# Creamos etiquetas (textos)
texto_usuario = tk.Label(ventana, text="Usuario:")
texto_clave = tk.Label(ventana, text="Contraseña:")

# Usamos grid como un formulario
texto_usuario.grid(row=0, column=0, padx=10, pady=5) # Fila 0, Columna 0
texto_clave.grid(row=1, column=0, padx=10, pady=5)   # Fila 1, Columna 0

# (Aquí podríamos poner las cajas para escribir en la columna 1)

ventana.mainloop()
```


💡 Nota: grid es perfecto para formularios y calculadoras.

### 3. El método `place()`: El francotirador 🎯

A diferencia de `pack` o `grid` que acomodan las cosas automáticamente, con `place()` tú eres el jefe absoluto. Le dices a Tkinter las coordenadas exactas en píxeles donde quieres que vaya el elemento.

La esquina superior izquierda de tu ventana es la coordenada `x=0`, `y=0`.

*Personalizando `place()`:*

- **x:** Píxeles de distancia desde el borde izquierdo.

- **y:** Píxeles de distancia desde el techo.

*Ejemplo de uso:*

```python
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x300")

boton_secreto = tk.Button(ventana, text="Botón Escondido")
# Lo ponemos exactamente a 150 px de la izquierda y 50 px de arriba
boton_secreto.place(x=150, y=50) 

ventana.mainloop()
```


⚠️ Peligro para principiantes: Rara vez usamos `place()`. ¿Por qué? Porque si el usuario hace la ventana más grande o la abre en una pantalla diferente, tus botones se quedarán estancados en esos píxeles exactos y todo se verá descuadrado.

🏆 Resumen: ¿Cuál elegir?

- Usa `pack()` cuando tu ventana sea muy sencilla y solo quieras apilar cosas una sobre otra o ponerlas en fila.

- Usa `grid()` el 90% de las veces. Es el mejor para crear formularios, aplicaciones reales y diseños estructurados.

- Usa `place()` casi nunca, solo cuando estés haciendo algo muy específico como un juego o un diseño donde necesites precisión milimétrica.

¡En la siguiente empezaremos a crear y usar estos elementos interactivos como Botones, Textos e Imágenes para darles vida con estos gestores de diseño!

---
## Dando Opciones al Usuario (Selección y Estado)
Hasta ahora tu usuario puede leer textos, hacer clics en botones y escribir en cajas. Pero, ¿qué pasa cuando quieres que el usuario elija entre opciones predefinidas?

Imagina que estás creando una aplicación para pedir pizzas. No quieres que el usuario escriba "tamaño grande", porque podría escribir "gande" con un error y tu programa se confundiría. Es mejor darle opciones exactas para que solo tenga que hacer clic.

Vamos a conocer los 5 elementos de selección más importantes en Tkinter.

### 1. El `Checkbutton`: Los ingredientes extra (Selección Múltiple) 🍕

Un `Checkbutton` es una pequeña casilla cuadrada. El usuario puede marcarla (ponerle una palomita/check) o desmarcarla.

- **Regla de oro:** Se usan cuando puedes elegir varias cosas al mismo tiempo (o ninguna).
- **Analogía:** Los ingredientes extra de una pizza. Puedes pedir extra queso, pepperoni y champiñones al mismo tiempo; o puedes no pedir ninguno.
- **El secreto:** Trabajan de la mano con una BooleanVar (Verdadero = Marcado, Falso = Desmarcado).

*Ejemplo de uso:*

```python
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x150")

# La variable que recordará si la casilla está marcada o no
var_queso = tk.BooleanVar()

# Creamos la casilla y la conectamos a la variable
casilla = tk.Checkbutton(ventana, text="Extra Queso", variable=var_queso)
casilla.pack(pady=20)

def ver_orden():
    if var_queso.get() == True:
        print("¡El cliente quiere extra queso!")
    else:
        print("Pizza normal sin extra queso.")

tk.Button(ventana, text="Confirmar", command=ver_orden).pack()

ventana.mainloop()
```

### 2. El `Radiobutton`: El tamaño de la pizza (Selección Única) 🎯

A diferencia del Checkbutton, los `Radiobutton` son circulitos y son exclusivos. Si seleccionas uno, los demás se deseleccionan automáticamente.

- **Regla de oro:** Se usan cuando el usuario solo puede elegir UNA opción de un grupo.
- **Analogía:** El tamaño de la pizza. No puedes pedir una pizza que sea "Pequeña" y "Grande" al mismo tiempo en la misma masa. O es una, o es la otra.
- **El secreto:** Varios Radiobuttons deben compartir la misma variable (por ejemplo, una `StringVar`).

Ejemplo de uso:

```python
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

tk.Label(ventana, text="Elige el tamaño:").pack()

# Una sola variable para todo el grupo
var_tamano = tk.StringVar()
var_tamano.set("Mediana") # Valor por defecto

# Todos los botones usan la misma 'variable', pero cada uno tiene un 'value' diferente
tk.Radiobutton(ventana, text="Pequeña", variable=var_tamano, value="Pequeña").pack()
tk.Radiobutton(ventana, text="Mediana", variable=var_tamano, value="Mediana").pack()
tk.Radiobutton(ventana, text="Grande", variable=var_tamano, value="Grande").pack()

def mostrar_tamano():
    print("Preparando una pizza tamaño:", var_tamano.get())

tk.Button(ventana, text="Pedir", command=mostrar_tamano).pack(pady=10)

ventana.mainloop()
```

### 3. El `Combobox`: La lista desplegable (Para ahorrar espacio) 🔽

Si tienes 3 opciones, los Radiobuttons son geniales. Pero, ¿qué pasa si tienes que elegir tu país de nacimiento de una lista de 195 países? Llenar la pantalla con 195 circulitos sería un desastre.

Para eso usamos el `Combobox`. Es una caja que, al hacer clic, despliega una lista hacia abajo.
Ojo: Este elemento no viene en el Tkinter básico, viene en un sub-módulo más moderno llamado `ttk`.

*Ejemplo de uso:*
```python
import tkinter as tk
from tkinter import ttk # Importamos el módulo moderno

ventana = tk.Tk()

tk.Label(ventana, text="Método de pago:").pack(pady=10)

# Creamos la caja desplegable
caja_opciones = ttk.Combobox(ventana, values=["Efectivo", "Tarjeta de Crédito", "PayPal"])
caja_opciones.pack()

# Para que el usuario no escriba cosas inventadas y solo elija de la lista
caja_opciones.state(["readonly"])

ventana.mainloop()
```


### 4. El `Listbox`: La lista a la vista 📋

Es parecido al Combobox, pero la lista siempre está visible en la pantalla como un pequeño recuadro. El usuario puede hacer clic en un elemento para sombrearlo y seleccionarlo.

- **Analogía:** Una lista del supermercado donde subrayas lo que necesitas.

*Ejemplo de uso:*

```python
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Frutas disponibles:").pack()

# Creamos la lista visual
lista = tk.Listbox(ventana)
lista.pack(pady=10)

# Le agregamos elementos usando .insert()
# El END significa "ponlo al final de lo que ya haya"
lista.insert(tk.END, "Manzana")
lista.insert(tk.END, "Banana")
lista.insert(tk.END, "Fresa")
lista.insert(tk.END, "Naranja")

ventana.mainloop()
```


### 5. El `Scale`: El deslizador numérico 🎚️
A veces no queremos que el usuario elija de una lista, sino que escoja un número dentro de un rango deslizando un control.
- Analogía: El control de volumen del estéreo o el brillo de tu pantalla.
- El secreto: Le decimos desde dónde empieza (from_) y dónde termina (to). (Nota que 'from' lleva un guión bajo al final en Python).

*Ejemplo de uso:*

```py
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x150")

tk.Label(ventana, text="Volumen:").pack()

# Creamos el deslizador. Orient=HORIZONTAL lo acuesta (por defecto es vertical)
deslizador = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL)
deslizador.pack(pady=10)

def checar_volumen():
    # .get() nos devuelve el número en el que se quedó el deslizador
    print("El volumen está en:", deslizador.get())

tk.Button(ventana, text="Ver Volumen", command=checar_volumen).pack()

ventana.mainloop()
```


*🏆 Resumen del Módulo*

- Checkbutton (Casilla): Para opciones de Sí o No, donde puedes seleccionar varias a la vez. Usa BooleanVar().
- Radiobutton (Circulito): Para opciones únicas y exclusivas. Todos deben compartir la misma variable.
- Combobox (Desplegable): Para listas largas que no caben en la pantalla. (Recuerda importar ttk).
- Listbox (Lista visible): Para listas de tamaño mediano que quieres que siempre estén a la vista.
- Scale (Deslizador): Para elegir un número rápidamente arrastrando una barrita.
