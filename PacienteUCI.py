from Paciente import Paciente

class PacienteUCI(Paciente):
    
    #Metodo Contructor que hereda y inicializa los datos
    def __init__(self, Nombre: str, Identificacion: str, Costo_Base_Servicio: float, Dias_Hospilatizacion: int, Soporte_vital: bool):
        super().__init__(Nombre, Identificacion, Costo_Base_Servicio, Dias_Hospilatizacion)
        self.__Soporte_vital = Soporte_vital
        self.__COSTO_DIA_UCI = 800000

    #Implementación del método abstracto
    def calcular_costo_tratamiento(self) -> float:
        costo_tratamiento = self._Costo_Base_Servicio + (self._Dias_Hospilatizacion * self.__COSTO_DIA_UCI)
        return costo_tratamiento

    # Mostrar información del paciente
    def Mostrar_Informacion(self) -> str:
        costo_final = self.Calcular_Costo_Total()  # Usa el método del padre (ya aplica la tasa)
        
        if self.__Soporte_vital:
            soporte = "Con soporte"
        else:
            soporte = "Sin soporte"
        
        return (
            f"<========= Paciente UCI =========>\n"
            f"Paciente: {self._Nombre}\n"
            f"Hospitalizado: {self._Dias_Hospilatizacion} días, {soporte}\n"
            f"Costo Final: ${costo_final:,.0f}\n"
            f"----------------------------------"
        )
