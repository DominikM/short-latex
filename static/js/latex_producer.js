var latex_box;
var latex_display;

latex_box = document.getElementById("latex_input");

function update_latex() {
    latex_display = MathJax.Hub.getAllJax("latex_display")[0];
    latex = latex_box.value;
    MathJax.Hub.Queue(["Text", latex_display, latex]);
}

function save_latex() {
    latex_text = latex_box.value;
    
    $.post(
	page_data.save_url,
	{latex_text: latex_text},
	function (data) {
	    if (data.result == 'success') {
		var url_cont = document.getElementById('latex_url_container');
		
		var url_p = document.createElement('p');
		var url_input = document.createElement('input');

		url_p.innerHTML = 'The url for this latex is: ';

		url_input.value = data.latex_url;
		url_input.readOnly = true;

		url_cont.appendChild(url_p);
		url_cont.appendChild(url_input);
	    }
	}
    );
}


		
	
    
    
