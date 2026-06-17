import tkinter as tk
import numpy as np
from tkinter import ttk, messagebox


def ventana_grupo_2(root):
    def validar_entradas():
        try:
            float(entry_xs.get())
            float(entry_ys.get())
            float(entry_xc.get())
            float(entry_yc.get())
            float(entry_dist.get())
            float(entry_ang.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos en todos los campos.")
            return
        messagebox.showinfo("Datos guardados", "Los datos de entrada se han ingresado correctamente.")

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

    def calcular_deltas():
        try:
            xs = float(entry_xs.get())
            ys = float(entry_ys.get())
            xc = float(entry_xc.get())
            yc = float(entry_yc.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos antes de calcular.")
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

        # lectura del ángulo horizontal (entrada)
        try:
            ang_h = float(entry_ang.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un ángulo horizontal válido.")
            return

        try:
            dist = float(entry_dist.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese una distancia horizontal válida.")
            return

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

        lbl_dx.config(text=f"ΔX: {abs(dx):.3f} {direccion_x}")
        lbl_dy.config(text=f"ΔY: {abs(dy):.3f} {direccion_y}")
        lbl_rumbo.config(text=f"Rumbo (°): {rumbo:.3f}")
        lbl_azimut.config(text=f"Azimut (°): {azimut:.3f}")
        lbl_nf.config(text=f"Nf: {nf:.3f}")
        lbl_ef.config(text=f"Ef: {ef:.3f}")
        messagebox.showinfo(
            "Resultados",
            f"ΔX = {abs(dx):.3f} {direccion_x}\n"
            f"ΔY = {abs(dy):.3f} {direccion_y}\n"
            f"Rumbo = {rumbo:.3f}°\n"
            f"Azimut = {azimut:.3f}°\n"
            f"Nf = {nf:.3f}\n"
            f"Ef = {ef:.3f}"
        )

    def validar_y_calcular():
        try:
            float(entry_xs.get())
            float(entry_ys.get())
            float(entry_xc.get())
            float(entry_yc.get())
            float(entry_dist.get())
            float(entry_ang.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos en todos los campos.")
            return
        calcular_deltas()

    boton_validar = ttk.Button(frame, text="Confirmar datos", command=validar_y_calcular)
    boton_validar.grid(row=10, column=0, columnspan=2, pady=(20,10), sticky="ew")

    boton_calcular = ttk.Button(frame, text="Calcular deltas", command=calcular_deltas)
    boton_calcular.grid(row=11, column=0, columnspan=2, pady=(0,10), sticky="ew")

    boton_volver = ttk.Button(frame, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.grid(row=12, column=0, columnspan=2, pady=(0,8), sticky="ew")

    # Etiquetas de resultado
    lbl_dx = ttk.Label(frame, text="ΔX: ")
    lbl_dx.grid(row=13, column=0, sticky="w", pady=4)
    lbl_dy = ttk.Label(frame, text="ΔY: ")
    lbl_dy.grid(row=13, column=1, sticky="w", pady=4)
    lbl_rumbo = ttk.Label(frame, text="Rumbo (°): ")
    lbl_rumbo.grid(row=14, column=0, columnspan=2, sticky="w", pady=4)
    lbl_azimut = ttk.Label(frame, text="Azimut (°): ")
    lbl_azimut.grid(row=15, column=0, columnspan=2, sticky="w", pady=4)
    lbl_nf = ttk.Label(frame, text="Nf: ")
    lbl_nf.grid(row=16, column=0, columnspan=2, sticky="w", pady=4)
    lbl_ef = ttk.Label(frame, text="Ef: ")
    lbl_ef.grid(row=17, column=0, columnspan=2, sticky="w", pady=4)
    frame.columnconfigure(1, weight=1)
