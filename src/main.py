from src.frameworks.database.memory_database import MemoryDatabase
from src.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.use_cases.criar_pedido import CriarPedido
from src.adapters.controlers.pedido_controller import PedidoController

def main() -> None:
    database = MemoryDatabase()
    gateway = MemoryPedidoRepository(database)
    use_case = CriarPedido(gateway)
    controller = PedidoController(use_case)

    pedido1 = controller.criar_pedido('Cliente A', 100, 'normal')
    pedido2 = controller.criar_pedido('Cliente B', 200, 'vip')
    pedido3 = controller.criar_pedido('Cliente C', 300, 'premium')

    print('Pedidos criados: ')
    print(pedido1.cliente, pedido1.desconto.desconto, pedido1.valor_final())
    print(pedido2.cliente, pedido2.desconto.desconto, pedido2.valor_final())
    print(pedido3.cliente, pedido3.desconto.desconto, pedido3.valor_final())

if __name__ == '__main__':
    main()