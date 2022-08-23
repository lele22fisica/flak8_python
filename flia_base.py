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

    def inseri_cliente(self):
        self.fila.append(self.senha_tual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...

