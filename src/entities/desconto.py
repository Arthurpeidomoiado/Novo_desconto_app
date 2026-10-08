from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass
class DescontoNormal(IDesconto):
    def calcular(self,valor,sub):
        valor_desconto = valor * 0.1
        valor_desconto =valor_desconto +  -sub
        return valor_desconto
class DescontoVIP(IDesconto):
    def calcular(self, valor):
        return valor * 0.2
class DescontoPremium(IDesconto):
    def calcular(self,valor):
        return valor * 0.3
