"use strict";

let returnBook = document.querySelectorAll('.overlay>button');

let host = 'http://127.0.0.1:8000/user/return/';

returnBook.forEach(book=>{
    book.addEventListener('click',function(e){
        e.preventDefault();



        let request = new Request(host + e.target.dataset.bid + "/",{
            method:"POST",
        })


        fetch(request)
        .then(response=>{

            if(!response.ok){
                throw new Error('Unexpected error, try reloading the page');
            }
            return response.json();
        })
        .then(data=>{

            alert(data['msg']);

        })
        .catch(error=>{
            alert("Unexpected error, try reloading the page");
            console.error(error);
        });
        





    });
});
