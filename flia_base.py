import abc


class FilaBase(metaclass=abc.ABCMeta):
    # Código é um atributo
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_tual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...

