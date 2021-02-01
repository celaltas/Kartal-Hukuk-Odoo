const btnScrollToTop = document.querySelector("#ScrollToTop");
const contactButton = document.querySelector("#contactFormButton")
var button = document.querySelector("#contactForm button");


button.addEventListener("click", function(){

    alert("Mesajınız alınmıştır");


})
contactButton.addEventListener("click",function(){
    document.querySelector(".bg-modal").style.display="flex";

});
document.querySelector(".fa-close").addEventListener("click",function(){
    document.querySelector(".bg-modal").style.display="none";



});



function upTo(){

    window.scrollTo({
        top:0,
        left:0,
        behavior:"smooth"
    });



};

btnScrollToTop.addEventListener("click",upTo)



var currentLocation = window.location;
var arr = currentLocation.pathname.split("/");
console.log(arr)


if (arr[1]=="Kadromuz"){
    document.querySelector(".dropTeam").style.display="none";


}
else if (arr[1].includes("Faaliyet")){
    document.querySelector(".dropActivities").style.display="none";



}

else if (arr[1].includes("Bilgi")){
    console.log("smdlkjaslkdjalksd")



}
/*
else if (arr[1].includes("leti")){
    contactButton.style.pointerEvents = "none";


}


*/









