# Metacaracteres: ^ $ \ ( )

# Quantificadores
# é aplicado ao elemento à esquerda
# * -> 0 ou n
# + -> 1 ou n
# ? -> 0 ou 1
# { } -> {n}
# { } -> {min, max}


# {10,} 10 ou mais
# {,10} de zero a 10
# {10} especificamente 10
# {5,10} de 5 a 10

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
'''

print(re.findall(r'jo+ão+', texto, flags=re.IGNORECASE))
# print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.IGNORECASE))
print(re.findall(r'jo*ão*', texto, flags=re.IGNORECASE))
print(re.findall(r'jo?ão*', texto, flags=re.IGNORECASE))
print(re.findall(r'jo{1,}ão{1,3}', texto, flags=re.IGNORECASE))


texto2 = 'João ama ser amado amad'
print(re.findall(r'ama[do]{,2}', texto2))
