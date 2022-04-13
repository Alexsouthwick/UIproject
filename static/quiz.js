$(document).ready(function(){
    $("#continue").hide()
    $("#answers").empty();
    console.log(question["answers"])
    $.each(question["answers"], function(i, value){
        let new_answer= $("<div><button type='submit' class='answer' id='" + i + "' value='" + value + "'>" + value + "</button></div>")
        $("#answers").append(new_answer)
    })

    $(".answer").click(function(event){
        id = event.target.id
        value = $("#" + id).attr("value")
        if(value == question["correct"]){
            correct(id)
        }
        else{
            incorrect(id)
        }
    })
})

function correct(id){
    $("#info").empty()
    $("#continue").show()
    info = question["info"][id]
    let new_info= $("<div class'incorrectinfo'>" + info + "</div>")
    $("#info").append(new_info)
}

function incorrect(id){
    $("#info").empty()
    info = question["info"][id]
    let new_info= $("<div class'incorrectinfo'>" + info + "</div>")
    $("#info").append(new_info)

}