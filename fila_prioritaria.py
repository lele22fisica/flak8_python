class FilaPrioritaria:
    #Código é um atributo
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def gera_senha_atual(self)-> None:
        self.senha_atual = f'PR{self.codigo}'

    def resta_fila(self)-> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self)-> None:
        self.resta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:int)-> str:
        if self.fila:
            clienteatual:str = self.fila.pop(0)
            self.clientes_atendidos.append(clienteatual)
            return (f'Cliente atual: {clienteatual}, dirija-se ao caixa: {caixa}')
        else:
            raise ValueError('Vazio')

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quantidade clientes atendidos'] = len(self.clientes_atendidos)

        return estatistica