"use strict";


let tasks = document.querySelector('.task_bottom');

let host = 'http://127.0.0.1:8000/user/admin/return/';





tasks.addEventListener('click',function(e){
    if(e.target.classList.contains("return_button")){

        let request = new Request(host,{
            method:'POST',
            body:JSON.stringify({'task':'return','uid':e.target.dataset.uid,'bid':e.target.dataset.bid}),
        });

        fetch(request)
        .then(response=>{
            if(!response.ok){
                throw new Error("Unexpected error, try reloading the page");
            }
            return response.json();
        }).then(data=>{

            if(data['msg']){
                alert(data['msg']);
            }

            if(data['task'] == "clear"){
                e.target.parentElement.remove();
            }


        })
        .catch(error=>{
            alert(error);
            console.error(error);
        })

    }

});














let observer = new IntersectionObserver(entries=>{
    let entry = entries[0];

    let request = new Request(host,{
        method:'POST',
        body:JSON.stringify({'task':'load'}),
    });

    if(entry.isIntersecting){
        fetch(request)
        .then(response=>{
            return response.json();
        }).then(data=>{
            if(data['data'] == "end"){
                return;
            }


            let totalHtml = '';

            data['data'].forEach((comment)=>{
                
                let html = `
                    <div class="request">
                        <div class="request_info">
                            <p>${comment.email}</p>
                            <p>${comment.title}</p>
                        </div>

                        <button class="return_button" data-uid="${comment.uid}" data-bid="${comment.bid}">Returned</button>
                    </div>
                `;
            
                totalHtml = totalHtml + html;
                
            });
            
            tasks.insertAdjacentHTML('beforeend', totalHtml);
            observer.observe(tasks.lastElementChild)


        })
        .catch(error=>{
            console.error(error);
        })

        observer.unobserve(entry.target);
    }

},{
    root:tasks,
    rootMargin:"150px",
});

observer.observe(tasks.lastElementChild);