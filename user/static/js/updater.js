"use strict";


let title = document.querySelector('.title');
let author = document.querySelector('.author');
let genre = document.querySelector('.genre');
let amount = document.querySelector('.amount');
let image = document.querySelector('.file');
let description = document.querySelector('.task_mid>textarea');
let add = document.querySelector('.task_bottom>button');


let host = "http://127.0.0.1:8000/user/admin/updater/";

add.addEventListener('click',function(){

    let formdata = new FormData();

    // append title
    formdata.append("title",title.value);

    // append author
    formdata.append("author",author.value);

    // append genre
    formdata.append("genre",genre.value);

    // append amount
    formdata.append("amount",amount.value);
    
    // append description
    formdata.append("description",description.value);

    // append image

    let file = image.files[0];

    if(file){
    
        formdata.append("image",file);
    }


    // send the form

    let request = new Request(host+add.dataset.bid+"/",{
        method:"POST",
        body:formdata,
    });

    fetch(request)
    .then(response=>{
        if(!response.ok){
            throw new Error('Unexpected error, try reloading the page');
        }

        return response.json();
    })
    .then(data=>{

        if(data['msg']){
            alert(data['msg']);
        }
        

        if(data['task'] == "redirect"){
            
            window.location.replace("/user/admin/update/");
        }

    })
    .catch(error=>{
        alert('Unexpected error, try reloading the page');
        console.log(error);
    });
    


});















