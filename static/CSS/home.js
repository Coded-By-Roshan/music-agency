    var humb = document.getElementById('humb');
    var nav = document.querySelector('.nav');
    humb.addEventListener('click',()=>{
        nav.classList.toggle("hide");
        humb.classList.toggle("bend");
    })
    window.addEventListener('scroll',()=>{
        if(window.scrollY > 20){
        nav.classList.add("sticky");
    }
    else{
        nav.classList.remove("sticky");
    }
   
    })
    