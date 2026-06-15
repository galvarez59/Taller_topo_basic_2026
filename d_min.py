import tkinter as tk
from tkinter import messagebox
import math

# Función para calcular la distancia mínima de un punto a una recta
def calcular_distancia():
    try:
        # Coordenadas de los puntos de la recta
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())

        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())

        # Coordenadas del punto
        xp = float(entry_xp.get())
        yp = float(entry_yp.get())

        # Fórmula de distancia punto-recta
        numerador = abs((y2 - y1) * xp - (x2 - x1) * yp + x2 * y1 - y2 * x1)
        denominador = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

        if denominador == 0:
            messagebox.showerror("Error", "Los puntos de la recta no pueden ser iguales.")
            return

        distancia = numerador / denominador

        # Mostrar resultado en rojo
        resultado_label.config(
            text=f"Distancia mínima: {distancia:.3f} metros",
            fg="red"
        )

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")


# Ventana principal
ventana = tk.Tk()
ventana.title("Distancia mínima de un punto a una recta")
ventana.geometry("500x450")
ventana.resizable(False, False)

# Título
titulo = tk.Label(
    ventana,
    text="Cálculo de Distancia Punto-Recta",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Frame principal
frame = tk.Frame(ventana)
frame.pack(pady=10)

# =========================
# PUNTO 1 DE LA RECTA
# =========================
tk.Label(frame, text="Punto 1 de la Recta", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(frame, text="Este X1 (m):").grid(row=1, column=0, sticky="e")
entry_x1 = tk.Entry(frame)
entry_x1.grid(row=1, column=1)

tk.Label(frame, text="Norte Y1 (m):").grid(row=2, column=0, sticky="e")
entry_y1 = tk.Entry(frame)
entry_y1.grid(row=2, column=1)

# =========================
# PUNTO 2 DE LA RECTA
# =========================
tk.Label(frame, text="Punto 2 de la Recta", font=("Arial", 11, "bold")).grid(row=3, column=0, columnspan=2, pady=5)

tk.Label(frame, text="Este X2 (m):").grid(row=4, column=0, sticky="e")
entry_x2 = tk.Entry(frame)
entry_x2.grid(row=4, column=1)

tk.Label(frame, text="Norte Y2 (m):").grid(row=5, column=0, sticky="e")
entry_y2 = tk.Entry(frame)
entry_y2.grid(row=5, column=1)

# =========================
# PUNTO EXTERNO
# =========================
tk.Label(frame, text="Punto Externo", font=("Arial", 11, "bold")).grid(row=6, column=0, columnspan=2, pady=5)

tk.Label(frame, text="Este Xp (m):").grid(row=7, column=0, sticky="e")
entry_xp = tk.Entry(frame)
entry_xp.grid(row=7, column=1)

tk.Label(frame, text="Norte Yp (m):").grid(row=8, column=0, sticky="e")
entry_yp = tk.Entry(frame)
entry_yp.grid(row=8, column=1)

# Botón calcular
btn_calcular = tk.Button(
    ventana,
    text="Calcular Distancia",
    command=calcular_distancia,
    bg="lightblue",
    font=("Arial", 11, "bold")
)
btn_calcular.pack(pady=15)

# Resultado
resultado_label = tk.Label(
    ventana,
    text="",
    font=("Arial", 14, "bold")
)
resultado_label.pack(pady=20)

# Ejecutar ventana
ventana.mainloop()