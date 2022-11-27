from random import randint
import requests
import cripto
import json
import eel
  
eel.init("web")  
  
# Exposing the random_python function to javascript
@eel.expose    
def random_python(login,senha):
    try:
        trylogin = requests.get(f'http://192.168.0.150:5000/get/getlogin?login={login}&senha={senha}')
        responselogin = trylogin.content.decode('utf-8')
        # print(responselogin,type(responselogin))
        if responselogin == 'ACEITO':
            return 'LOGADO COM SUCESSO' 
        elif responselogin == 'SENHA INCORRETA':
            return 'SENHA INCORRETA'
        else:
            return 'LOGIN INCORRETO'
    except:
        return'ERRO O SISTEMA ENCONTRA-SE INOPERANTE NO MOMENTO. CONTATE A AREA RESPONSÁVEL.'
  
# Start the index.html file
eel.start("index.html")