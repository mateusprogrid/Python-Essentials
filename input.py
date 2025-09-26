# -----> Interação com o usuário <-----
# A função input()
# Vamos agora apresentar uma função completamente nova, que parece ser um 
# reflexo da boa e velha função print().
# Por quê?
# print() envia dados para o console. A nova função obtém dados dela.
# A função input() é capaz de ler os dados inseridos pelo usuário e retornar 
# os mesmos dados para o programa em execução.
# O programa pode manipular os dados, tornando o código verdadeiramente interativo.
print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "... Realmente?")
print("----------------------------------------------------------")
# Nota:
# • O programa solicita que o usuário insira alguns dados do console (provavelmente 
# usando um teclado, embora também seja possível inserir dados usando voz ou imagem);
# • A função input() é invocada sem argumentos (essa é a maneira mais simples de usar 
# a função); a função mudará o console para o modo de entrada; você verá um cursor 
# piscando e poderá inserir algumas teclas, finalizando pressionando a tecla Enter; 
# todos os dados inseridos serão enviados ao seu programa através do resultado da 
# função;
# • Nota: você precisa atribuir o resultado a uma variável; isso é crucial - perder 
# esta etapa fará com que os dados inseridos sejam perdidos;
# • Em seguida, usamos a função print() para exibir os dados que obtemos, com algumas 
# observações adicionais.
# ------------------------------------------------------------------------------------------
# A função input() com um argumento
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")
print("----------------------------------------------------------")
# Nota:
# • A função input() é invocada com um argumento ‒ é uma string contendo uma mensagem;
# • A mensagem será exibida no console antes que o usuário tenha a oportunidade de 
# digitar qualquer coisa;
# • input() fará seu trabalho.
# ------------------------------------------------------------------------------------------
# O resultado da função input() é uma string
# Uma string contendo todos os caracteres que o usuário insere no teclado. Não é um 
# inteiro ou um float.
# Isso significa que você não deve usá-lo como argumento de nenhuma operação aritmética, 
# por exemplo, você não pode usar esses dados para elevá-los ao quadrado, dividi-los por 
# qualquer coisa ou dividir qualquer coisa por eles.
# ⇩⇩
anything = input("Digite um número: ")
something = anything ** 2.0
print(anything, "elevado a 2 é", something)
# ⇧⇧
# ERRO!!
# Isso deve ser óbvio - você pode prever o valor de "ser ou não ser" elevado à potência 
# de 2?
# Nós não podemos. Python também não.
# Há uma solução para esse problema? Claro que sim.
# ------------------------------------------------------------------------------------------
# Conversão de tipo (tipo de conversões)
# O Python oferece duas funções simples para especificar um tipo de dados e resolver 
# esse problema: aqui estão eles: int() e float().
# • A função int() usa um argumento (por exemplo, uma string: int(string)) e tenta 
# convertê-lo em um número inteiro; se falhar, o programa inteiro também falhará 
# (há uma solução para essa situação, mas mostraremos isso um pouco mais tarde);
# • A função float() usa um argumento (por exemplo, uma string: float(string)) e 
# tenta convertê-la em um flutuante (o resto é o mesmo).
# Isso é muito simples e muito eficaz. Além disso, você pode chamar qualquer uma 
# das funções passando os resultados de input() diretamente para elas. Não há 
# necessidade de usar nenhuma variável como armazenamento intermediário.
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)
print("----------------------------------------------------------")

anything = int(input("Digite um número: "))
something = int(anything ** 2.0)
print(anything, "elevado a 2 é", something)
print("----------------------------------------------------------")
# ------------------------------------------------------------------------------------------
# Calculando a hipotenusa
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)
print("----------------------------------------------------------")
# ------------------------------------------------------------------------------------------
# Operadores de string
# ----> Concatenação <----
# É hora de voltar para esses dois operadores aritméticos: + e *.
# Agora, vamos mostrar que eles podem lidar com cadeias de caracteres, embora de 
# uma forma muito específica.
# O sinal de + (mais), quando aplicado a duas cadeias de caracteres, torna-se um 
# operador de concatenação:
# string + string
# Ela simplesmente concatena (cola) duas sequências de caracteres em uma.
# Não se esqueça - se você quiser que o sinal de + seja um concatenador, não um 
# somador, certifique-se de que ambos os argumentos sejam cadeias.
# "ab" + "ba" não é o mesmo que "ba" + "ab"
fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")
print("----------------------------------------------------------")
# Nota: usar + para concatenar strings permite que você construa a saída de uma 
# maneira mais precisa do que com uma função print() pura, mesmo se enriquecida 
# com os argumentos de palavra-chave end= e sep=.
# ----> Replicação <----
# O sinal * (asterisco), quando aplicado a uma string e um número (ou um número e 
# uma string, pois permanece comutativo nessa posição) se torna um operador de 
# replicação:
# string * number
# number * string
# Por exemplo:
# • "James" * 3 gera "JamesJamesJames"
# • 3 * "an" gera "ananan"
# • 5 * "2" (or "2" * 5) gera "22222" (não10!)
# ------------------------------------------------------------------------------------------
# str()
# Você já sabe como usar as funções int() e float() para converter uma string em um 
# número.
# Você também pode converter um número em uma string, o que é muito mais fácil e seguro 
# - esse tipo de operação é sempre possível.
# Uma função capaz de fazer isso é chamada str():
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é " + str((leg_a**2 + leg_b**2) ** .5))
print("----------------------------------------------------------")