$(document).ready(
    function() {

$(document).on('click', '.createLink', function(event){
    $('.modal').modal('show');

    $.get(this.href, function(data){
        $('.modal-body').html(data);
    });
    $('.modal').on('shown.bs.modal', function () {
        $('.chosen-select', this).chosen();
    });
    event.preventDefault();
});

$(document).on('click', '.editLink', function(event){
    $('.modal').modal('show');

    $.get(this.href, function(data){
        $('.modal-body').html(data);
    });
    $('.modal').on('shown.bs.modal', function () {
        $('.chosen-select', this).chosen();
    });
    event.preventDefault();
});


$(document).on('click', 'button.ajaxlike', function(event) {
        var data = $(this).data();
        var likesSpan = $('#likes');
        $.ajax({url: document.URL + 'like/', method: 'post'}).done(function(data){likesSpan.html("Количество лайков: " + data);})
    });


        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });
    }
);