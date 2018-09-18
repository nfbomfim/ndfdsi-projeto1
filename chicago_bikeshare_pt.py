'''Programa Nanodegree Fudamentos de Data Science I - Modulo 2 - Projeto 1
Autor: Fabio Bomfim Nunes Data: 14.09.2018'''
# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for x in range(0, 20): #utilizando a função range() como interador para
    print(data_list[x]) # delimitar a qtde de linhas impressas

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Loop original do primeiro envio do projeto.
# Objetivo alcançado mas acolhi a sugestão do revisor para
# u,ma melhor apresentação
#for ROW_LIST in data_list[:20]: # Criando uma lista de lista utilizando
#    print(ROW_LIST[6])          # a propria lista como interador

# Sugestão do revisor para melhor apresentação do resultado
for i, line in enumerate(data_list[:20], start=1):
    print(f"Line: {i} \tGender: {line[-2]}")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    '''a função column_to_list recebe dois parametros de entrada (uma lista e
     um indice da lista) e retorna como valor uma lista de lista a partir
     de uma determinada coluna passado como parametro'''

    column_list = []
    for row_list in data: # Utilizando a função enumerate()
        column_list.append(row_list[index])  # como interador e criando Uma
                                             # lista apartir de seus interaveis

# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
for x, row_list in enumerate(data_list):
    if row_list[-2].lower() == 'male':
        male += 1
    elif row_list[-2].lower() == 'female':
        female += 1


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    '''função que recebe uma lista como parametro, contabiliza e retornar
     uma tupla de valores de genero masculi e femenino da lista'''

    male = 0
    female = 0
    #utilizadndo a funcão count() para retornar a quantidade de determinado
    #parametro presente em uma lista
#    male = column_to_list(data_list, -2).count('Male')
#    female = column_to_list(data_list, -2).count('Female')

#   A obrigatoriedade de não utilização de função era da TAREFA 4.
#   Por esse motivo, como já havia apresentado a habilidade de contar sem
#   a utilização de função resolvi empregar outra forma para demonstração
#   dos conhecimento. De qualquer forma estarei acatando a solicitação do
#   revisor apesar de não concordar.
    for x, row_list in enumerate(data_list):
        if row_list[-2].lower() == 'male':
            male += 1
        elif row_list[-2].lower() == 'female':
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    ''' Função que recebe uma lista como parametro e retorna uma string
    determinando qual o gênero mais polular da lista'''
    answer = ""

    #utilizado-se da função count_gener() da tarefa anterior para
    #determinar qual o gênero mais popular

    # Realmente faz senti a orientação do revisor. Uma situação que passou
    # desapercebido. Sem necessidade de chamar mais de uma vez a função
    # count_gener()

    male, female = count_gender(data_list)
#    if count_gender(data_list)[0] > count_gender(data_list)[1]:
    if male > female:
        answer = "Masculino"
#    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
    elif male < female:
        answer = "Femenino"
    else:
        answer = "Igual"

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

# Eu pensei em fazer a mesma função para determinar as quantidade de
# user_type, mas como não ficou claro para mim na atividade eu somente
# alterei os titulo e rotumos das propriedade do grafico.
def count_user_type(data_list):
    '''função que recebe uma lista como parametro, contabiliza e retornar
     uma tupla de valores de tipos de usuários (Subscribe e Customer)
      da lista.'''

    subscriber = 0
    customer = 0
    for x, row_list in enumerate(data_list):
        if row_list[-3].lower() == 'subscriber':
            subscriber += 1
        elif row_list[-3].lower() == 'customer':
            customer += 1

    return [subscriber, customer]

gender_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Type')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Os valores diferentes de 'Male' e 'Female' estão sendo desprezados \
na contabilização da lista."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
sum_list = 0.
for ind, trip_duration in enumerate(trip_duration_list):
    #totalizador de duração da viagem
    sum_list += float(trip_duration)

    #definição da viagem de maior e menor duração
    if ind == 0:
        min_trip = int(trip_duration)
        max_trip = int(trip_duration)
        continue

    if min_trip > int(trip_duration):
        min_trip = int(trip_duration)
    elif max_trip < int(trip_duration):
        max_trip = int(trip_duration)

#calculo da média de duração da viagem (totalizador / pela quantidade de
#de trip_duration na lista)
mean_trip = round(sum_list/len(trip_duration_list))
#convertendo trip_duration_list de string para Integer
trip_duration_list = [int(duration) for duration in trip_duration_list]
#para então classificar de forma correta a lista como Integer
trip_duration_list.sort()
#definição da mediana;. Se o tamanmo da lista for impar, basta pegar a posição
#central da lista. Caso contrario deve-se pegar os dois pontos centrais,
#soma-los e dividir por 2 para obter a mediana
if len(trip_duration_list) % 2 == 1:
    median_trip = round(trip_duration_list[len(trip_duration_list)//2 +1])
else:
    median_trip = round((trip_duration_list[len(trip_duration_list)//2-1] +
    trip_duration_list[len(trip_duration_list)//2 +2]) /2.0)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    '''Função para retornar os tipos presentes em uma lista de uma
    determinada coluna e quantifica-los sem a definição como hard code
    tornando uma função generica.'''
    item_types = []
    count_items = []
    count = 0
    item_types = list(set(column_list))
    #utilizando-se do Compression List e da função count() para obter
    #uma lista totalizada dos tipos de itens
    #count_items = [column_to_list(data_list, -2).count(item)
    #for item in item_types]

    # Como esta tarefa não havia restrição quanto ao uso de função
    # tentei utilizar para fixar
    for item in item_types:
        for lista in data_list:
            if lista[-2] == item:
                count += 1
        count_items.append(count)
        count = 0

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
