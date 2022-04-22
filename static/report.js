$(document).ready(function(){
    $("#next").click(function(){
        next = module["next"]
        if (next == '0'){
            window.location.href = "/learning/end"
        }
        else{
            window.location.href = "/learning/" + next
        }
    });
})