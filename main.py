from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
# control/
senha = FilaNormal()
senha.atualiza_fila()
senha.atualiza_fila()
senha.atualiza_fila()
print(senha.chama_cliente(5))
senha.chama_cliente(9)
print(senha.chama_cliente(10))
#print(senha.chama_cliente(11))

senha = FilaPrioritaria()
senha.atualiza_fila()
senha.atualiza_fila()
senha.atualiza_fila()
senha.atualiza_fila()
print(senha.chama_cliente(10))
print(senha.chama_cliente(1))
