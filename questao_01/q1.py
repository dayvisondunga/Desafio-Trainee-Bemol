#Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?

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
        list_conteudo.append(conteudo) #guardando o que está dentro de conteúdo na lista de conteúdo (list_conteudo) crianda mais acima
    arq.close() #fechando o arquivo de dados após a leitura

#Função media para fazer o calculo do PIB per capita de Manaus entre 2010 a 2018 
def media():
    pib = [] #lista para armazenar os valores do PIB per capita de Manaus entre 2010 a 2018
    resultados = [] #lista para armazenar os resultados de cada ano da respectiva cidade
    for coluna in list_conteudo[0:]:
        if coluna[3] == 'Manaus':
           pib.append(float(coluna[13])) #adicionando os valores dos PIBs(coluna[13]) de cada ano na lista pib
           
            #adicionando na lista resultados os titulos    
                                   # Ano    -  Estado     -  Cidade     - Pib per capita       
           resultados.append(f'{coluna[0]:} - {coluna[2]} - {coluna[3]} - R${coluna[13]}')
    
    #função sum() - somar os valores contidos na lista pib
    #função len() - quantidade de elementos na lista pib
    #usando função sum() e dividindo pela função len() e armazenando o valor na variável media_Manaus
    media_Manaus = sum(pib)/len(pib)

    #criando o arquivo saida_q1.txt e escrevendo o resultado dentro do arquivo
    with open('./Desafio-Trainee-Bemol/questao_01/saida_q1.txt', 'w', encoding="utf-8") as saida:
        saida.write('Ano  -  Estado -  Cidade - Pib per capita\n')
        for ocorrencias in resultados:
            saida.write(f'{ocorrencias}')

        #escrevendo no arquivo o valor da media do PIB formatado e usando apenas 2 casas decimais após as virgulas    
        saida.write("\nO valor médio do PIB per capital de Manaus no período que abrange o dataset é: R${:.2f}".format(media_Manaus))
    saida.close()
        
        #imprimindo no terminal o valor da media do PIB formatado e usando apenas 2 casas decimais após as virgulas
    print("O valor médio do PIB per capital de Manaus no período que abrange o dataset é: R${:.2f}".format(media_Manaus))

    
