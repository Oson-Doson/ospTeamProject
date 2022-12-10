$(document).ready(function () {

    $('.typeButton').click(function() {
        //var tab_id = $(this).attr('data-tab');

        $('.typeButton').removeClass('current');
        //$('.tab-content').removeClass('current');
        
        $(this).addClass('current');
        //$("#" + tab_id).addClass('current');
       
    }) 

    // 페이징 버튼 눌렀을떄도 색 고정되게끔 설정
    $('.page-nation a').click(function() {
        //var tab_id = $(this).attr('data-tab');

        $('.page-nation a').removeClass('current');
        //$('.tab-content').removeClass('current');
        
        $(this).addClass('current');
        //$("#" + tab_id).addClass('current');
       
    }) 

    type=$('#cate_color').attr('data-cate');
    if(type=='한식'){
        $('.typeButton').removeClass('current');
        $('#typeKorean').addClass('current');
    }
    else if(type=='중식'){
        $('.typeButton').removeClass('current');
        $('#typeChinese').addClass('current');
    }
    else if(type=='일식'){
        $('.typeButton').removeClass('current');
        $('#typeJapanese').addClass('current');
    }
    else if(type=='양식'){
        $('.typeButton').removeClass('current');
        $('#typeWestern').addClass('current');
    }
    else if(type=='카페'){
        $('.typeButton').removeClass('current');
        $('#typeCafe').addClass('current');
    }
})

//$('.page-nation a').attr('id', this.)