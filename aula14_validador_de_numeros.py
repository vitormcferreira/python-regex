import re

texto = '''
10
10.20
-10
-10.20967
+10
+10.20
0
-0
+0
-0.1
+0.1
000.1
-000.1
+000.1
'''
# validador_de_numeros = re.compile(
#     r'^[+-]?\d+(?:\.\d+)?$',
#     flags=re.MULTILINE
# )
# print(validador_de_numeros.findall(texto))


def is_float(string):
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))


def is_int(string):
    return bool(re.search(r'^[+-]?\d+$', string))
