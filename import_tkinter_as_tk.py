import tkinter as tk
from tkinter import ttk, messagebox
import math 

# ==================================================
# ===   SUBRUTINA MAIN                           ===
# ==================================================
def ventana_main():
    win = tk.Toplevel(root)
    win.title("Ventana main")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: main",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí main debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ MAIN DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de main")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA AYLEEN                         ===
# ==================================================
def ventana_ayleen():
    win = tk.Toplevel(root)
    win.title("Ventana ayleen")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: ayleen",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí ayleen debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ AYLEEN DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de ayleen")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA HARLEY                         ===
# ==================================================
def ventana_Harley():
    win = tk.Toplevel(root)
    win.title("Ventana Harley")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Harley",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Harley debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ HARLEY DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Harley")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA IGNACIO                        ===
# ==================================================
def ventana_Ignacio():
    win = tk.Toplevel(root)
    win.title("Ventana Ignacio")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Ignacio",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Ignacio debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ IGNACIO DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Ignacio")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA RAFAEL                         ===
# ==================================================
def ventana_Rafael():
    win = tk.Toplevel(root)
    win.title("Distancia mínima punto-recta")
    win.geometry("550x500")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Rafael",
        font=("Segoe UI", 18, "bold")
    )
    titulo.pack(pady=10)

    frame = tk.Frame(win, bg="#ecf0f1")
    frame.pack(pady=10)

    # Punto 1
    tk.Label(frame, text="Punto 1 de la Recta", bg="#ecf0f1",
             font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)

    tk.Label(frame, text="Este X1 (m):", bg="#ecf0f1").grid(row=1, column=0)
    entry_x1 = tk.Entry(frame)
    entry_x1.grid(row=1, column=1)

    tk.Label(frame, text="Norte Y1 (m):", bg="#ecf0f1").grid(row=2, column=0)
    entry_y1 = tk.Entry(frame)
    entry_y1.grid(row=2, column=1)

    # Punto 2
    tk.Label(frame, text="Punto 2 de la Recta", bg="#ecf0f1",
             font=("Arial", 10, "bold")).grid(row=3, column=0, columnspan=2, pady=5)

    tk.Label(frame, text="Este X2 (m):", bg="#ecf0f1").grid(row=4, column=0)
    entry_x2 = tk.Entry(frame)
    entry_x2.grid(row=4, column=1)

    tk.Label(frame, text="Norte Y2 (m):", bg="#ecf0f1").grid(row=5, column=0)
    entry_y2 = tk.Entry(frame)
    entry_y2.grid(row=5, column=1)

    # Punto externo
    tk.Label(frame, text="Punto Externo", bg="#ecf0f1",
             font=("Arial", 10, "bold")).grid(row=6, column=0, columnspan=2, pady=5)

    tk.Label(frame, text="Este Xp (m):", bg="#ecf0f1").grid(row=7, column=0)
    entry_xp = tk.Entry(frame)
    entry_xp.grid(row=7, column=1)

    tk.Label(frame, text="Norte Yp (m):", bg="#ecf0f1").grid(row=8, column=0)
    entry_yp = tk.Entry(frame)
    entry_yp.grid(row=8, column=1)

    resultado = tk.Label(
        win,
        text="",
        fg="red",
        bg="#ecf0f1",
        font=("Arial", 12, "bold")
    )
    resultado.pack(pady=15)

    def calcular():

        try:
            x1 = float(entry_x1.get())
            y1 = float(entry_y1.get())

            x2 = float(entry_x2.get())
            y2 = float(entry_y2.get())

            xp = float(entry_xp.get())
            yp = float(entry_yp.get())

            numerador = abs(
                (y2 - y1) * xp
                - (x2 - x1) * yp
                + x2 * y1
                - y2 * x1
            )

            denominador = math.sqrt(
                (y2 - y1) ** 2 +
                (x2 - x1) ** 2
            )

            if denominador == 0:
                messagebox.showerror(
                    "Error",
                    "Los puntos de la recta no pueden ser iguales."
                )
                return

            distancia = numerador / denominador

            resultado.config(
                text=f"Distancia mínima: {distancia:.3f} metros"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese valores numéricos válidos."
            )

    ttk.Button(
        win,
        text="Calcular",
        command=calcular
    ).pack(pady=10)

    ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=win.destroy
    ).pack(pady=10)

# ==================================================
# ===   SUBRUTINA WILSON                         ===
# ==================================================
def ventana_Wilson():
    win = tk.Toplevel(root)
    win.title("Ventana Wilson")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Wilson",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Wilson debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ WILSON DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Wilson")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA ANDRES                         ===
# ==================================================
def ventana_Andres():
    win = tk.Toplevel(root)
    win.title("Ventana Andres")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Andres",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Andres debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ ANDRES DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Andres")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA PANTOJA                        ===
# ==================================================
def ventana_pantoja():
    win = tk.Toplevel(root)
    win.title("Ventana pantoja")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: pantoja",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí pantoja debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ PANTOJA DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de pantoja")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================
# ===   VENTANA PRINCIPAL MENÚ    ===
# ==================================
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x650")
root.configure(bg="#ecf0f1")

banner = ttk.Label(
    root,
    text="Filtrado de Nube de Puntos",
    anchor="center",
    font=("Segoe UI", 20, "bold"),
    background="#0984e3",
    foreground="white"
)
banner.pack(fill="x", pady=(0, 20))

instruccion = ttk.Label(
    root,
    text="Seleccione una opción del menú",
    font=("Segoe UI", 12),
    background="#ecf0f1"
)
instruccion.pack(pady=(10, 30))

# Botones del menú principal
b1 = ttk.Button(root, text="main", command=ventana_main)
b1.pack(pady=10, ipadx=20, ipady=5)

b2 = ttk.Button(root, text="ayleen", command=ventana_ayleen)
b2.pack(pady=10, ipadx=20, ipady=5)

b3 = ttk.Button(root, text="Harley", command=ventana_Harley)
b3.pack(pady=10, ipadx=20, ipady=5)

b4 = ttk.Button(root, text="Ignacio", command=ventana_Ignacio)
b4.pack(pady=10, ipadx=20, ipady=5)

b5 = ttk.Button(root, text="Rafael", command=ventana_Rafael)
b5.pack(pady=10, ipadx=20, ipady=5)

b6 = ttk.Button(root, text="Wilson", command=ventana_Wilson)
b6.pack(pady=10, ipadx=20, ipady=5)

b7 = ttk.Button(root, text="Andres", command=ventana_Andres)
b7.pack(pady=10, ipadx=20, ipady=5)

b8 = ttk.Button(root, text="pantoja", command=ventana_pantoja)
b8.pack(pady=10, ipadx=20, ipady=5)

root.mainloop()