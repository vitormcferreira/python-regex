# Metacaracteres: ^ $ \ ( )

# Quantificadores
# é aplicado ao elemento à esquerda
# * -> 0 ou n
# + -> 1 ou n
# ? -> 0 ou 1
# { } -> {n} {1,10}

import re

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>
'''

# guloso
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))

# ? depois de * ou + impede esse comportamento
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
