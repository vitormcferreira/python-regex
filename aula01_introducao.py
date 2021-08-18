# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html
import re

# findall search sub
# compile

string = 'Este é um teste de expressões teste regulares'

# r'' é para o uso do \ único

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string, count=0))

# Compilando a expressão regular (melhora desempenho)
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
