#Qual o ranking de estados por média de PIB per capita no ano de 2010?

# importando o módulo do sistema operacional, para passar o caminho absoluto do arquivo de dados ".txt"
import os

#pegando o caminho absoluto do arquivo pib_municipio_2010_a_2018.txt e guardando na variável caminho
caminho = os.path.abspath("./Desafio-Trainee-Bemol/dataset/pib_municipio_2010_a_2018.txt")

#criando um lista para armazenar o conteudo do arquivo de dados
list_conteudo = []

#usando a função with open para abrir o arquivo para leitura e,
#passando como parâmetro a variável caminho, parâmetro 'r' para indicar que é leitura e,
#o encoding='utf-8'para especificar a codificação dos caractéres e conseguir fazer leitura de caractéres especiais e acentos do arquivo
with open(caminho, 'r', encoding='UTF-8') as arq:
    arq.readline()
    #fazendo um loop nas linhas dentro do arquivo
    for linhas in arq: 
        conteudo = linhas.split(";") #dividindo o conteúdo do arquivo em cada ";" guardando na variável conteudo
        list_conteudo.append(conteudo) #guardando o que está dentro de conteúdo na lista de conteúdo (list_conteudo) criado mais acima
    arq.close() #fechando o arquivo de dados após a leitura


def ranking():
    #listar estados
    list_estados = []
    for linha in list_conteudo[0:]:
        list_estados.append(linha[2]) #adicionando os valores de cada estados(coluna[2]) na lista list_estados
    list_estados = list(set(list_estados))

    #criando dicionário de estados
    dict_estados = {}
    for estado in list_estados:
        dict_estados[estado] = []

    #Somando PIB de cada estado
    for linha in list_conteudo[1:]:
        if linha[0] == '2010':
            dict_estados[linha[2]].append(float(linha[-1].replace('\n', '')))
    
    #função sum() - somar os valores contidos na lista pib
    #função len() - quantidade de elementos na lista pib
    #usando função sum() e dividindo pela função len() e armazenando o valor no dicionario de estados
    for estado in dict_estados:
        dict_estados[estado] = sum(dict_estados[estado]) / len(dict_estados[estado])

    #função sorted() - ordenar os valores contidos no dicionario de estados
    #função lambda recebe o parâmetro item na psoição [1] que está como chave do dicionário
    # reordenando as chaves (item) do dicionario pelo maior valor
    dict_estados = dict(sorted(dict_estados.items(), key=lambda item: item[1], reverse=True))

    #imprimindo o ranking no terminal
    print("2. Qual o ranking de estados por média de PIB per capita no ano de 2010?\n")
    print("Ranking de estados por média de PIB per capita no ano de 2010:")
    print('\nPosição  -      Estado         - Pib per capta médio\n')
    p = 0
    for i, r in dict_estados.items():
        p = p + 1
        print('{}°  -  {}  - R${:.2f}'.format((p), i, r))
    
    #criando o arquivo saida_q2.txt e escrevendo o resultado dentro do arquivo
    with open('./Desafio-Trainee-Bemol/questao_02/saida_q1.txt', 'w', encoding="utf-8") as saida:
        saida.write("2.Qual o ranking de estados por média de PIB per capita no ano de 2010?\n")
        saida.write('Ranking dos estados por média de PIB per capita em 2010:\n')
        saida.write('\nPosição  -  Estado  -  Pib per capta médio\n')
        p = 0
        for i, r in dict_estados.items():
            p = p + 1
            saida.write("\n{}° - {} - R${:.2f}\n".format(p, i, r))
    saida.close()