$(document).ready(function(){
    let report = {"id": module["id"]}
    report["feelings"] = 0
    report["notes"] = ""
    report["breathing"] = 'No'
    report["body"] = 'No'
    report["thoughts"] = 'No'
    $("#next").click(function(){
        next = module["next"]
        let notes = $("#notes_box").val()
        report["notes"] = notes
        if (next == '0'){
            let new_link = "/learning/end"
            $("#next_lession").attr("href",new_link)
        }
        $.ajax({
            type: "POST",
            url: "submit",                
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(report),
            success: function(result){
                console.log("next lession")
                return None
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request);
                console.log(status);
                console.log(error);
            }
        });
        
    });
    $("#breathing").click(function(){
        console.log($("#breathing").is(':checked'))
        console.log(module["id"]) 
        // report["breathing"] = $("#breathing").is(':checked')
        console.log(report["breathing"]);
        report["breathing"] = 'Yes';
    })
    $("#body").click(function(){
        // report["body"] = $("#body").is(':checked')
        report["body"] = 'Yes';

    })
    $("#thoughts").click(function(){
        // report["thoughts"] = $("#thoughts").is(':checked')
        report["thoughts"] = 'Yes';
    })
    $("#feeling_scale").click(function () {
        console.log("feelings")
        console.log($("#feeling_scale").val())
        feelings =  $("#feeling_scale").val()
        report["feelings"] = feelings
        console.log(feelings)
    })
})