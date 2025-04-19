import tkinter as tk
from tkinter import ttk, messagebox

medicamentos = {
    "Paracetamol": 15,
    "Amoxicilina": 40,
    "Ibuprofeno": 10
}

def calcular_dosis():
    try:
        nombre = entry_nombre.get()
        peso = float(entry_peso.get())
        edad = int(entry_edad.get())
        medicamento = combo_medicamento.get()

        if medicamento not in medicamentos:
            raise ValueError("Medicamento no válido.")

        dosis_estandar = medicamentos[medicamento]
        dosis_total = dosis_estandar * peso

        resultado = f"Paciente: {nombre}\n"
        resultado += f"Medicamento: {medicamento}\n"
        resultado += f"Dosis recomendada: {dosis_total:.2f} mg"

        if medicamento == "Amoxicilina":
            resultado += "\n(Dosis diaria. Repartir en 2 o 3 tomas)"
        else:
            resultado += "\n(Repetir cada 6-8 horas según indicación médica)"

        text_resultado.config(state='normal')
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado)
        text_resultado.config(state='disabled')

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de Dosis Médicas")
ventana.geometry("400x400")
ventana.resizable(False, False)
ventana.configure(bg="#f0f0f0")
fuente = ("Arial", 12)

tk.Label(ventana, text="Nombre del paciente:", bg="#f0f0f0", font=fuente).pack(pady=5)
entry_nombre = tk.Entry(ventana, font=fuente)
entry_nombre.pack()

tk.Label(ventana, text="Peso (kg):", bg="#f0f0f0", font=fuente).pack(pady=5)
entry_peso = tk.Entry(ventana, font=fuente)
entry_peso.pack()

tk.Label(ventana, text="Edad (años):", bg="#f0f0f0", font=fuente).pack(pady=5)
entry_edad = tk.Entry(ventana, font=fuente)
entry_edad.pack()

tk.Label(ventana, text="Medicamento:", bg="#f0f0f0", font=fuente).pack(pady=5)
combo_medicamento = ttk.Combobox(ventana, values=list(medicamentos.keys()), font=fuente)
combo_medicamento.set("Selecciona uno")
combo_medicamento.pack()

tk.Button(ventana, text="Calcular dosis", command=calcular_dosis, font=fuente).pack(pady=10)

text_resultado = tk.Text(ventana, height=6, width=40, font=fuente, wrap="word")
text_resultado.pack()
text_resultado.config(state='disabled')

ventana.mainloop()