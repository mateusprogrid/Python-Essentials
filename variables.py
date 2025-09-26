# -----> Variáveis <-----
var = 1
print(var)
print("----------------------------------------------------------")
# Você já sabe que pode fazer algumas operações aritméticas com esses números: 
# Adicionar, subtrair etc. Você fará isso muitas vezes.
# Mas é uma pergunta normal perguntar como armazenar os resultados dessas operações, 
# para usá-los em outras operações e assim por diante.
# Como você salva os resultados intermediários e os usa novamente para produzir os 
# subsequentes?
# Python irá ajudá-lo com isso. Ele oferece "caixas" especiais (ou "contêineres", 
# como podemos chamá-los) para essa finalidade, e essas caixas são chamadas de 
# variáveis - o próprio nome sugere que o conteúdo desses contêineres pode ser variado 
# (quase) de qualquer forma.
# ------------------------------------------------------------------------------------------------
# Variáveis são espaços reservados na memória!
# O que todas as variáveis Python têm?
# • Um nome;
# • Um valor (o conteúdo do contêiner).
# As variáveis não aparecem em um programa automaticamente. Como desenvolvedor, você 
# deve decidir quantas variáveis e quais usar em seus programas.
# Você também deve nomeá-los.
# ------------------------------------------------------------------------------------------------
# Nomes de variáveis
# O PEP 8 - Guia de Estilo para Código Python recomenda a seguinte convenção de nomenclatura 
# para variáveis e funções em Python:
# • Os nomes de variáveis devem estar em letras minúsculas, com palavras separadas por 
# sublinhados para melhorar a legibilidade (por exemplo, var, my_variable)
# • Nomes de funções seguem a mesma convenção que nomes de variáveis (por exemplo, fun,
# my_function)
# • Também é possível usar casos mistos (por exemplo, myVariable), mas apenas em contextos onde 
# esse já é o estilo predominante, para manter a compatibilidade com a convenção adotada.
# Obs.: As mesmas restrições se aplicam a nomes de função.
# CUIDADO:
# Dê uma olhada na lista de palavras que desempenham um papel muito especial em todos os programas 
# Python.
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Eles são chamados de palavras-chave reservadas. Eles são reservados porque você não deve usá-los 
# como nomes: nem para suas variáveis, nem funções, nem quaisquer outras entidades nomeadas que você 
# deseja criar.
# -------> Uma variável passa a existir como resultado da atribuição de um valor a ela. Ao contrário 
# de outros idiomas, você não precisa declará-lo de nenhuma maneira especial. <-------
# -------> A criação (ou seja, sua sintaxe) é extremamente simples: basta usar o nome da variável 
# desejada, depois o sinal de igual (=) e o valor que deseja colocar na variável. <-------
valor_produto = "R$ 10.00"
print(valor_produto)
print("----------------------------------------------------------")
# ------------------------------------------------------------------------------------------------
# Como usar uma variável
var = 1
account_balance = 1000.0
client_name = 'Gustavo Pereira'
print(var, account_balance, client_name)
print(var)
print("----------------------------------------------------------")

funcionario_name = 'Larissa Vaz'
presenca = 'Presente'
print("Chamada de funcionários: " + funcionario_name, presenca)
print("----------------------------------------------------------")
# ------------------------------------------------------------------------------------------------
# Como atribuir um novo valor a uma variável já existente
var = 1
print(var)
var = var + 1
print(var)
print("----------------------------------------------------------")
# A primeira linha do trecho cria uma nova variável chamada var e atribui 1 a ela.
# A instrução diz: atribua um valor de 1 a uma variável denominada var.
# A terceira linha atribui a mesma variável com o novo valor retirado da própria variável, 
# somada com 1. Vendo um registro como esse, um matemático provavelmente protestaria - nenhum 
# valor pode ser igual a si mesmo mais um. Isso é uma contradição. Mas Python trata o sinal = não 
# como igual a, mas como atribuir um valor a.
# A nova instrução diz: Pegue o valor atual da variável var, adicione 1 e armazene o resultado 
# na variável var.
# ------------------------------------------------------------------------------------------------
# Problemas matemáticos com variáveis
a = 3
b = 4
c = (a ** 2 + b ** 2) ** 0.5
print("c = ", c)
print("----------------------------------------------------------")

jhon = 3
mary = 5
adam = 6
print(jhon, mary, adam, sep=",")
total_apples = jhon + mary + adam
print("Total de maças:", total_apples)
print("----------------------------------------------------------")
# ------------------------------------------------------------------------------------------------
# Variáveis ‒ um simples conversor -
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")
print("----------------------------------------------------------")
# Nota: round(), é uma novidade. É uma função cujo trabalho é arredondar o resultado de saída para 
# o número de casas decimais especificadas entre parênteses e retornar um float (dentro da função 
# round() você pode encontrar o nome da variável, uma vírgula e o número de casas decimais que 
# pretendemos por).
# ------------------------------------------------------------------------------------------------
# Operadores e Expressões
# 3x³ - 2x² + 3x - 1, o resultado deve ser atribuído a y.
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
print("----------------------------------------------------------")
# Dê uma olhada no código no editor: ele lê um valor float, coloca-o em uma variável chamada x e 
# imprime o valor de uma variável chamada y