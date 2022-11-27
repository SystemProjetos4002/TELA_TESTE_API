var form = document.getElementById('forminput');
var login = document.getElementById('loginenter');
var senha = document.getElementById('senhapswd')

eel.expose(go_to)
        function go_to(url) {window.location.replace(url);};


form.addEventListener('submit', e => {
  e.preventDefault()

  eel.tentativa_login(login.value,senha.value)(function(response){                      
 
       document.getElementById('h1id').innerHTML = response;
       if(response == 'LOGADO COM SUCESSO'){
        go_to('session_check.html')
       }

     })
});

