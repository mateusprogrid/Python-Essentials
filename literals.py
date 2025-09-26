# Literais - os dados em si -
# Um literal são dados cujos valores são determinados pelo próprio literal.
# é um conceito difícil de entender, um bom exemplo pode ser útil.
# Veja o seguinte conjunto de dígitos:
# 123
# Você consegue adivinhar qual valor representa? Claro que você pode
# - são cento e vinte e três.
# Mas e quanto a isso:
# c
# Isso representa algum valor? Talvez. Pode ser o símbolo da velocidade 
# da luz, por exemplo. Também pode ser a constante de integração. Ou até mesmo 
# o comprimento de uma hipotenusa no sentido de um teorema de Pitágoras. Há muitas 
# possibilidades.
# --------------------------------------------------------------------------------------
#E esta é a pista: 123 é um literal e c não é.
print("2")
print(2)
print("------")
# Ambas instruções imprimem 2.
# Por quê?
# Neste exemplo, você encontrará dois tipos diferentes de literais:
# uma -- string --, que você já conhece, são usadas quando você precisa 
# processar texto
# e um -- número inteiro (int) --, algo completamente novo.
# Em Python um inteiro pode ser escrito da seguinte forma: 
# 11111111 ou desta forma: 11_111_111 (só a partir do Python 3.6).
print("2.5")
print(2.5)
print(0.4)
print("------")
# Neste exemplo, você encontrará dois tipos diferentes de literais:
# uma -- string --, que você já conhece, são usadas quando você precisa 
# processar texto
# e um -- número ponto flutuante (float) --, algo completamente novo.
# Em Python um float só pode ser escrito com "." Ex.: 25.7 
# Você deve garantir que seu número não contenha nenhuma vírgula.
# pois a própria vírgula tem seu próprio significado reservado em Python.
print(2e4) # "e" ou "E" representa 2 x 10⁴ = 20000.0
print(6.5647E4) # 6.5647 x 10⁴ = 65647.0
print(0.00000000000000000001) # Resultado: 1e-23
print("------")
# --------------------------------------------------------------------------------------
# Valores booleanos
# São usadas para representar um valor muito abstrato - a veracidade. Cada vez que 
# você pergunta ao Python se um número é maior que outro, a pergunta resulta na criação 
# de alguns dados específicos - um valor booleano.
# Álgebra booleana ‒ uma parte da álgebra que faz uso de apenas dois valores distintos: 
# True e False, denotados como 1 e 0.
print(True > False) # A máquina entende: 1 > 0? Resposta: True (Sim, 1 é maior do que 0)
print(True < False)
print("------")