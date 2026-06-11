import tkinter as tk
from tkinter import ttk, messagebox

# ============================================
# ===   FUNCIÓN GENERAL PARA CADA VENTANA   ===
# ============================================
def abrir_ventana(nombre):
    """
    Esta función crea una nueva ventana para cada opción del menú.
    Recibe como parámetro el nombre de la opción seleccionada.
    """

    win = tk.Toplevel(root)
    win.title(f"Ventana {nombre}")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    # Título de la ventana secundaria
    titulo = ttk.Label(
        win,
        text=f"Subrutina: {nombre}",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    # Texto explicativo
    etiqueta = ttk.Label(
        win,
        text=f"Aquí se puede agregar el código de cálculo de {nombre}",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    # ----------------------------------------
    # ===   FUNCIÓN DEL BOTÓN CALCULAR      ===
    # ----------------------------------------
    def calcular():
        """
        Aquí debe ir la lógica de cálculo de cada estudiante o grupo.
        Por ahora muestra un mensaje de ejemplo.
        """
        messagebox.showinfo(
            "Calcular",
            f"Se ejecutó la subrutina de cálculo para: {nombre}"
        )

    # Botón Calcular
    boton_calcular = ttk.Button(
        win,
        text="Calcular",
        command=calcular
    )
    boton_calcular.pack(pady=15)

    # Botón Volver al Menú Principal
    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=win.destroy
    )
    boton_volver.pack(pady=10)


# ==================================
# ===   VENTANA PRINCIPAL MENÚ    ===
# ==================================
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x650")
root.configure(bg="#ecf0f1")

# Banner superior
banner = ttk.Label(
    root,
    text="Filtrado de Nube de Puntos",
    anchor="center",
    font=("Segoe UI", 20, "bold"),
    background="#0984e3",
    foreground="white"
)
banner.pack(fill="x", pady=(0, 20))

# Instrucción
instruccion = ttk.Label(
    root,
    text="Seleccione una opción del menú",
    font=("Segoe UI", 12),
    background="#ecf0f1"
)
instruccion.pack(pady=(10, 30))

# Lista de opciones del menú
opciones = [
    "main",
    "ayleen",
    "Harley",
    "Ignacio",
    "Rafael",
    "Wilson",
    "Andres",
    "pantoja"
]

# Creación automática de los 8 botones
for nombre in opciones:
    boton = ttk.Button(
        root,
        text=nombre,
        command=lambda n=nombre: abrir_ventana(n)
    )
    boton.pack(pady=10, ipadx=20, ipady=5)

# Ejecutar aplicación
root.mainloop()