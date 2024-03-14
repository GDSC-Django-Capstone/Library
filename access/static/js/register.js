"use strict";

let fname = document.querySelector('.fname')
let lname = document.querySelector('.lname')
let email = document.querySelector('.email')
let password = document.querySelector('.password')
let registerButton = document.querySelector('.register_mid_bottom>button');

let host = 'http://127.0.0.1:8000/register/';


registerButton.addEventListener('click',function(){
    let data = JSON.stringify({
        'fname':fname.value,
        'lname':lname.value,
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
        }

    })
    .catch(error=>{
        alert("Unexpected error, try reloading the page");
        console.log(error);
    });


    

});