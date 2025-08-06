from abc import ABC, abstractmethod

class BaseCredito(ABC):
    def __init__(self, monto, plazo, tasa):
        self.monto = monto
        self.plazo = plazo
        self.tasa = tasa

    @abstractmethod
    def calcular_cuota(self):
        pass