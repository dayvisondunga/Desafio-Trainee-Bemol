#Qual a proporção do valor adicionado bruto médio ao valor adicionado bruto total médio no estado
# do Amazonas no ano de 2018?

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

def valorProporcao():
    list_setor_servicos = []
    list_bruto_total = []

    #adicionando valores nas listas de serviços (list_setor_servicos) e na lista de bruto total médio (list_bruto_total)
    for linha in list_conteudo[0:]:
        if linha[0] == '2018' and linha[2] == 'Amazonas':
            list_setor_servicos.append(float(linha[8]))
            list_bruto_total.append(float(linha[10]))

    #obetendo a média do setor de serviços e do bruto total no estado do Amazonas
    media_setor_servicos = sum(list_setor_servicos) / len(list_setor_servicos)
    media_bruto_total = sum(list_bruto_total) / len(list_bruto_total)

    #fazendo o calculo do valor da proporção e da porcentagem
    proporcao_valor = media_setor_servicos/media_bruto_total
    proporcao_porcentagem = "{:.2f}%".format(media_setor_servicos/media_bruto_total*100)

    #imprimindo no terminal o resultado alcançado
    print("3. Qual a proporção do valor adicionado bruto médio do setor de serviços em relação ao valor adicionado bruto total médio no estado do Amazonas no ano de 2018?\n")
    print("A proporção do setor de serviços pelo total em valores é: ", proporcao_valor)
    print("A proporção do setor de serviços pelo total em porcentagem é: ", proporcao_porcentagem)

    #criando o arquivo saida_q3.txt e escrevendo o resultado dentro do arquivo
    with open('./Desafio-Trainee-Bemol/questao_03/saida_q1.txt', 'w', encoding="utf-8") as saida:
        saida.write("3. Qual a proporção do valor adicionado bruto médio do setor de serviços em relação ao valor adicionado bruto total médio no estado do Amazonas no ano de 2018?\n")
        saida.write(f"A proporção do setor de serviços pelo total em valores é:{proporcao_valor}\n")
        saida.write(f"\nA proporção do setor de serviços pelo total em porcentagem é:{proporcao_porcentagem}")
    saida.close()