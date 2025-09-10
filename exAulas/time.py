import time

def funcao_1():
    inicio = time.time()
    time.sleep(5)
    fim = time.time() #simular alguma interação
    duracao = fim - inicio
    print(f"O tempo de execução é de: {duracao:.2f} segundos")

# Executa a função
funcao_1()
