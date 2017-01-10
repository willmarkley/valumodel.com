// JavaScript to check user input

function checkInput(inElement){
	//if( inElement.id != "NaN1" && inElement.id != "NaN2"){
		if( isNaN(inElement.value) ){
			inElement.style.backgroundColor = "#ff6666";
		}
	//}
}


function checkForm(){
	var formElement = document.getElementById("frm");
	var i;
	for(i = 0; i < formElement.length; i++){
		checkInput(formElement.elements[i])
	}
}
