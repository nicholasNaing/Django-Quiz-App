let question_container = document.getElementById('quiz_info');
let quiz_type = question_container.getAttribute('data-quiz-type');
const currentPage = parseInt(question_container.getAttribute('data-current-page'));
const total_page = parseInt(question_container.getAttribute('data-total-quizes'));

function showalert(message,alert_type){
    let alert_data = '<div class="alert alert-'+alert_type+'">'+message+'</div>';
    document.getElementById('alert_message').innerHTML=alert_data;
};
function next_page(){
    const nextPage = currentPage + 1;
    window.location.href = '?page=' + nextPage;
}
function check_ans(ans, correct_ans) {
    let correct_ans_num = parseInt(localStorage.getItem('correct_ans_num') || 0);
    const correct_answer = correct_ans;

    if (total_page > currentPage) {
        if (ans === correct_answer) {
            correct_ans_num++;
            localStorage.setItem('correct_ans_num', correct_ans_num);
            showalert('You are correct.', 'success');
            $(".custom-button").each(function(index,element){
                $(".custom-button").slideUp(600);
                $("#question").fadeOut(600);
                $("#quit").slideUp(600);
            });
            setTimeout(next_page, 600);
        } else {
            showalert('Wrong. The correct answer is ' + correct_answer + '.', 'danger');
            $(".custom-button").each(function(index,element){
                $(".custom-button").slideUp(600);
                $("#question").fadeOut(600);
                $("#quit").slideUp(600);
            });
            setTimeout(next_page, 600);
        }
    } else {
        localStorage.setItem('total_quiz',total_page);
        if (ans === correct_answer) {
            correct_ans_num++;
            localStorage.setItem('correct_ans_num', correct_ans_num);
            showalert('You are correct.', 'success');
            $(".custom-button").each(function(index,element){
                $(".custom-button").slideUp(600);
                $("#question").fadeOut(600);
                $("#quit").slideUp(600);
            });
            setTimeout(function(){
                window.location.href = quiz_type+'finished/';
            },500);
            correct_ans_num = localStorage.getItem('correct_ans_num');
            let score = document.getElementById('show-score');
            score.innerHTML = 'You answered '+correct_ans_num+' question out of {{ total_quizes }}questions correctly.';
        } else {
            showalert('Wrong. The correct answer is ' + correct_answer + '.', 'danger');
            $(".custom-button").each(function(index,element){
                $(".custom-button").slideUp(600);
                $("#question").fadeOut(600);
                $("#quit").slideUp(600);
            });
            setTimeout(function(){
                window.location.href = quiz_type+'finished/';
            } ,500);
        }
    };
}
function finished(){
    localStorage.clear();
    window.location.href = 'http://127.0.0.1:8000/category/'
}
function quit(){
    localStorage.clear();
    $("#quit").fadeOut(600);
    $(".custom-button").each(function(index,element){
        $(".custom-button").fadeOut(600);
        $("#question").fadeOut(600);
    });
    setTimeout(function(){
        window.location.href = 'http://127.0.0.1:8000/category/';
    },700);
}
if(window.location.href == 'http://127.0.0.1:8000/'+quiz_type+'finished/'){
    correct_ans_num = localStorage.getItem('correct_ans_num');
    total_quiz = localStorage.getItem('total_quiz');
    let score = document.getElementById('show-score');
    if (total_quiz>=correct_ans_num){
        score.innerHTML = 'You answered '+correct_ans_num+' questions correctly out of '+total_quiz+' questions.';
    } else{
        score.innerHTML = 'Cannot calculate the scores as you have tried to select more than one time!';
    }
};
if(window.location.href == 'http://127.0.0.1:8000/'+quiz_type+'intro/'){
    localStorage.clear();
}
