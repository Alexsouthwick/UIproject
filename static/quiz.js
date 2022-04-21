$(document).ready(function(){
    $("#continue").hide()
    $("#answers").empty();
    console.log(question["answers"])
    $.each(question["answers"], function(i, value){
        let new_answer= $("<div><button type='submit' class='answer' id='" + i + "' value='" + value + "'>" + value + "</button></div>");
        $("#answers").append(new_answer);
    })


    $(".answer").click(function(event){
        id = event.target.id
        let correctness = "false"
        value = $("#" + id).attr("value")
        if(value == question["correct"]){
            correct(id)
            correctness = "true"
        }
        else{
            incorrect(id)
        }
        console.log("out of if statment")
        answer_to_save = {"correct": correctness,"id": $("#question_num").html()}
        console.log(id)
        $.ajax({
            type: "POST",
            url: "update_score",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(answer_to_save),
            success: function(result){
                let total_score = result["total_score"]
                console.log(total_score)
                $("#total_score").html(total_score)
                
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request);
                console.log(status);
                console.log(error);
            }
        });
    })

    $("#continue").click(function(){
        next = question["next"];
        if (next == '0'){
            window.location.href = "/quiz/end";
        }
        else{
            window.location.href = "/quiz/" + next;
        }
    })
});

function correct(id){
    $("#info").empty();
    $("#continue").show();
    info = question["info"][id]
    let new_info= $("<p class='correct-info'>" + info + "</p>");
    $("#info").append(new_info);
}

function incorrect(id){
    $("#info").empty();
    info = question["info"][id];
    let new_info= $("<p class='incorrect-info'>" + info + "</p>");
    $("#info").append(new_info);
}