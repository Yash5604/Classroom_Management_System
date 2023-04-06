const body = document.querySelector("body"),
    nav = document.querySelector("nav"),
    sidebarOpen = document.querySelector(".sidebarOpen"),
    sidebarClose = document.querySelector(".sidebarClose");

sidebarOpen.addEventListener("click", ()=>{
    nav.classList.add("active");
    sidebarClose.classList.toggle("active");
    sidebarOpen.classList.remove("active");
});

sidebarClose.addEventListener("click", e=>{
    let clickedelm = e.target;
    if(!clickedelm.classList.contains("sidebarOpen") && !clickedelm.classList.contains("menu")){
        nav.classList.remove("active");
    }
});

function fun() {
    const plus = document.querySelector(".plus");
    const cjbtn = document.querySelector(".cjbtn");
    plus.addEventListener("click", ()=>{
        cjbtn.classList.add("active");
    });
    document.addEventListener("click", (event) => {
        const isClickInsidePlus = plus.contains(event.target);
        const isClickInsideCjbtn = cjbtn.contains(event.target);
        if (!isClickInsidePlus && !isClickInsideCjbtn) {
            cjbtn.classList.remove("active");
        }
    });
}

fun();