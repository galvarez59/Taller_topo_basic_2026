import tkinter as tk
from tkinter import ttk
import replanteo_coordenadas_topo

# ============================
# ===   VENTANA GRUPO 1    ===
# ============================
def ventana_grupo_1():
    win = tk.Toplevel(root)
    win.title("Poligono 1")
    win.geometry("400x350")
    replanteo_coordenadas_topo.construir_interfaz(win)
    # --- Botón para volver al menú principal ---

    
    # -------------- INSTRUCCIONES GRUPO 1 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------

# ===================================
# ===   VENTANA GRUPO 2 Ejemplo   ===
# ===================================
def ventana_grupo_2():
    # --- IMPORTA AQUI LAS LIBRERIAS QUE NECESITES ---
    import tkinter as tk
    from tkinter import messagebox

    # --- AQUI VA TU LOGICA, FUNCIONES Y CLASES ---
    # Por ejemplo:
    def ejemplo_funcion():
        messagebox.showinfo("Ejemplo", "Esto es un ejemplo para el Poly_2.")

    # --- CREA UNA NUEVA VENTANA PARA TU GRUPO ---
    win = tk.Toplevel(root)
    win.title("Poligono 2")
    win.geometry("400x300")

    # --- Botón para volver al menú principal ---
    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)
    
    
    # -------------- INSTRUCCIONES GRUPO 3 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------

# ============================
# ===   VENTANA GRUPO 3    ===
# ============================
def ventana_grupo_3():
    win = tk.Toplevel(root)
    win.title("Poligono 3")
    win.geometry("400x250")
    label = ttk.Label(win, text="Poly 3\nAgrega aquí tu código de filtrado", font=("Segoe UI", 14))
    label.pack(pady=50)
    
    # --- Botón para volver al menú principal ---
    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)
    # -------------- INSTRUCCIONES GRUPO 3 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------


# ============================
# ===   VENTANA GRUPO 4    ===
# ============================
def Intercepcion_de_coordenadas():
    win = tk.Toplevel(root)
    win.title("Intersección de dos rectas")
    win.geometry("500x550")

    ttk.Label(win, text="Recta 1").pack(pady=5)

    ttk.Label(win, text="X1").pack()
    x1_entry = ttk.Entry(win)
    x1_entry.pack()

    ttk.Label(win, text="Y1").pack()
    y1_entry = ttk.Entry(win)
    y1_entry.pack()

    ttk.Label(win, text="X2").pack()
    x2_entry = ttk.Entry(win)
    x2_entry.pack()

    ttk.Label(win, text="Y2").pack()
    y2_entry = ttk.Entry(win)
    y2_entry.pack()

    ttk.Label(win, text="Recta 2").pack(pady=5)

    ttk.Label(win, text="X3").pack()
    x3_entry = ttk.Entry(win)
    x3_entry.pack()

    ttk.Label(win, text="Y3").pack()
    y3_entry = ttk.Entry(win)
    y3_entry.pack()

    ttk.Label(win, text="X4").pack()
    x4_entry = ttk.Entry(win)
    x4_entry.pack()

    ttk.Label(win, text="Y4").pack()
    y4_entry = ttk.Entry(win)
    y4_entry.pack()

    resultado = ttk.Label(win, text="", font=("Segoe UI", 10))
    resultado.pack(pady=10)

    def calcular():
        try:
            x1 = float(x1_entry.get())
            y1 = float(y1_entry.get())
            x2 = float(x2_entry.get())
            y2 = float(y2_entry.get())

            x3 = float(x3_entry.get())
            y3 = float(y3_entry.get())
            x4 = float(x4_entry.get())
            y4 = float(y4_entry.get())

            denominador = ((x1 - x2) * (y3 - y4)
                           - (y1 - y2) * (x3 - x4))

            if denominador == 0:
                resultado.config(
                    text="Las rectas son paralelas.\nNo existe intersección."
                )
                return

            px = (
                ((x1*y2 - y1*x2) * (x3 - x4)
                 - (x1 - x2) * (x3*y4 - y3*x4))
                / denominador
            )

            py = (
                ((x1*y2 - y1*x2) * (y3 - y4)
                 - (y1 - y2) * (x3*y4 - y3*x4))
                / denominador
            )

            resultado.config(
                text=f"Punto de intersección:\nX = {px:.3f}\nY = {py:.3f}"
            )

        except ValueError:
            resultado.config(
                text="Ingrese valores numéricos válidos."
            )

    ttk.Button(
        win,
        text="Calcular Intersección",
        command=calcular
    ).pack(pady=10)

    ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=win.destroy
    ).pack(pady=10)

# ============ VENTANA PRINCIPAL =============
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x500")
root.configure(bg="#ecf0f1")

banner = ttk.Label(root, text="Filtrado de Nube de Puntos", anchor="center",font=("Segoe UI", 20, "bold"), background="#0984e3", foreground="white")
banner.pack(fill="x", pady=(0, 20))

# 69 text= "esto es editable"
instruccion = ttk.Label(root, text="Seleccione un Poligono", font=("Segoe UI", 12), background="#ecf0f1")
instruccion.pack(pady=(10,30))

# Botones de cada grupo, Luego del bg= hay un cuadrado con color al apretarlo configuran el color del boton
b1 = ttk.Button(root, text="Poligono 1", style="B1.TButton", command=ventana_grupo_1)
b1.pack(pady=15)

b2 = ttk.Button(root, text="Poligono 2", style="B2.TButton", command=ventana_grupo_2)
b2.pack(pady=15)

b3 = ttk.Button(root, text="Poligono 3", style="B3.TButton", command=ventana_grupo_3)
b3.pack(pady=15)

b4 = ttk.Button(root, text="Intercepcion de coordenadas", style="B3.TButton", command=Intercepcion_de_coordenadas)
b4.pack(pady=15)

root.mainloop()
