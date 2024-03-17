"use strict";


let email = document.querySelector('.superemail');
let button = document.querySelector('.task_bottom>button');


let host = "http://127.0.0.1:8000/user/super/remove/";


button.addEventListener('click',function(){

    let request = new Request(host,{
        method:"POST",
        body:JSON.stringify({
            'email':email.value,
        }),
    });

    fetch(request)
    .then(response=>{
        if(!response.ok){
            throw new Error('Unexpected error, try reloading the page');
        }

        return response.json();
    })
    .then(data=>{

        alert(data['msg']);

        if(data['task'] == "clear"){
            email.value="";

        }

    })
    .catch(error=>{
        alert("Unexpected error, try reloading the page");
        console.log(error);
    });

});
