# Python Essentials 1 (Cisco Networking Academy) e a certificação.
# PCEP — Certified Entry-Level Python Programmer (Python Institute). 
print("Hello World!!") # Tradição da programação!
print("-----------------------------------------")
print("My name is Mateus Melo.\n")
print("-----------------------------------------")
print("A aranha pequenininha\nsubiu a tromba d'água.")
print("-----------------------------------------")
print("abaixo veio a chuva\ne lavou a aranha.")
print("Eu gosto \"Monty Python\"") # (\) para fugir das aspas
print("-----------------------------------------")
print('Eu gosto "Monty Python"') # Python pode usar -- ' ' -- ao 
# envés de aspas e não precisa usar escape aqui
# A barra invertida (\) tem um significado muito especial quando usada 
# dentro de strings – isso é chamadode caractere de escape.
# A letra n colocada após a barra invertida vem da palavra newline (nova linha).
# Tanto a barra invertida quanto o n formam um símbolo especial chamado caractere 
# de nova linha, que incita o console a iniciar uma nova linha de saída.
print("-----------------------------------------")
print("Programação", "essencial", "em", sep="***", end="...")
print("Python")
print("-----------------------------------------")
print("Meu nome é ", end="_")
print("Monty Python", sep="_", end="_") # Meu nome é _Monty Python --> é o que aparece 
# no terminal, veja que, quando utilizei sep="_", o depurador não separou com "_", pois
# o depurador lê "Monty Python" como uma coisa só (um argumento)... Diferente quando 
# utilizo: "Monty", "Python", sep="_". O depurador irá enxergar uma ordem de leitura, 
# primeiro argumento "Monty", depois irá ler o segundo argumento "Python" e então 
# separá-los com "_". Veja:
print()
print("Meu nome é ", end="_")
print("Monty", "Python", sep="_", end="_") 
print()

#Veja essa brincadeira para entendimento:
print("-----------------------------------------")
###################
print("versão original:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("com menos 'print()' invocações:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("mais alto:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("dobrou:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)