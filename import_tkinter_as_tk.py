import tkinter as tk
import numpy as np
from tkinter import ttk, messagebox

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
def ventana_Harley(root):
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
        text="Cálculo de coordenadas (Sexagesimal)",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def abrir_formulario():
        win.destroy()
        calcular(root)

    boton_calcular = ttk.Button(win, text="Calcular", command=abrir_formulario)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


def calcular(root):
    win = tk.Toplevel(root)
    win.title("Polígono 2 - Entrada de Datos")
    win.geometry("480x460")
    win.configure(bg="#f7f7f7")

    frame = ttk.Frame(win, padding=16)
    frame.pack(fill="both", expand=True)

    titulo = ttk.Label(frame, text="Calculo de coordenadas (Sexagesimal)", font=("Segoe UI", 16, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=(0, 12))

    ttk.Label(frame, text="Coordenadas Estación", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, columnspan=2, sticky="w", pady=(10,4))
    ttk.Label(frame, text="X (Norte):").grid(row=2, column=0, sticky="e", pady=4, padx=(0,8))
    entry_xs = ttk.Entry(frame)
    entry_xs.grid(row=2, column=1, sticky="ew", pady=4)
    ttk.Label(frame, text="Y (Este):").grid(row=3, column=0, sticky="e", pady=4, padx=(0,8))
    entry_ys = ttk.Entry(frame)
    entry_ys.grid(row=3, column=1, sticky="ew", pady=4)

    ttk.Label(frame, text="Coordenadas Calaje", font=("Segoe UI", 12, "bold")).grid(row=4, column=0, columnspan=2, sticky="w", pady=(15,4))
    ttk.Label(frame, text="X (Norte):").grid(row=5, column=0, sticky="e", pady=4, padx=(0,8))
    entry_xc = ttk.Entry(frame)
    entry_xc.grid(row=5, column=1, sticky="ew", pady=4)
    ttk.Label(frame, text="Y (Este):").grid(row=6, column=0, sticky="e", pady=4, padx=(0,8))
    entry_yc = ttk.Entry(frame)
    entry_yc.grid(row=6, column=1, sticky="ew", pady=4)

    ttk.Label(frame, text="Datos del punto", font=("Segoe UI", 12, "bold")).grid(row=7, column=0, columnspan=2, sticky="w", pady=(15,4))
    ttk.Label(frame, text="Distancia horizontal (m):").grid(row=8, column=0, sticky="e", pady=4, padx=(0,8))
    entry_dist = ttk.Entry(frame)
    entry_dist.grid(row=8, column=1, sticky="ew", pady=4)
    ttk.Label(frame, text="Ángulo horizontal(°):").grid(row=9, column=0, sticky="e", pady=4, padx=(0,8))
    entry_ang = ttk.Entry(frame)
    entry_ang.grid(row=9, column=1, sticky="ew", pady=4)

    def confirmar_y_calcular():
        try:
            xs = float(entry_xs.get())
            ys = float(entry_ys.get())
            xc = float(entry_xc.get())
            yc = float(entry_yc.get())
            dist = float(entry_dist.get())
            ang_h = float(entry_ang.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos en todos los campos.")
            return

        # Crear arrays de numpy para coordenadas
        coord_estacion = np.array([xs, ys])
        coord_calaje = np.array([xc, yc])
        
        # Calcular deltas usando numpy
        delta_coords = coord_calaje - coord_estacion
        dx = float(delta_coords[0])
        dy = float(delta_coords[1])

        if dx == 0:
            rumbo = 90.0
        else:
            rumbo = float(np.abs(np.degrees(np.arctan(dy / dx))))

        direccion_x = "N" if dx > 0 else "S"
        direccion_y = "E" if dy > 0 else "W"

        if direccion_x == "N" and direccion_y == "E":
            azimut = rumbo
        elif direccion_x == "S" and direccion_y == "E":
            azimut = 180.0 - rumbo
        elif direccion_x == "S" and direccion_y == "W":
            azimut = 180.0 + rumbo
        else:  # N-W
            azimut = 360.0 - rumbo

        if azimut == 360.0:
            azimut = 0.0

        # Azimut punto observado = azimut + ang_h (si >360 restar 360)
        azimut_punto = azimut + ang_h
        if azimut_punto > 360.0:
            azimut_punto -= 360.0
        if azimut_punto == 360.0:
            azimut_punto = 0.0

        # Calcular proyecciones usando numpy
        azimut_punto_rad = np.radians(azimut_punto)
        delta_np = dist * np.cos(azimut_punto_rad)
        delta_ep = dist * np.sin(azimut_punto_rad)

        # Calcular coordenadas finales
        nf = xs + float(delta_np)
        ef = ys + float(delta_ep)

        messagebox.showinfo(
            "Resultados",
            f"ΔX = {abs(dx):.3f} {direccion_x}\n"
            f"ΔY = {abs(dy):.3f} {direccion_y}\n"
            f"Rumbo = {rumbo:.3f}°\n"
            f"Azimut = {azimut:.3f}°\n"
            f"Nf = {nf:.3f}\n"
            f"Ef = {ef:.3f}"
        )
        win.destroy()

    boton_confirmar = ttk.Button(frame, text="Confirmar datos y calcular", command=confirmar_y_calcular)
    boton_confirmar.grid(row=10, column=0, columnspan=2, pady=(20,10), sticky="ew")

    boton_cancelar = ttk.Button(frame, text="Cancelar", command=win.destroy)
    boton_cancelar.grid(row=11, column=0, columnspan=2, pady=(0,8), sticky="ew")

    frame.columnconfigure(1, weight=1)


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
    win.title("Ventana Rafael")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Rafael",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Rafael debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ RAFAEL DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Rafael")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


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

b3 = ttk.Button(root, text="Harley", command=lambda: ventana_Harley(root))
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