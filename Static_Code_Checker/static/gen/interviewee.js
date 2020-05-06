
function populateTextFromFile () {
    //was supposed to populate text area with contents of file
    var file = document.getElementById('intervieweeCodeFile').files[0];

    var reader = new FileReader();
    reader.onload = function (e) {
        var textArea = document.getElementById('intervieweeTextArea');
        textArea.value = e.target.result;
    };
    reader.readAsText(file);
}

function navigatePages(int) {
//causing page changes
    if(int == 1) {
        window.location.href="/student";
    }
    else if (int == 2) {
        window.location.href="/teacher";
    }
    else if (int == 3) {
        window.location.href="/interviewer";
    }
    else if (int == 4) {
        window.location.href="/interviewee";
    }
    else if (int == 5) {
        window.location.href="/";
    }
}