# \w -> inclui todas as letras, numeros e _ (todas as linguagens). Se a flag re.ASCII for usada encontra apenas [a-zA-Z0-9_]
# \W -> negação de \w

# \d -> [0-9]
# \D -> [^0-9] -> negação de \d

# \s -> espaços em branco
# \S -> negação de \s

# \b -> borda 
# \B -> oposto de \b

import re


texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jão
çか

foo,
'''
# [À-ú] -> range de letras acentuadas e ç

# print(re.findall(r'[a-z0-9À-ú]+', texto, flags=re.I))
# print(re.findall(r'\w+', texto, flags=re.I))
# print(re.findall(r'\W+', texto, flags=re.I))

# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))

# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\S+', texto, flags=re.I))

# começa com e
# print(re.findall(r'\be\w*', texto, flags=re.I))

# termina com e
print(re.findall(r'\w*e\b', texto, flags=re.I))

# palavras com 4 letras
print(re.findall(r'\b\w{4}\b', texto, flags=re.I))

# print(re.findall(r'\bfoo\B', 'foooo', flags=re.I))
