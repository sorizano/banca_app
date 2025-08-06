from .base_model import BaseCredito

class CreditoHipotecario(BaseCredito):
    def calcular_cuota(self):
        r = self.tasa / 12 / 100
        n = self.plazo * 12
        cuota = self.monto * (r * (1+r)**n)/((1+r)**n - 1)
        return round(cuota,2)

class CreditoVehicular(BaseCredito):
    def calcular_cuota(self):
        r = self.tasa / 12 / 100
        n = self.plazo * 12
        cuota = self.monto * (r * (1+r)**n)/((1+r)**n - 1)
        return round(cuota * 1.05,2) # incluye seguro vehicular