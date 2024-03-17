"use strict";


let title = document.querySelector('.title');
let author = document.querySelector('.author');
let genre = document.querySelector('.genre');
let amount = document.querySelector('.amount');
let image = document.querySelector('.file');
let description = document.querySelector('.task_mid>textarea');
let add = document.querySelector('.task_bottom>button');


let host = "http://127.0.0.1:8000/user/admin/add/";

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

    formdata.append("image",file);


    // send the form

    let request = new Request(host,{
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

        alert(data['msg']);

        if(data['task'] == "erase"){
            title.value = "";
            author.value = "";
            genre.value = "";
            amount.value = "";
            description.value = "";
            image.value = "";

        }

    })
    .catch(error=>{
        alert('Unexpected error, try reloading the page');
        console.log(error);
    });
    


});















