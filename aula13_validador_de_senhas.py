import re

# https://en.wikipedia.org/wiki/List_of_Unicode_characters
validador_senha_regexp = re.compile(
    # letras minúsculas, maiúsculas, números e caracteres especiais
    r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12}',
    flags=re.MULTILINE | re.VERBOSE)

if __name__ == '__main__':
    from pprint import pprint
    senhas = '''
m0|;36w=GQaB
8@jIoGY18>}n
pgB5\52|H So
n'}t]Fp3L12C
-C:zw3:A4Rp4
S7;{8;20KC`V
:N[CS1!N\939
J|7::>5RH60R
01DN$)`00T:S
N7?66XQ%]|V4
AIK{[R^!?PA`
H{P|]E_XW!N_
T>~!NTZ~_FS|
CQT<W+`D|@#W
="{PBU)V]T;X
BMREHRZSMKRF
JYDMXCQNACFN
RHHZGHOWOEHV
LADFSXKOTHHV
MWBJWRVAFTLV
5g$X9s
xU20c\\
W91:by
8rj{Z1
l}E9q7
'''
    pprint(validador_senha_regexp.findall(senhas))
