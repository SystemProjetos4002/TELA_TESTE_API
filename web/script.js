var form = document.getElementById('forminput');
var login = document.getElementById('loginenter');
var senha = document.getElementById('senhapswd')
form.addEventListener('submit', e => {
  e.preventDefault()
  // alert(login.value)
  // eel.random_python()(function(number){                      
  //   // Update the div with a random number returned by python
  //   alert( document.getElementById('h1id').innerHTML)
  //   document.getElementById('h1id').innerHTML = number;
  // })
  eel.random_python(login.value,senha.value)(function(number){                      
    //   // Update the div with a random number returned by python
    //   alert( document.getElementById('h1id').innerHTML)
       document.getElementById('h1id').innerHTML = number;
     })
});

