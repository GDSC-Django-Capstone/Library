"use strict";


let tasks = document.querySelector('.task_bottom');

let host = 'http://127.0.0.1:8000/user/admin/lent/';








let observer = new IntersectionObserver(entries=>{
    let entry = entries[0];

    let request = new Request(host,{
        method:'POST',
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

            data['data'].forEach((lent)=>{
                
                let html = `
                    <div class="lent">
                        <p>${lent['email']}</p>
                        <div class="lent_info">
                            <div>
                                <p>First Name:</p>
                                <p>${lent['fname']}</p>
                            </div>

                            <div>
                                <p>Last Name:</p>
                                <p>${lent['lname']}</p>
                            </div>
                        </div>
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