import tkinter as tk
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

    titulo = ttk.Label(frame, text="Entrada de datos - Punto 2", font=("Segoe UI", 16, "bold"))
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
    ttk.Label(frame, text="Distancia-Estación (m):").grid(row=8, column=0, sticky="e", pady=4, padx=(0,8))
    entry_dist = ttk.Entry(frame)
    entry_dist.grid(row=8, column=1, sticky="ew", pady=4)
    ttk.Label(frame, text="Ángulo Calaje–Estación(°):").grid(row=9, column=0, sticky="e", pady=4, padx=(0,8))
    entry_ang = ttk.Entry(frame)
    entry_ang.grid(row=9, column=1, sticky="ew", pady=4)

    boton_validar = ttk.Button(frame, text="Confirmar datos", command=validar_entradas)
    boton_validar.grid(row=10, column=0, columnspan=2, pady=(20,10), sticky="ew")

    boton_volver = ttk.Button(frame, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.grid(row=11, column=0, columnspan=2, pady=(0,8), sticky="ew")

    frame.columnconfigure(1, weight=1)
