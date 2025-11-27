import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://github.com/melosant')
except: # caso não consiga acessar, seja por falta de internet ou qualquer outro motivo.
    print('Não consegui acessar o repositório de Nathã Melo.')
else:
    print('Consegui acessar o repositório do Nathã Melo.')