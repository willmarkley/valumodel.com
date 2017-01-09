// JavaScript to check user input

function checkInput(inElement){
 	if( isNaN(inElement.value) ){
 		inElement.style.backgroundColor = "red";
 	}
}


function checkForm(id){
	var formElement = document..getElementById(id);
	var i;
	for(i = 0; i < formElement.length; i++){
		checkInput(formElement.elements[i])
	}
}
