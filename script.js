for (let i=1;i<=25;i++){
    const btn = document.getElementById("b"+String(i))
    btn.addEventListener("click", ()=>{
        const a = document.getElementById("b"+String(i))
        const isPressed = a.getAttribute("aria-pressed") === true;
        a.setAttribute("aria-pressed", !isPressed);
        if(!isPressed){a.setAttribute("style", "background-color:#FFCB05");}
        if(isPressed){a.setAttribute("style", "background-color:#FFFFFF");}
    })
}
