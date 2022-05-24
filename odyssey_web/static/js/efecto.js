$(document).ready(function () {
    
    $('#presentacion1_R').show();

    $('#presentacion1_L').hide();

    $('#btnInvertir').click(function () {
        $('#presentacion1_L').show();
        $('#presentacion1_R').hide();
    })
})