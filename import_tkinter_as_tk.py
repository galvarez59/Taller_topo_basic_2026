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
    win.title("Intercepcion de coordenadas")
    win.geometry("400x200")

    label = ttk.Label(
        win,
        text="Intercepcion de coordenadas\nAgrega aquí tu código",
        font=("Segoe UI", 14)
    )
    label.pack(pady=50)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=win.destroy
    )
    boton_volver.pack(pady=10)


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