import re
from pprint import pprint

numeros = '''
(21) 9 1234-1234
(11) 9878-9874
(35)9 9874-1235
(31) 1596-7532
9 4532-1423
1425-3625
'''

# r = r'(?:(\(\d{2}\))\s)?(?:(\d)\s)?(\d{4}-\d{4})'  # separa por bloco
r = r'(?:\(\d{2}\)\s)?(?:\d\s)?\d{4}-\d{4}'  # tudo junto
# r = r'(\(\d{2}\)\s)?(9\s)?(\d{4}-\d{4})'  # separa por bloco com espaços

numeros_regexp = re.compile(r, flags=re.MULTILINE)

pprint(numeros_regexp.findall(numeros))
