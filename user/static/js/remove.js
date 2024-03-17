"use strict";

let search = document.querySelector('.index_search_button');
let term = document.querySelector('.index_search_input');

let task = document.querySelector('.task');

let host = "http://127.0.0.1:8000/user/admin/remove/";

search.addEventListener('click',function(){

    if(term.value.replace(/ /g,"") != ""){

        let request = new Request(host,{
            method:"POST",
            body:JSON.stringify({
                "task":"read",
                "title":term.value,
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
            
            if(data['msg']){
                alert(data['msg']);
            }
            

            if(data['status'] == "add"){

                
                let taskMid = document.querySelector(".task_mid");
                let amount = document.querySelector(".amount");
                let taskBottom = document.querySelector(".task_bottom");

                if(taskMid){
                    taskMid.remove();
                }

                if(amount){
                    amount.remove();
                }

                if(taskBottom){
                    document.querySelector('.task_bottom>button').removeEventListener('click',remover);
                    taskBottom.remove();
                }

                let html1 = `
                    <div class="task_mid">
                        <div class="book">
                            <div class="book_left">
                                <img src="http://127.0.0.1:8000/${data['image']}">
                            </div>

                            <div class="book_right">
                                <p class="title ">${data['title']}</p>
                                <p class="author">${data['author']}</p>
                                <p class="genre">${data['genre']}</p>
                                <p class="rating">${data['rating']}/10</p>
                            </div>
                        </div>
                    </div>
                
                `;


                let html2 = `
                    <div class="amount">
                        <div>
                            <p>Amount to remove</p>
                            <p>(Available:${data['amount']})</p>
                        </div>

                        <input type="number" min="1" value="1">
                    </div>

                    <div class="task_bottom">
                        <button data-bid="${data['bid']}">Remove</button>
                    </div>
                
                `;

                let totalHtml = html1 + html2;
                
                task.insertAdjacentHTML('beforeend', totalHtml);


                let remove = document.querySelector('.task_bottom>button');
                console.log(remove);

                remove.addEventListener('click',function(e){
                    remover(e);
                });

            }
    
        })
        .catch(error=>{
            alert("Unexpected error, try reloading the page")
            console.error(error);
        });





    }

});





function remover(e){

    let request = new Request(host,{
        method:"POST",
        body:JSON.stringify({
            "task":"remove",
            "number":document.querySelector('.amount>input').value,
            "bid":e.target.dataset.bid,
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
        
        if(data['msg']){
            alert(data['msg']);
        }
        

        

    })
    .catch(error=>{
        alert("Unexpected error, try reloading the page")
        console.error(error);
    });


};