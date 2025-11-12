from Paciente import Paciente

class PacienteGeneral(Paciente):
    
    #Metodo Contructor que hereda y inicializa los datos
    def __init__(self, Nombre: str, Identificacion: str, Costo_Base_Servicio: float, Dias_Hospilatizacion: int, Tipo_Consulta: str):
        super().__init__(Nombre, Identificacion, Costo_Base_Servicio, Dias_Hospilatizacion)
        self.__Tipo_Consulta = Tipo_Consulta
        self.__Descuento_EPS = 0.20  # 20% de descuento

    #Implementación del método abstracto
    def calcular_costo_tratamiento(self) -> float:
        costo_tratamiento = self._Costo_Base_Servicio * (1 - self.__Descuento_EPS)
        return costo_tratamiento

    # Getter para el tipo de consulta
    def get_Tipo_Consulta(self) -> str:
        return self.__Tipo_Consulta

    # Mostrar información del paciente
    def Mostrar_Informacion(self) -> str:
        costo_final = self.Calcular_Costo_Total()  # Usa el método del padre (ya aplica la tasa)
        return (
            f"<===== Paciente General =====>\n"
            f"Paciente: {self._Nombre}\n"
            f"Tipo de Consulta: {self.__Tipo_Consulta}\n"
            f"Costo Final: ${costo_final:,.0f}\n"
            f"----------------------------------"
        )
