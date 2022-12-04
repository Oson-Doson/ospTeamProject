$(document).ready(function () {

    $('.typeButton').click(function () {
        //var tab_id = $(this).attr('data-tab');

        $('.typeButton').removeClass('current');
        //$('.tab-content').removeClass('current');
        
        $(this).addClass('current');
        //$("#" + tab_id).addClass('current');
        
    })

    //우측 화살표 클릭 이벤트
    $('#next-slick-arrow').click(function () {
        if ($('.typeButton.current').attr('data-tab') == 'tab-1') {

            var tab__id = $('#tab-1 .current').attr('id');
            $('#tab-1 .current').removeClass('current');
            switch (tab__id) {
                case "tab-1-1":
                    $('#tab-1-2').addClass('current');
                    break;
                case "tab-1-2":
                    $('#tab-1-1').addClass('current');
                    break;
            }

        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-2') {
            var tab__id = $('#tab-2 .current').attr('id');
            $('#tab-2 .current').removeClass('current');
            switch (tab__id) {
                case "tab-2-1":
                    $('#tab-2-2').addClass('current');
                    break;
                case "tab-2-2":
                    $('#tab-2-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-3') {
            var tab__id = $('#tab-3 .current').attr('id');
            $('#tab-3 .current').removeClass('current');
            switch (tab__id) {
                case "tab-3-1":
                    $('#tab-3-2').addClass('current');
                    break;
                case "tab-3-2":
                    $('#tab-3-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-4') {
            var tab__id = $('#tab-4 .current').attr('id');
            $('#tab-4 .current').removeClass('current');
            switch (tab__id) {
                case "tab-4-1":
                    $('#tab-4-2').addClass('current');
                    break;
                case "tab-4-2":
                    $('#tab-4-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-5') {
            var tab__id = $('#tab-5 .current').attr('id');
            $('#tab-5 .current').removeClass('current');
            switch (tab__id) {
                case "tab-5-1":
                    $('#tab-5-2').addClass('current');
                    break;
                case "tab-5-2":
                    $('#tab-5-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-6') {
            var tab__id = $('#tab-6 .current').attr('id');
            $('#tab-6 .current').removeClass('current');
            switch (tab__id) {
                case "tab-6-1":
                    $('#tab-6-2').addClass('current');
                    break;
                case "tab-6-2":
                    $('#tab-6-1').addClass('current');
                    break;
            }
        }
    })

    //좌측 화살표 클릭 이벤트
    $('#prev-slick-arrow').click(function () {

        if ($('.typeButton.current').attr('data-tab') == 'tab-1') {

            var tab__id = $('#tab-1 .current').attr('id');
            $('#tab-1 .current').removeClass('current');
            switch (tab__id) {
                case "tab-1-1":
                    $('#tab-1-2').addClass('current');
                    break;
                case "tab-1-2":
                    $('#tab-1-1').addClass('current');
                    break;
            }

        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-2') {
            var tab__id = $('#tab-2 .current').attr('id');
            $('#tab-2 .current').removeClass('current');
            switch (tab__id) {
                case "tab-2-1":
                    $('#tab-2-2').addClass('current');
                    break;
                case "tab-2-2":
                    $('#tab-2-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-3') {
            var tab__id = $('#tab-3 .current').attr('id');
            $('#tab-3 .current').removeClass('current');
            switch (tab__id) {
                case "tab-3-1":
                    $('#tab-3-2').addClass('current');
                    break;
                case "tab-3-2":
                    $('#tab-3-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-4') {
            var tab__id = $('#tab-4 .current').attr('id');
            $('#tab-4 .current').removeClass('current');
            switch (tab__id) {
                case "tab-4-1":
                    $('#tab-4-2').addClass('current');
                    break;
                case "tab-4-2":
                    $('#tab-4-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-5') {
            var tab__id = $('#tab-5 .current').attr('id');
            $('#tab-5 .current').removeClass('current');
            switch (tab__id) {
                case "tab-5-1":
                    $('#tab-5-2').addClass('current');
                    break;
                case "tab-5-2":
                    $('#tab-5-1').addClass('current');
                    break;
            }
        }
        else if ($('.typeButton.current').attr('data-tab') == 'tab-6') {
            var tab__id = $('#tab-6 .current').attr('id');
            $('#tab-6 .current').removeClass('current');
            switch (tab__id) {
                case "tab-6-1":
                    $('#tab-6-2').addClass('current');
                    break;
                case "tab-6-2":
                    $('#tab-6-1').addClass('current');
                    break;
            }
        }
    })

    $('.sreviewTextFix').slick({
        autoplay: true,
        arrows: false
    })
    $('.breviewTextFix').slick({
        autoplay: true,
        arrows: false
    })
    $('.greviewTextFix').slick({
        autoplay: true,
        arrows: false
    })
*/

})