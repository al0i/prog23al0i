function listing(listZone){

var route = `http://localhost:5000/ranking`;
var action = $.ajax({
    url: route,
    dataType: 'json'
});
action.done(function(result){
    try{
        if(result.result == "ok"){
            for (var reg of result.details){
                var paragraph = $('<tr>');
                var s = '';
                for (zone of listZone){
                    var test = String(zone);
                    if (test.indexOf('.') !== -1){
                        var parts = test.split('.');
                        var value = reg[parts[0]][parts[1]];
                        if (value == undefined){
                            valor = "";
                        }
                        s = s + '<td>' + value + '</td>';
                    } else{
                        s = s + '<td>' + reg[zone] + '</td>';
                    }
                }
                paragraph.html(`${s}`);
                $('#players').append(paragraph);
            }
        } else {
            alert("Backend error: "+result.details);
        }
    } catch(error) {
        alert("Ajax error: "+error+"\nAnswer: "+result.details);
    }
});

action.fail(function(jqXHR, textStatus){
    msg = findError(jqXHR, textStatus, route);
    alert("Ajax error: "+msg);
});
function findError(jqXHR, textStatus, route){
    var msg = '';
    if (jqXHR.status === 0){
        msg = "Cannot connect. Verify if the backend address is correct and running";
    } else if(jqXHR.status == 404){
        msg = 'Cannot find the URL in server [404 error]' + route;
    } else if (textStatus === 'parsererror'){
        msg = 'Failed to decode json result'
    } else if(textStatus === 'timeout'){
        msg = 'Timeout';
    } else if (textStatus === 'abort'){
        msg = 'Aborted';
    } else {
        msg = 'Unknown error: '+jqXHR.responseText;
    }
    return msg;
}}