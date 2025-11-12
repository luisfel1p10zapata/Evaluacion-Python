from abc import ABC, abstractmethod

class Paciente(ABC):
    
    # Atributo de clase
    TASA_ADM_CLINICA = 0.05  

    # Constructor que permite inicializar
    def __init__(self, Nombre: str, Identificacion: str, Costo_Base_Servicio: float, Dias_Hospilatizacion: int):
        
        #Validaciones de datos
        if not isinstance (Nombre,str) or not Nombre or not Nombre.strip():
            raise ValueError("ERROR: El nombre del paciente no puede estar vacío y debe ser una cadena de texto.")
        if not isinstance (Identificacion,str) or not Identificacion or not Identificacion.strip():
            raise ValueError("ERROR: La identificación no puede estar vacía y debe ser una cadena de texto.")
        if not isinstance (Costo_Base_Servicio,(int,float)) or Costo_Base_Servicio <= 0:
            raise ValueError("ERROR: El costo base del servicio debe ser un número mayor que cero.")
        if not isinstance (Dias_Hospilatizacion,int) or Dias_Hospilatizacion < 0:
            raise ValueError("ERROR: Los días de hospitalización debe ser un número Positivo.")
        
        self._Nombre = Nombre
        self._Identificacion = Identificacion
        self._Costo_Base_Servicio = Costo_Base_Servicio
        self._Dias_Hospilatizacion = Dias_Hospilatizacion

    # Métodos y Getters
    def get_Nombre(self) -> str:
        return self._Nombre

    def get_Identificacion(self) -> str:
        return self._Identificacion

    def get_Costo_Base_Servicio(self) -> float:
        return self._Costo_Base_Servicio

    def get_Dias_Hospilatizacion(self) -> int:
        return self._Dias_Hospilatizacion

    #Método Abstracto 
    @abstractmethod
    def calcular_costo_tratamiento(self) -> float:
        #Método abstracto: debe devolver el costo del tratamiento antes de aplicar la tasa administrativa.
        pass

    # Método general que sí aplica la tasa administrativa
    def Calcular_Costo_Total(self) -> float:
        costo_tratamiento = self.calcular_costo_tratamiento()
        return costo_tratamiento * (1 + self.TASA_ADM_CLINICA)

    # Mostrar información general
    def Mostrar_Informacion(self) -> str:
        return f'Paciente: {self._Nombre}, Identificación: {self._Identificacion}, Días: {self._Dias_Hospilatizacion}, Costo Base: ${self._Costo_Base_Servicio:,.0f}'
