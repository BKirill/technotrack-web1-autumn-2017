function updateComments(){
    $.get(document.URL + 'comments/', function(data){
        $('#comments').replaceWith(data);
    });
}

setInterval(updateComments, 5000);