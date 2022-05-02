const messages = document.querySelector('.messages');


$('#toggle-menu').click(function(){
    $(this).next().slideToggle();
})

$(window).on('resize', function(){
    var width = $(window).width();

    console.log("width",width)

    if (width>768){
        $('nav').css('display', 'block')
    }

})


//temporizador del message
//$(document).ready(function() {
    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.messages').attr('style', 'display:none;');
    }, 3000); 
