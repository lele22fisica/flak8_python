from constantes import CODIGO_NORMAL

from flia_base import FilaBase


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:  # Esta seta com a palavra 'None' indica que este método não retorna nada.
        self.senhatual = f'{CODIGO_NORMAL}{self.codigo}'  # Ele pega o atributo senhatual e simplsmente iguala o atributo a um sufixo mais um código.

    def chama_cliente(self, caixa: int) -> str:
        clienteatual: str = self.fila.pop(0)
        self.clientes_atendidos.append(clienteatual)
        return (f'Cliente atual: {clienteatual}, dirija-se ao caixa: {caixa}')
