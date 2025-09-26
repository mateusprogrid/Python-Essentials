# Operadores - ferramentas de manipulação de dados
# Operadores básicos:
# +, -, *, /, //, %, **
# ----------------------------------------------------------------------------------------------------
# Exponenciação:
print(2 ** 3) # R: 8
print(2 ** 3.) # R: 8.0
print(2. ** 3) # R: 8.0
print(2. ** 3.) # R: 8.0
print()
# Quando os dois ** argumentos são inteiros, o resultado também é um número inteiro;
# Quando pelo menos um argumento ** é um float, o resultado também é um float.
# Nota: Recebemos os asteriscos duplos com espaços em nossos exemplos. Não é obrigatório, 
# mas melhora a legibilidade do código.
# ----------------------------------------------------------------------------------------------------
# Multiplicação:
print(2 * 3) # R: 6
print(2 * 3.) # R: 6.0
print(2. * 3) # R: 6.0
print(2. * 3.) # R: 6.0
print()
# Nota: Mantém a regra da exponenciação.
# ----------------------------------------------------------------------------------------------------
# Divisaão
print(6 / 3) # R: 2.0
print(6 / 3.) # R: 2.0
print(6. / 3) # R: 2.0
print(6. / 3.) # R: 2.0
print()
# Nota: Você verá que há uma exceção à regra.
# O resultado produzido pelo operador de divisão é sempre um float, independentemente de 
# parecer ou não ser um flutuante à primeira vista: 1 / 2, ou se parece com um inteiro 
# puro: 2 / 1.
# Isso é um problema? Sim!
# Às vezes acontece que você realmente precisa de uma divisão que forneça um valor inteiro, 
# não um valor flutuante. Felizmente, o Python pode ajudá-lo com isso.
# ----------------------------------------------------------------------------------------------------
# Divisão de número inteiro (divisão arredondada). 
print(6 // 3) # R: 2
print(6 // 3.) # R: 2.0
print(6. // 3) # R: 2.0
print(6. // 3.) # R: 2.0
print()
# Um sinal // (barra dupla) é um operador de divisão inteira. Difere do padrão / operador em 
# dois detalhes:
# seu resultado não possui a parte fracionária ‒ está ausente (para inteiros), ou é sempre igual 
# a zero (para flutuantes); isso significa que os resultados são sempre arredondados;
# ele está de acordo com a regra integer vs. float.
# Ex.:
print(6 // 4) # R: 1.5 (real), R: 1 (interpretado pela máquina)
print(6. // 4) # R: 1.5 (real), R: 1.0 (interpretado pela máquina)
print()
# ATENÇÃO!!
# O resultado da divisão do número inteiro é sempre arredondado para o valor inteiro mais próximo que 
# é menor que o resultado real (não arredondado).
print(-6 // 4) # R: -1.5 (real), R: -2 (interpretado pela máquina)
print(6. // -4) # R: -1.5 (real), R: -2.0 (interpretado pela máquina)
print()
# ----------------------------------------------------------------------------------------------------
# Restante (módulo)
# Esse operador é bastante peculiar, porque não tem equivalente entre os operadores aritméticos 
# tradicionais. O resultado do operador é o restante após a divisão do número inteiro.
print(14 % 4) # R: 2 (Resta 2)
print(12 % 4.5) # R: 3 (Resta 3)
print()
# ----------------------------------------------------------------------------------------------------
# Adição
print(-4 + 4) # R: 0
print(-4. + 8) # R: 4.0
print()
# ----------------------------------------------------------------------------------------------------
# Subtração
print(-4 - 4) # R: -8
print(4. - 8) # R: -4.0
print(-1.1) # R: -1.1
print()
# ----------------------------------------------------------------------------------------------------
# Expressões e Prioridades
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# R: ((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# R: ((5 * ((7 + 100) / 26)) // 2)
# R: ((5 * ((107 / 26)) // 2)
# R: ((5 * (4,1) // 2)
# R: ((20,5) // 2)
# R: 10.0
print()
print((2 ** 4), (2 * 4.), (2 * 4))
# R: 16 8.0 8
print()