$(document).ready(function(){
    $("#continue").click(function(){
        next = module["next"]
        console.log(next)
        window.location.href = "/report/" + module["id"]
    });

    $("#takeQuizBtn").click(function() {
        window.location.href = "/quiz/start"
    });
})