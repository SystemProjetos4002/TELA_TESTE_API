from random import randint
import requests
import cripto
import json
import eel
import os

eel.init("web")  

@eel.expose    
def tentativa_login(login: str,senha : str):
    try:

        trylogin = requests.get(f'http://192.168.0.150:5000/get/getlogin?login={login}&senha={senha}')
        
        responselogin = trylogin.content.decode('utf-8')
      
        if responselogin == 'ACEITO':
            
            new_session = {}
            
            try:

                with open('session.json', 'r') as session_json:
                    
                 
                    new_session["login"] = cripto.encriptar(bytes(login.encode('utf-8'))).decode('utf-8')

                    new_session["senha"] =  cripto.encriptar(bytes(senha.encode('utf-8'))).decode('utf-8')
                    
                    os.remove('session.json')
                    
                    with open('session.json', 'w') as f:
                        json.dump(new_session, f, indent=4)

            except:
                
                new_session["login"]= cripto.encriptar(bytes(login.encode('utf-8'))).decode('utf-8')  # type: ignore
               
                new_session["senha"] = cripto.encriptar(bytes(senha.encode('utf-8'))).decode('utf-8') # type: ignore
                
                with open('session.json', 'w') as f:

                    json.dump(new_session, f, indent=4)

            return 'LOGADO COM SUCESSO' 
        
        elif responselogin == 'SENHA INCORRETA':
            
            return 'SENHA INCORRETA'
        else:
            
            return 'LOGIN INCORRETO'
    except:
        
        return'ERRO O SISTEMA ENCONTRA-SE INOPERANTE NO MOMENTO. CONTATE A AREA RESPONSÁVEL.'
  


# Start the index.html file
try:
    with open("config.json",'r') as r:

        config = json.load(r)

        iplocal = config["iplocal"]

        porta = config["porta"]

        with open('session.json', 'r') as s:

            session_json = json.load(s)
            
            login = session_json["login"]  # type: ignore
            
            senha = session_json["senha"]  # type: ignore
            
            logindec = cripto.decriptar(bytes(login.encode('utf-8'))).decode('utf-8')
            
            senhadec = cripto.decriptar(bytes(senha.encode('utf-8'))).decode('utf-8')  
        
            trylogin = requests.get(f'http://{iplocal}:{porta}/get/getlogin?login={logindec}&senha={senhadec}')
            
            if trylogin.content.decode('utf-8') != 'ACEITO':
            
                eel.start("index.html",disable_cache=True)
            
            else:
            
                eel.start("session_check.html",disable_cache=True)
except:
    
    eel.start("index.html",disable_cache=True)

