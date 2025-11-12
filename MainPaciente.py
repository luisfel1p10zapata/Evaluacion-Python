from SistemaClinica import SistemaClinica
from PacienteGeneral import PacienteGeneral
from PacienteUrgencias import PacienteUrgencias
from PacienteUCI import PacienteUCI

def main():
    
    #Crea un objeto de la clase sistema - Da funcionalidad
    sistema = SistemaClinica()

    #Creamos los objetos pacientes y usamos el metodo set para agregarlos
    print("\n<===== Lista de Pacientes =====>")
    
    try:
        Paciente_1 = PacienteGeneral("Mario Mendoza","837465189",150000,5,"Control")
        sistema.set_agregar_paciente(Paciente_1)
    except ValueError as e:
        print(e)

    try:
        Paciente_2 = PacienteUrgencias("Carolina Vallez","838563813",150000,1,3)
        sistema.set_agregar_paciente(Paciente_2)
    except ValueError as e:
        print(e)

    try:
        Paciente_3 = PacienteUCI("Luis Gonzales", "746272833",150000,1,True)
        sistema.set_agregar_paciente(Paciente_3)
    except ValueError as e:
        print(e)
        
    print("----------------------------------")

    # Generar el reporte solo si hay pacientes válidos
    if sistema.lista_pacientes:
        sistema.generar_reporte_costos()
    else:
        print("⚠️  No se pudo generar el reporte: no hay pacientes válidos.\n")

if __name__ == "__main__":
    main()
