# Flags
# re.A  ou re.ASCII -> ASCII
# re.I ou re.IGNORECASE -> Ignore case
# re.M ou re.MULTILINE -> aplicado em ^ e $, as flags são aplicadas linha a linha
# re.S ou re.DOTALL -> o . reconhece \n

import re


texto = '''
012.345.678-90 a
012.345.678-91
012.345.678-92
'''

# print(re.findall(r'^\d{3}.\d{3}.\d{3}-\d{2}$', texto, flags=re.M))

texto2 = '''O João gosta de folia 
E adora ser amado'''

print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
