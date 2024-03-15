"use strict";

let search = document.querySelector('.index_search_button');
let term = document.querySelector('.index_search_input');


search.addEventListener('click',function(){

    if(term.value.replace(/ /g,"") != ""){
        window.location.href = "/book/search/title/" + term.value;
    }

});