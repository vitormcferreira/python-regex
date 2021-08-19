# Metacaracteres: ^ $ \ ( )

# grupos
# (abc|def) -> encontra 'abc' ou 'def'

#         retrovisores (usados para acessar o grupo criado, os indices são por ordem de criação)
# ()      \1
# ()()    \1 \2
# (())()  \1 \2 \3

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

# print('\nSeleciona tag e conteudo:')
# pprint(re.findall(r'<([pdiv]{1,3})>(.*?)<\/\1>', texto))

# pprint(re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)', texto))

# # grupo nomeado
# tags = re.findall(r'(<(?P<tag>[pdiv]{1,3})>(.*?)<\/(?P=tag)>)', texto)
# print('nomeado')
# pprint(tags)

# # (?: ) o ?: no inicio do grupo faz com que ele não seja salvo
# pprint(re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>', texto))

# pprint(re.findall(r'<(.+?)>(.*?)<\/\1>', texto))
# pprint(re.findall(r'<(.+?)>(.*?)<\/\1>', texto))

# pprint(re.findall(r'(<p>.*?</p>)', texto))


# Remontar a tag html
# pprint('\nRemonta a tag HTML:')
# pprint(re.sub(r'(<(.+?)>)(.*?)(<\/\2>)', r'\1Meu texto\3\4', texto))
pprint(re.findall(r'(?:<(.+?)>).*?(<\/\1>)', texto))


# print('\nSeleciona cpf:')
# cpf = '012.345.678-90'
# # seleciona o cpf
# print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
# # seleciona o cpf
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
