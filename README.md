
# Calculadora 

Es una **calculadora de consola**. Eso significa que no tiene botones ni imágenes, sino que funciona escribiendo comandos desde una ventana negra (la terminal). Lo que se puede hacer con esta calculadora es lo siguiente:

- Sumar, restar, multiplicar y dividir.
- Calcular raíces cuadradas, porcentajes, factoriales, etc.
- Escribir expresiones matemáticas completas, como `2 + 3 * (5 - 1)`.
- Guardar un historial de las operaciones realizadas en un archivo.
- Revisar si el código funciona automáticamente con pruebas.

---

## Estructura del proyecto

Se crea **varios archivos separados**, como se hace en cualquier proyecto real. Esto ayuda a mantener el código ordenado y fácil de entender.

```
calculator/
├── main.py               ← El corazón del programa: muestra el menú y recibe órdenes
├── operations.py         ← Acá están las funciones matemáticas (sumar, dividir, etc.)
├── utils.py              ← Funciones de apoyo: mostrar menú, limpiar pantalla, etc.
├── test_operations.py    ← Un archivo que prueba si las funciones matemáticas funcionan
├── history.json          ← Archivo donde se guarda el historial de cálculos
└── README.md             ← Este documento que estás leyendo
```

---

## Herramientas usadas

### Bibliotecas (librerías de código ya hecho que podemos usar)

#### `math`
Nos da funciones matemáticas como raíz cuadrada (`sqrt`) o factorial.

#### `json`
Nos permite guardar datos en un archivo como texto (por ejemplo, el historial).

#### `colorama`
Sirve para mostrar texto de colores en la consola (verde para resultados, rojo para errores).
> No viene con Python, así que se tiene que instalar:
```bash
pip install colorama
```

---

## Explicación archivo por archivo

### 1. `main.py` — El programa principal

Aquí se muestra el menú principal, se pregunta al usuario qué quiere hacer, y se encarga de ejecutar la función correcta.

#### ¿Qué se importa?
```python
from utils import show_menu, get_number, save_history, load_history, clear_screen
from operations import *
from colorama import Fore, Style, init
import math
```

- `from utils import...`: se importa funciones que muestran el menú, piden datos, etc.
- `from operations import *`: se importa TODAS las funciones matemáticas.
- `colorama`: esto es para que el texto tenga color (verde = OK, rojo = error).
- `math`: esto es necesario para que podamos usar funciones matemáticas seguras en expresiones como `2 + sqrt(4)`.

#### ¿Qué hace el código?
- Usa un **bucle infinito** (`while True:`) para que la calculadora siga funcionando hasta que el usuario decida salir.
- Muestra un menú:
  ```
  1. Basic Operations
  2. Advanced Operations
  3. Evaluate Expression
  4. View History
  5. Exit
  ```
- Según la opción que se elija, se llama a una función: por ejemplo `basic_operations_menu()` o `evaluate_expression()`.
- Después de cada operación, te pide que presiones Enter para continuar.

---

### 2. `operations.py` — Las funciones matemáticas

Este archivo contiene una función por cada operación. Por ejemplo:

```python
def add(a, b): return a + b
def divide(a, b): return "Error: Division by zero" if b == 0 else a / b
```

- Cada función recibe uno o dos números (a, b).
- Devuelven el resultado.
- Algunas validan errores, como dividir por cero o hacer la raíz de un número negativo.

Incluye funciones como:

- `power(a, b)` → potencia
- `square_root(a)` → raíz cuadrada
- `modulo(a, b)` → resto de una división
- `percentage(total, percent)` → porcentaje

---

### 3. `utils.py` — Funciones auxiliares

Estas funciones no hacen cálculos, pero ayudan a que el programa sea más cómodo y útil.

```python
def show_menu(): ...
def get_number(prompt): ...
def save_history(entry): ...
def load_history(): ...
def clear_screen(): ...
```

- `show_menu()` → imprime el menú
- `get_number("...")` → pide al usuario que escriba un número (y valida que sea válido)
- `save_history()` y `load_history()` → guardan/leen datos del archivo `history.json`
- `clear_screen()` → borra la pantalla como lo hacen los programas reales

---

### 4. `test_operations.py` — Pruebas automáticas

Es un archivo especial que se usa para asegurar de que las funciones estén bien.

```python
import unittest
from operations import *

class TestCalculator(unittest.TestCase):
    def test_add(self): ...
    def test_divide_zero(self): ...
    ...
```

Usa `unittest`, una herramienta que ya viene con Python. Cada `test_...` es una función que prueba algo.

Para ejecutarlas:
```bash
python3 test_operations.py
```

Si todo está bien, te dirá que los tests pasaron. Si hay errores, te lo mostrará también.

---

## ¿Cómo funciona todo junto?

1. Se ejecuta el archivo principal:
   ```bash
   python3 main.py
   ```

2. Se abre el menú:
   ```
   === CALCULATOR ===
   1. Basic Operations
   2. Advanced Operations
   3. Evaluate Expression
   4. View History
   5. Exit
   ```

3. Hay que eligir una opción (por ejemplo `2` para operaciones avanzadas).

4. El programa te guía paso a paso: te pide datos, hace el cálculo, muestra el resultado y lo guarda.

5. Se puede salir en cualquier momento, para eso hay que elegir la opción 5. Al hacerlo el programa terminará en el acto.

---

## 🔄 ¿Cómo podés mejorarlo?

Para mejorarlo se podría hacer lo siguiente por ejemplo:

- Agregar una **interfaz gráfica** con `tkinter`
- Guardar el historial con fechas y horas
- Hacer que funcione desde una app web con `Flask`
- Agregar más funciones científicas: seno, coseno, logaritmo…

---

