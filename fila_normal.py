class FilaNormal:
    # Código é um atributo
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_tual: str = ""

    def gera_senha_atual(self) -> None:  # Esta seta com a palavra 'None' indica que este método não retorna nada.
        self.senhatual = f'NM{self.codigo}'  # Ele pega o atributo senhatual e simplsmente iguala o atributo a um sufixo mais um código.

    def reseta_filha(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atuaiza_fila(self) -> None:
        self.reseta_filha()
        self.gera_senha_atual()
        self.fila.append(self.senhatual)
        # caixa é um argumento

    def chama_cliente(self, caixa: int) -> str:
        if self.fila:
            clienteatual: str = self.fila.pop(0)
            self.clientes_atendidos.append(clienteatual)
            return (f'Cliente atual: {clienteatual}, dirija-se ao caixa: {caixa}')
        else:
            raise ValueError('Vazio')
