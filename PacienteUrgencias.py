from Paciente import Paciente

class PacienteUrgencias(Paciente):
    
    #Metodo Contructor que hereda y inicializa los datos
    def __init__(self, Nombre: str, Identificacion: str, Costo_Base_Servicio: float, Dias_Hospilatizacion: int, Prioridad: int):
        super().__init__(Nombre, Identificacion, Costo_Base_Servicio, Dias_Hospilatizacion)
        
        # Validación adicional
        if not isinstance(Prioridad, int) or Prioridad < 1 or Prioridad > 5:
            raise ValueError("ERROR: La prioridad debe ser un número entre 1 y 5.")
        
        self.__Prioridad = Prioridad
        self.__Recargo_Urgencias = 50000  # Recargo fijo por atención inmediata

    #Implementación del método abstracto
    def calcular_costo_tratamiento(self) -> float:
        costo_tratamiento = self._Costo_Base_Servicio + self.__Recargo_Urgencias
        return costo_tratamiento

    # Getter de prioridad
    def get_Prioridad(self) -> int:
        return self.__Prioridad

    # Mostrar datos del paciente
    def Mostrar_Informacion(self) -> str:
        costo_final = self.Calcular_Costo_Total()  # Usa el método del padre
        return (
            f"<===== Paciente Urgencias =====>\n"
            f"Paciente: {self._Nombre}\n"
            f"Prioridad: {self.__Prioridad}\n"
            f"Costo Final: ${costo_final:,.0f}\n"
            f"----------------------------------"
        )
