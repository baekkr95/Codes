$('#send').on('click', sendBubble);

function sendBubble() {
    if($('textarea').val() != '') {
        $('.chatbox').append('<div class="my-bubble bubble">' + $('textarea').val() + '</div>');
        $('textarea').val('');
    }
}
