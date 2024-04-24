<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
//change password

// Get the modal retrieves actual pop
//  var modal = document.getElementById("myModal");
// // Get the button that opens the modal  retireves button to open it
// var btn = document.getElementById("myBtn");
// // Get the <span> element that closes the modal x to close pop up
// var span = document.getElementsByClassName("close")[0];
        
// When the user clicks the button, open the modal popup appears on top of webpage
btn.onclick = function() {
    modal.style.display = "block";
}

// btn4.onclick = function() {
//     extra.style.display = "block";
// }

// span4.onclick = function() {
//     extra.style.display = "none";
// }
       
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    } else if (event.target == help) {
        help.style.display = "none";
    } else if (event.target == extra) {
        extra.style.display = "none";
    } else if (event.target == helprh) {
        helprh.style.dispay = "none";
    }
}
