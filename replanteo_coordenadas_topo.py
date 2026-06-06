import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import math

# Variables globales de tu grupo
datos_entrada = {}
resultados_calculo = []

def construir_interfaz(win):
    """Esta función recibe la ventana del profe y le instala tu programa"""
    
    # 1. Limpiar lo que haya puesto el profe de ejemplo en esa ventana
    for widget in win.winfo_children():
        widget.destroy()
        
    # 2. Funciones matemáticas
    def boton_1_entrada():
        global datos_entrada
        try:
            ee = float(simpledialog.askstring("Entrada", "Este de la Estación:"))
            ne = float(simpledialog.askstring("Entrada", "Norte de la Estación:"))
            er = float(simpledialog.askstring("Entrada", "Este de Referencia:"))
            nr = float(simpledialog.askstring("Entrada", "Norte de Referencia:"))
            
            datos_entrada = {
                "est": (ee, ne),
                "ref": (er, nr),
                "puntos": [
                    ("PR-01", ee + 5, ne + 5),
                    ("PR-02", ee - 5, ne - 5),
                    ("PR-03", ee, ne - 10)
                ]
            }
            messagebox.showinfo("Éxito", "Coordenadas base cargadas correctamente.")
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Debes ingresar números válidos.")

    def boton_2_calcular():
        global datos_entrada, resultados_calculo
        if not datos_entrada:
            messagebox.showwarning("Atención", "Primero ingresa los datos en el Botón 1.")
            return

        ee, ne = datos_entrada["est"]
        resultados_calculo = []
        
        for nombre, ep, np in datos_entrada["puntos"]:
            dx = ep - ee
            dy = np - ne
            dh = math.sqrt(dx**2 + dy**2)
            azimut = math.degrees(math.atan2(dx, dy)) % 360
            resultados_calculo.append((nombre, dh, azimut))
        
        messagebox.showinfo("Proceso", "Cálculos finalizados.")

    def boton_3_resultados():
        global resultados_calculo
        if not resultados_calculo:
            messagebox.showwarning("Atención", "Primero calcula los datos con el Botón 2.")
            return
        
        res_texto = "REPORTE DE REPLANTEO\n" + "-"*35 + "\n"
        res_texto += f"{'Punto':<8} | {'Dist. (m)':<10} | {'Azimut (°)':<10}\n"
        res_texto += "-"*35 + "\n"
        for p, d, a in resultados_calculo:
            res_texto += f"{p:<8} | {d:<10.3f} | {a:<10.4f}\n"
        
        ventana_res = tk.Toplevel(win)
        ventana_res.title("Resultados de Replanteo")
        tk.Label(ventana_res, text=res_texto, font=("Courier", 11), justify=tk.LEFT, padx=20, pady=20).pack()

    # 3. Dibujar tus botones en la ventana del profe
    titulo = ttk.Label(win, text="Módulo de Replanteo", font=("Segoe UI", 16, "bold"))
    titulo.pack(pady=(20, 10))

    btn_in = ttk.Button(win, text="1. Entrada de Coordenadas", command=boton_1_entrada)
    btn_in.pack(pady=10, fill='x', padx=50)

    btn_calc = ttk.Button(win, text="2. Procesar Azimuts", command=boton_2_calcular)
    btn_calc.pack(pady=10, fill='x', padx=50)

    btn_out = ttk.Button(win, text="3. Ver Cartera de Campo", command=boton_3_resultados)
    btn_out.pack(pady=10, fill='x', padx=50)

    # Botón para volver al menú principal
    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=(30, 10))
    