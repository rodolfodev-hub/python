# programa tem como exemplo a eliminação de espaços em branco(de maneira temporária)
linguagem = "java   "            # A string tem espaços em branco à direita
print(linguagem)                 # Imprime a string original
print(linguagem.rstrip())        # Remove os espaços à direita da string (somente na exibição)
print(linguagem)                 # Imprime novamente a string original
