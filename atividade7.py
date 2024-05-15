# Função para contar a frequência das palavras em uma frase
def contar_frequencia(frase):
    # Dividindo a frase em palavras
    palavras = frase.split()

    # Inicializando o dicionário para armazenar a frequência das palavras
    frequencia = {}

    # Iterando sobre cada palavra na lista de palavras
    for palavra in palavras:
        # Se a palavra já estiver no dicionário, incrementa sua contagem
        if palavra in frequencia:
            frequencia[palavra] += 1
        # Se a palavra não estiver no dicionário, adiciona-a com contagem 1
        else:
            frequencia[palavra] = 1

    return frequencia

# Frase de exemplo
frase_exemplo = "O rato roeu a roupa do rei de Roma"

# Chamando a função para contar a frequência das palavras na frase de exemplo
frequencia_palavras = contar_frequencia(frase_exemplo)

# Imprimindo a frequência de cada palavra
for palavra, frequencia in frequencia_palavras.items():
    print(f"A palavra '{palavra}' aparece {frequencia} vezes na frase.")
