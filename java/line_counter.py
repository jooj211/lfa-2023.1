import os

def contar_linhas_diretorio(diretorio):
    total_linhas = 0

    # Obtém o caminho absoluto do diretório atual
    diretorio_atual = os.path.abspath(diretorio)

    # Percorre todos os arquivos do diretório atual
    for nome_arquivo in os.listdir(diretorio_atual):
        caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

        # Verifica se o caminho é um arquivo (ignora subdiretórios)
        if os.path.isfile(caminho_arquivo):
            with open(caminho_arquivo, 'r') as arquivo:
                linhas_arquivo = arquivo.readlines()
                total_linhas += len(linhas_arquivo)

    return total_linhas

# Exemplo de uso
diretorio_atual = os.getcwd()  # Obtém o diretório atual
numero_linhas = contar_linhas_diretorio(diretorio_atual)
print(f'O número total de linhas nos arquivos do diretório {diretorio_atual} é: {numero_linhas}')