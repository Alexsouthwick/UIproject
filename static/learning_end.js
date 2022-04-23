$(document).ready(function(){
    console.log(reports)
    let let_report = reports["1"]
    let bre_report = reports["2"]
    let sky_report = reports["3"]
    let fin_report = reports["4"]
    for(let k in reports){
        let report = reports[k]
        let new_feel = ""
        if (report["feelings"] < 0 && report["feelings"] > -5){
            new_feel = "Slightly Agitated"
        }
        else if(report["feelings"] > 0 && report["feelings"] < 5){
            new_feel = "Slightly Relaxed"
        }
        else if(report["feelings"] == 0){
            new_feel = "The Same"
        }
        else if(report["feelings"] == -5){
            new_feel = "Agitated"
        }
        else if(report["feelings"] == 5){
            new_feel = "Relaxed"
        }
        let new_breath = report["breathing"].toString()
        let new_body = report["body"].toString()
        let new_thoughts = report["thoughts"].toString()
        let new_notes = report["notes"]
        if (k == "1"){
            $("#let_feel").append(new_feel)
            $("#let_bre").append(new_breath)
            $("#let_bod").append(new_body)
            $("#let_tho").append(new_thoughts)
            $("#let_notes").append(new_notes)
        }
        if (k == "2"){
            $("#bre_feel").append(new_feel)
            $("#bre_bre").append(new_breath)
            $("#bre_bod").append(new_body)
            $("#bre_tho").append(new_thoughts)
            $("#bre_notes").append(new_notes)
        }
        if (k == "3"){
            $("#sky_feel").append(new_feel)
            $("#sky_bre").append(new_breath)
            $("#sky_bod").append(new_body)
            $("#sky_tho").append(new_thoughts)
            $("#sky_notes").append(new_notes)
        }
        if (k == "4"){
            $("#fin_feel").append(new_feel)
            $("#fin_bre").append(new_breath)
            $("#fin_bod").append(new_body)
            $("#fin_tho").append(new_thoughts)
            $("#fin_notes").append(new_notes)
        }
        
    }

    $("#takeQuizBtn").click(function() {
        window.location.href = "/quiz/start"
    });
})