$(document).ready(function(){
    $("#answers").empty();
    console.log(question["answers"])
    $.each(question["answers"], function(i, value){
        let new_answer= $("<div><button type='submit' class='answer'>" + value + "</button></div>")
        $("#answers").append(new_answer)
    })

    // $("#e_btn").click(function(){
    //     window.location.href = "/edit/" + show["id"];
    // })
})