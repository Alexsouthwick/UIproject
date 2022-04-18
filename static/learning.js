$(document).ready(function(){
    $("#continue").click(function(){
        next = module["next"]
        console.log(next)
        if (next == '0'){
            window.location.href = "/learning/end"
        }
        else{
            window.location.href = "/learning/" + next
        }
    });

    $("#takeQuizBtn").click(function() {
        window.location.href = "/quiz/start"
    });
})