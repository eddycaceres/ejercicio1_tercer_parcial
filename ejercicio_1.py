import csv

class Persona:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = float(salario)
        self.deducciones = float(deducciones)
        self.genero = genero

class GestorPersonas:
    def __init__(self, archivo):
        self.personas = []
        self.cargar_personas(archivo)
    
    def cargar_personas(self, archivo):
        with open(archivo, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                persona = Persona(
                    row['Nombre'],
                    row['Apellido'],
                    row['Edad'],
                    row['Salario'],
                    row['Deducciones'],
                    row['Género']
                )
                self.personas.append(persona)

    def persona_mayor_edad(self):
        return max(self.personas, key=lambda persona: persona.edad)

    def persona_menor_edad(self):
        return min(self.personas, key=lambda persona: persona.edad)

    def contar_genero(self):
        hombres = sum(1 for persona in self.personas if persona.genero.lower() == 'masculino')
        mujeres = sum(1 for persona in self.personas if persona.genero.lower() == 'femenino')
        return hombres, mujeres

    def promedio_salario(self):
        total_salario = sum(persona.salario for persona in self.personas)
        return total_salario / len(self.personas)

    def persona_con_mas_deducciones(self):
        return max(self.personas, key=lambda persona: persona.deducciones)

    def persona_que_gana_mas(self):
        return max(self.personas, key=lambda persona: persona.salario)

def main():
    gestor_personas = GestorPersonas('datos.csv')

    persona_mayor_edad = gestor_personas.persona_mayor_edad()
    print(f"Persona con mayor edad: {persona_mayor_edad.nombre} {persona_mayor_edad.apellido}")

    persona_menor_edad = gestor_personas.persona_menor_edad()
    print(f"Persona con menor edad: {persona_menor_edad.nombre} {persona_menor_edad.apellido}")

    hombres, mujeres = gestor_personas.contar_genero()
    print(f"Hombres: {hombres}, Mujeres: {mujeres}")

    promedio_salario = gestor_personas.promedio_salario()
    print(f"Promedio de salario: {promedio_salario}")

    persona_mas_deducciones = gestor_personas.persona_con_mas_deducciones()
    print(f"Persona con más deducciones: {persona_mas_deducciones.nombre} {persona_mas_deducciones.apellido}")

    persona_que_gana_mas = gestor_personas.persona_que_gana_mas()
    print(f"Persona que gana más: {persona_que_gana_mas.nombre} {persona_que_gana_mas.apellido}")

if __name__ == "__main__":
    main()
