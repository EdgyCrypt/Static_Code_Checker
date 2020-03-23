
function populateTextFromFile () {
    var file = document.getElementById('intervieweeCodeFile').files[0];

    var reader = new FileReader();
    reader.onload = function (e) {
        var textArea = document.getElementById('intervieweeTextArea');
        textArea.value = e.target.result;
    };
    reader.readAsText(file);
}