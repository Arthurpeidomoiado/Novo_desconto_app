from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass
class DescontoNormal(IDesconto):
    desconto = 'Normal'
    def calcular(self,valor):
        valor_desconto = valor * 0.1
        valor_desconto =valor_desconto 
        return valor_desconto
class DescontoVIP(IDesconto):
    desconto = 'Vip'
    def calcular(self, valor):
        return valor * 0.2
class DescontoPremium(IDesconto):
    desconto = 'Premium'
    def calcular(self,valor):
        return valor * 0.3
