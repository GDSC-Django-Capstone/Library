"use strict";


let email = document.querySelector('.email')
let password = document.querySelector('.password')
let loginButton = document.querySelector('.register_mid_bottom>button');

let host = 'http://127.0.0.1:8000/login/';


loginButton.addEventListener('click',function(){
    let data = JSON.stringify({
        'email':email.value,
        'password':password.value,
    });

    let request = new Request(host,{
        method:"POST",
        headers:{
            'Content-Type':'application/json',
        },
        body:data,
    });

    fetch(request)
    .then(response=>{
        if (!response.ok) {
            throw new Error('Unexpected error, try reloading the page');
        }

        return response.json();
    })
    .then(data=>{
        alert(data['msg']);

        if(data['task'] == 'redirect'){
            let hostArray = host.split('/');
            let redirect = hostArray.slice(0,(hostArray.length-2)).join("/");
            
            window.location.replace(redirect);
        }else if(data['task'] == 'admin'){
            window.location.replace("http://127.0.0.1:8000/user/admin/add/");
        }

    })
    .catch(error=>{
        alert("Unexpected error, try reloading the page");
        console.log(error);
    });


    

});