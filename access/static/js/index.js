'use strict';

let bookContainer = document.querySelector('.book_container');

let search = document.querySelector('.index_search_button');
let term = document.querySelector('.index_search_input');




search.addEventListener('click',function(){

    if(term.value.replace(/ /g,"") != ""){
        window.location.href = "/book/search/title/" + term.value;
    };

});



let host = 'http://127.0.0.1:8000/'
let request = new Request(host,{
    method:'POST',
});



let observer = new IntersectionObserver(entries=>{
    let entry = entries[0];

    if(entry.isIntersecting){
        fetch(request)
        .then(response=>{
            return response.json();
        }).then(data=>{
            // console.log('adding');

            let totalHtml = '';

            data['data'].forEach((book)=>{
                
                let html = `
                    <a class = link href="/book/info/${book.id}">
                        <div class="book">
                            <div class="book_left">
                                <img src="${book.image}">
                            </div>

                            <div class="book_right">
                                <p class="title">${book.title}</p>
                                <p class="author">${book.author}</p>
                                <p class="genre">${book.genre}</p>
                                <p class="rating">${book.rating}/10</p>
                            </div>
                        </div>
                    </a>
                `;
            
                totalHtml = totalHtml + html;
                
            });
            
            bookContainer.insertAdjacentHTML('beforeend', totalHtml);
            observer.observe(bookContainer.lastElementChild)


        })
        .catch(error=>{
            console.error(error);
        })

        observer.unobserve(entry.target);
    }

},{
    root:null,
    rootMargin:"150px",
});

observer.observe(bookContainer.lastElementChild);