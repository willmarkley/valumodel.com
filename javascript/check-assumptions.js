// JavaScript to check user input

function checkInput(inElement){
 	if( isNaN(inElement.value) ){
 		inElement.style.backgroundColor = "red";
 	}
}


function checkForm(){
	var formElement = document.getElementById("frm");
	var i;
	for(i = 0; i < formElement.length; i++){
		checkInput(formElement.elements[i])
	}
}
