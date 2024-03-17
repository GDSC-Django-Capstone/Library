"use strict";

let search = document.querySelector('.index_search_button');
let term = document.querySelector('.index_search_input');

let task = document.querySelector('.task');

let host = "http://127.0.0.1:8000/user/admin/update/";

search.addEventListener('click',function(){

    if(term.value.replace(/ /g,"") != ""){

        let request = new Request(host,{
            method:"POST",
            body:JSON.stringify({
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


                if(taskMid){
                    taskMid.remove();
                }


                let html = `
                    
                    <div class="task_mid">
                        <a class="link" href="/user/admin/updater/${data["bid"]}">
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
                        </a>
                    </div>
                    
                
                `;


                
                task.insertAdjacentHTML('beforeend', html);


            }
    
        })
        .catch(error=>{
            alert("Unexpected error, try reloading the page")
            console.error(error);
        });





    }

});



