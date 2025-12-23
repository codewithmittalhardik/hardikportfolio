
const checkbox = document.getElementById('check');
const links = document.querySelectorAll('.navbar a');

const mybutton = document.getElementById("scrollTopBtn");

links.forEach(link => {
    link.addEventListener('click', () => {
        checkbox.checked = false;
    });
});

window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        mybutton.style.display = "flex";
    } else {
        mybutton.style.display = "none";
    }
}
mybutton.addEventListener("click", function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});