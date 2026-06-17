import tkinter as tk
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
    win.title("Poligono 1 - Cálculo de Azimut")
    win.geometry("450x600")
    win.configure(bg="#ecf0f1")
    
    titulo = ttk.Label(win, text="Cálculo de Coordenadas", font=("Segoe UI", 16, "bold"), background="#ecf0f1")
    titulo.pack(pady=15)

    # --- Creación de los campos de entrada ---
    coord_entries_coordenadas = {}
    campos = [
        "Norte Estación", "Este Estación", 
        "Norte Calaje", "Este Calaje", 
        "Ángulo Cente (gon)", "Distancia DH (m)"
    ]

    frame_inputs = tk.Frame(win, bg="#ecf0f1")
    frame_inputs.pack(pady=10)

    for i, campo in enumerate(campos):
        tk.Label(frame_inputs, text=campo + ":", bg="#ecf0f1", font=("Segoe UI", 10)).grid(row=i, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(frame_inputs, justify="center")
        entry.grid(row=i, column=1, padx=5, pady=5)
        coord_entries_coordenadas[campo] = entry

    # --- Frame para Mostrar Resultados (Oculto inicialmente) ---
    coord_result_frame = tk.Frame(win, bg="#ecf0f1")
    
    font_res = ("Segoe UI", 10, "bold")
    result_azimut_label = tk.Label(coord_result_frame, bg="#ecf0f1", fg="#2980b9", font=font_res)
    result_azimut_label.pack(anchor="w", pady=2)
    
    result_at_label = tk.Label(coord_result_frame, bg="#ecf0f1", fg="#2980b9", font=font_res)
    result_at_label.pack(anchor="w", pady=2)
    
    result_cpn_label = tk.Label(coord_result_frame, bg="#ecf0f1", fg="#27ae60", font=font_res)
    result_cpn_label.pack(anchor="w", pady=2)
    
    result_cpe_label = tk.Label(coord_result_frame, bg="#ecf0f1", fg="#27ae60", font=font_res)
    result_cpe_label.pack(anchor="w", pady=2)
    
    result_nuevo_n_label = tk.Label(coord_result_frame, bg="#ecf0f1", fg="#8e44ad", font=font_res)
    result_nuevo_n_label.pack(anchor="w", pady=2)
    
    result_nuevo_e_label = tk.Label(coord_result_frame, bg="#ecf0f1", fg="#8e44ad", font=font_res)
    result_nuevo_e_label.pack(anchor="w", pady=2)

    # --- LÓGICA DE CÁLCULO  ---
    def calcular_coordenadas():
        for key in coord_entries_coordenadas:
            if coord_entries_coordenadas[key].get().strip() == "":
                return

        try:
            N_est = float(coord_entries_coordenadas["Norte Estación"].get())
            E_est = float(coord_entries_coordenadas["Este Estación"].get())
            N_cal = float(coord_entries_coordenadas["Norte Calaje"].get())
            E_cal = float(coord_entries_coordenadas["Este Calaje"].get())
            ang_cente = float(coord_entries_coordenadas["Ángulo Cente (gon)"].get())
            dh = float(coord_entries_coordenadas["Distancia DH (m)"].get())

            delta_n = N_cal - N_est
            delta_e = E_cal - E_est

            if delta_n == 0 and delta_e == 0:
                coord_result_frame.pack_forget()
                return

            if delta_n > 0 and delta_e > 0:
                cuadrante = 1
            elif delta_n < 0 and delta_e > 0:
                cuadrante = 2
            elif delta_n < 0 and delta_e < 0:
                cuadrante = 3
            elif delta_n > 0 and delta_e < 0:
                cuadrante = 4
            else:
                coord_result_frame.pack_forget()
                return

            if delta_n != 0:
                rumbo_rad = atan(abs(delta_e / delta_n))
                rumbo_gon = rumbo_rad * (200 / pi)
            else:
                coord_result_frame.pack_forget()
                return

            if cuadrante == 1:
                azimut = rumbo_gon
            elif cuadrante == 2:
                azimut = 200 - rumbo_gon
            elif cuadrante == 3:
                azimut = 200 + rumbo_gon
            else:
                azimut = 400 - rumbo_gon

            ang_trabajo = azimut + ang_cente

            cpn = dh * cos(ang_trabajo * pi / 200)
            cpe = dh * sin(ang_trabajo * pi / 200)

            n_punto = N_est + cpn
            e_punto = E_est + cpe

            result_azimut_label.config(text=f"Azimut (gon): {azimut:.4f}")
            result_at_label.config(text=f"Ángulo de trabajo (gon): {ang_trabajo:.4f}")
            result_cpn_label.config(text=f"Coordenada Parcial Norte (CPN): {cpn:.4f}")
            result_cpe_label.config(text=f"Coordenada Parcial Este (CPE): {cpe:.4f}")
            result_nuevo_n_label.config(text=f"Nueva Coordenada Norte: {n_punto:.4f}")
            result_nuevo_e_label.config(text=f"Nueva Coordenada Este: {e_punto:.4f}")

            coord_result_frame.pack(padx=40, pady=(0, 10), anchor="w")

        except ValueError:
            coord_result_frame.pack_forget()
            messagebox.showerror("Error", "Por favor, ingresa solo valores numéricos válidos.")

    # --- Botones de Acción ---
    btn_calcular = ttk.Button(win, text="Calcular Azimut", command=calcular_coordenadas)
    btn_calcular.pack(pady=10)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10) 

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