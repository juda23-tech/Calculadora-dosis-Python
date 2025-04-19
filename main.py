print("Calculadora de dosis médicas (uso educativo)")

nombre = input("Nombre del paciente: ")
peso = float(input("Peso del paciente (kg): "))
edad = int(input("Edad del paciente (años): "))

print("\nMedicamentos disponibles:")
print("1. Paracetamol")
print("2. Amoxicilina")
print("3. Ibuprofeno")
opcion = int(input("Selecciona el número del medicamento: "))

if opcion == 1:
    dosis = 15
    nombre_medicamento = "Paracetamol"
elif opcion == 2:
    dosis = 40
    nombre_medicamento = "Amoxicilina"
elif opcion == 3:
    dosis = 10
    nombre_medicamento = "Ibuprofeno"
else:
    print("Opción inválida.")
    exit()

dosis_total = dosis * peso

print(f"\n--- Resultado ---")
print(f"Paciente: {nombre}")
print(f"Medicamento: {nombre_medicamento}")
print(f"Dosis recomendada: {dosis_total:.2f} mg")

if opcion == 2:
    print("(Dosis total diaria: dividir entre 2 o 3 tomas según indicación médica)")
else:
    print("(Cada dosis individual: repetir cada 6-8 horas según indicación médica)")