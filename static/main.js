$(document).ready(function() {

    $('html').removeClass('no-js').addClass('js');

    $('#photos img').hover(function() {
        var full = $(this).parent().attr('href');
        $('#photo-overlay')
            .css('background-image', 'url("' + full + '")')
            .addClass('visible');
    }, function() {
        $('#photo-overlay')
            .removeClass('visible');
    });

});
