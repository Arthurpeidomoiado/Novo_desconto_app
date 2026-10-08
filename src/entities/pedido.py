from src.entities.desconto import IDesconto

class Pedido:
    def __init__(self, cliente, desconto : IDesconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0
    def valor_desconto(self) -> float:
        return self.desconto.calcular(self.valor_original)
    def valor_final(self) -> float:
        return self.valor_original - self.valor_desconto()