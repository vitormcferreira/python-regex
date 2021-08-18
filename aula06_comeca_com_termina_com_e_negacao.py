# Meta caracteres:
# ^ -> começa com
# $ -> termina com

# [^a-z] -> nesse contexto significa negação (deve ir no inicio do conjunto)

import re

cpf = '012.345.678-90'
print(re.findall(r'^([0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2})$', cpf))

# qualquer coisa que não seja [a-z]
print(re.findall(r'[^a-z]+', cpf))