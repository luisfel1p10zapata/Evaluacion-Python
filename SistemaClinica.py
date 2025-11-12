class SistemaClinica:
    
    #Creamos una lista vacia
    def __init__(self):
        self.lista_pacientes = []

    #Metodo que añade los pacientes a la lista vacia
    def set_agregar_paciente(self, paciente):
        self.lista_pacientes.append(paciente)
        print(f"Paciente agregado: {paciente.get_Nombre()}")

    #Metodo para generar y calcular reporte
    def generar_reporte_costos(self):
        total_facturacion = 0
        total_tasa_adm = 0

        print("<== Reporte De Costos Clínicos ==>")
        print('----------------------------------')
        #Ciclo para recorrer la lista de paciente
        for paciente in self.lista_pacientes:
            costo_final = paciente.Calcular_Costo_Total()

            
            total_facturacion = total_facturacion + costo_final
            total_tasa_adm = total_tasa_adm + (costo_final * paciente.TASA_ADM_CLINICA)
            
            # Mostrar información del paciente
            print(paciente.Mostrar_Informacion())

        # Mostrar resumen general
        print("----------------------------------")
        print("<=========== Totales ===========>")
        print(f"Total Facturación: ${total_facturacion:,.0f}")
        print(f"Total Ingreso por TASA: ${total_tasa_adm:,.0f}")
        print("----------------------------------\n")
