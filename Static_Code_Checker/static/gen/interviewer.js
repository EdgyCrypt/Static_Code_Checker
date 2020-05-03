function goToInterviewee() {
    window.location.href="/interviewee";
}

function navigatePages(int) {

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