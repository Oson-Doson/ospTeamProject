$(document).ready(function(){
	
	$('.typeButton').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('.typeButton').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})

})