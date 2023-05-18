from abc import ABC
from errores import ValidadorError, NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTienePalabraSecretaError, NoTieneCaracterEspecialError

class ReglaValidacion (ABC):
    def __init__(self, longitud_esperada = 8):
        self.longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str):
        if len(clave) < self.longitud_esperada:
            raise NoCumpleLongitudMinimaError("La clave no cumple la longitud minima")

    def _contiene_mayuscula(self, clave: str):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave no tiene ninguna letra mayuscula")

    def _contiene_minuscula(self, clave: str):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave no tiene ninguna letra minuscula")

    def _contiene_numero(self, clave: str):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave no tiene ningun numero")

    @abstractmethod
    def es_valida(self, clave: str):
        pass

class ReglaValidacionGanimedes:
    def __init__(self):
        pass

    def contiene_caracter_especial(self, clave: str):
