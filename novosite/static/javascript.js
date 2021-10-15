(function(win,doc){
    'use strict';
    //verificar se o usuario quer apagar o dado ou nao
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
               if(confirm('Deseja remover este dado?')){
                return true;
               } else {
                event.preventDefault();
               }
            });
        }
    }
})(window,document);