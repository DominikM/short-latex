var latex_box;
var latex_display;

latex_box = document.getElementById("latex_input");
latex_url_container = document.getElementById("latex_url_container");


function update_latex() {
    latex_display = MathJax.Hub.getAllJax("latex_display")[0];
    latex = latex_box.value;
    MathJax.Hub.Queue(["Text", latex_display, latex]);
}

function save_latex() {
    $.post(
	page_data.save_url,
	{latex_text: latex_box.value},
	function(data) {
	    if (data.result = "success") {
		latex_url_container.innerHTML = "";
		
		var url_p = document.createElement('p');
		var url_input = document.createElement('input');
		url_p.innerHTML = "The url of this latex is: ";
		url_input.readOnly = true;
		url_input.value = data.latex_url;
		url_input.style = "width: 100%";

		latex_url_container.appendChild(url_p);
		latex_url_container.appendChild(url_input);
	    }
	}
    )
}
		
	
    
    
