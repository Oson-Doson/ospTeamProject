$(document).ready(function () {

    $('.typeButton').click(function() {
        //var tab_id = $(this).attr('data-tab');

        $('.typeButton').removeClass('current');
        //$('.tab-content').removeClass('current');
        
        $(this).addClass('current');
        //$("#" + tab_id).addClass('current');
       
    }) 

    type=$('#cate_color').attr('data-cate');
    if(type=='한식'){
        $('.typeButton').removeClass('current');
        $('#typeKorean').addClass('current');
    }
})

//$('.page-nation a').attr('id', this.)