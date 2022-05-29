// get the modal
var modal = document.getElementById("myModal");

//get the trigger

var trigger = document.getElementById("trigger");

//get the button element that closes the modal
var btn = document.getElementsByClassName("close")[0];

//when the user clicks on the image/button, open the modal
trigger.onclick = function(){
    modal.style.display = 'block';

}

//when the user clicks on the button (x), close the modal
btn.onclick = function(){
    modal.style.display = 'none';

}

//when the user clicks anywhere outside of the modal, close it
window.onclick = function(event){
    if(event.target == modal){
        modal.style.display = 'none';
    }
}