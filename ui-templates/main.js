
// Geolocate

var x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}

//Custom File Input

var realFilebtn = document.getElementById("real-file");
var customButton = document.getElementById('custom-button');

customButton.addEventListener('click', function() {
    realFilebtn.click();
});

var realFilebtn2 = document.getElementById("real-file2");
var customButton2 = document.getElementById('custom-button2');

customButton2.addEventListener('click', function() {
    realFilebtn2.click();
});

// CREATING MODAL WINDOW FOR USER INCIDENT CREATIONS

// Get Modal Element
var modal = document.getElementById('createRecord');

// Get Open Modal Button
var createmodal  = document.getElementById('createModal');

//Get close button
var closebtn = document.getElementsByClassName('closeModal')[0];

//Listen for open click
createmodal.addEventListener('click', openModal);

//Listen for close click
closebtn.addEventListener('click', closeModal);

// Lister for Outside click
window.addEventListener('click', outsideClick);

//Function to open Modal
function openModal(){
    modal.style.display='block';
}

//Function to close Modal
function closeModal(){
    modal.style.display='none';
}

//Function to close Modal if Outside the click
function outsideClick(e) {
    if(e.target == modal) {
        modal.style.display='none';
    }
    
}

// CREATING MODAL WINDOW FOR VIEWING RECORD

// Get Modal Element
var modal2 = document.getElementById('createRecord2');

// Get Open Modal Button
var createmodal2  = document.getElementById('createModal2');

//Get close button
var closebtn2 = document.getElementsByClassName('closeModal2')[0];

//Listen for open click
createmodal2.addEventListener('click', openModal2);

//Listen for close click
closebtn2.addEventListener('click', closeModal2);

//Function to open Modal
function openModal2(){
    modal2.style.display='block';
}

//Function to close Modal
function closeModal2(){
    modal2.style.display='none';
}


