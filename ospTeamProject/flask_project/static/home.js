$(document).ready(function(){
	
	$('.typeButton').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('.typeButton').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})  

    $('#next-slick-arrow').click(function(){
        if($('.typeButton.current').attr('data-tab')=='tab-1'){
            var $button=$('#typeKorean')
            var tab_id='tab-2';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-2'){
            var $button=$('#typeChinese')
            var tab_id='tab-3';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-3'){
            var $button=$('#typeJapanese')
            var tab_id='tab-4';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-4'){
            var $button=$('#typeWestern')
            var tab_id='tab-5';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-5'){
            var $button=$('#typeCafe')
            var tab_id='tab-6';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
    })

    $('#prev-slick-arrow').click(function(){
    
        if($('.typeButton.current').attr('data-tab')=='tab-2'){
            var $button=$('#typeTotal')
            var tab_id='tab-1';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-3'){
            var $button=$('#typeKorean')
            var tab_id='tab-2';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-4'){
            var $button=$('#typeChinese')
            var tab_id='tab-3';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-5'){
            var $button=$('#typeJapanese')
            var tab_id='tab-4';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
            $(this).style.display=none;
        }
        else if($('.typeButton.current').attr('data-tab')=='tab-6'){
            var $button=$('#typeWestern')
            var tab_id='tab-5';
            $('.typeButton').removeClass('current');
		    $('.tab-content').removeClass('current');

		    $button.addClass('current');
		    $("#"+tab_id).addClass('current');
            $(this).style.display=none;
        }
    })

    $('.sreviewTextFix').slick({
        autoplay:true,
        arrows:false
    })
    $('.breviewTextFix').slick({
        autoplay:true,
        arrows:false
    })
    $('.greviewTextFix').slick({
        autoplay:true,
        arrows:false
    })
})