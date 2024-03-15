"use strict";


let bookContainer = document.querySelector('.book_container');
let borrow = document.querySelector('.info_container_bottom>button');
let send = document.querySelector('.comments_container_bottom>button');
let comment = document.querySelector('.commentbox');
let commentContainer = document.querySelector('.comments_container_top');

let hostBorrow = 'http://127.0.0.1:8000/book/function/borrow/';
let hostComment = 'http://127.0.0.1:8000/book/function/comment/';
let hostRate = 'http://127.0.0.1:8000/book/function/rate/';




function fetcher(req, erase=false){

    fetch(req)
    .then(response=>{
        if(!response.ok){
            throw new Error('Unexpected error, try reloading the page');
        }

        return response.json();
    })
    .then(data=>{
        

        if(data['task'] == 'redirect'){
            window.location.href = "/login";
        }

        if(data['task'] == 'add'){

            let html = `
                <div class="comment">
                    <div class="comment_top">
                        <div></div>
                        <p>${data['name']}</p>
                    </div>

                    <div class="comment_bottom">
                        <p>${comment.value}</p>
                    </div>
                </div>
            `;


            commentContainer.insertAdjacentHTML('afterBegin', html);

            comment.value = '';

            return;


        }

        if(erase){
            comment.value = '';
        }

        alert(data['msg']);

    })
    .catch(error=>{
        alert("Unexpected error, try reloading the page")
        console.error(error);
    });


}


bookContainer.addEventListener('click',function(e){
    if(e.target == borrow){
        let host = hostBorrow + borrow.dataset.id + '/';
    
        let request = new Request(host,{
            method:"POST",
        });

        fetcher(request);
        

    }else if(e.target.classList.contains('star')){

        let star = e.target;
        let book_id = borrow.dataset.id;
        let rating = star.dataset.rating;

        let host = hostRate + book_id + '/'  + rating + '/';
    
        let request = new Request(host,{
            method:"POST",
        });

        fetcher(request);


    }else if(e.target == send){

        let host = hostComment + borrow.dataset.id + '/';

        let data = JSON.stringify({
            'comment':comment.value,
        });

    
        let request = new Request(host,{
            method:"POST",
            headers:{
                'Content-Type':'application/json',
            },
            body:data,
        });

        fetcher(request,true);
        

    }



});