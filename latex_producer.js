var latex_box;
var latex_display;

latex_box = document.getElementById("latex_input");

function update_latex() {
    latex_display = MathJax.Hub.getAllJax("latex_display")[0];
    latex = latex_box.value;
    MathJax.Hub.Queue(["Text", latex_display, latex]);
}
    
    
