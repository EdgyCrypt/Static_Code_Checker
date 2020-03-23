
function populateTextFromFile () {
    var file = document.getElementById('studentCodeFile').files[0];

    file.addEventListener('change', () => {
        var reader = new FileReader();
        reader.onload = function (e) {
            var textArea = document.getElementById('studentTextArea');
            textArea.value = e.target.result;
        };
        reader.readAsText(file);
    });
    
}