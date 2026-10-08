from src.models.desconto import Desconto

class Pedido:
    def __init__(self, cliente, desconto : Desconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0
    def valor_final(self, valor) -> float:
        self.valor_original = valor
        return self.valor_original - self.desconto.calcular(self.valor_original)