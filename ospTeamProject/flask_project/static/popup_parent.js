var popup;

function allergyPopup() {
    var url = "/allergycheck";

    var name = 'allergy check';

    var width = 600;
    var height = 600;

    var left = (window.screen.width / 2) - (width / 2);

    var windowStatus = 'width=' + width + ',height=' + height + ',left=' + left + ',top=500,scrollbars=yes,status=no,resizable=no,menubar=no,toolbars=no,location=no';

    popup = window.open(url, name, windowStatus);

    /*팝업창에서 아무 행동도 하지 않고 그냥 닫을 시 menuUpload 창의 알레르기 체크박스 선택이 해제된다.*/
    popup.addEventListener('unload', function () {
        document.getElementById("allergy").checked = false;
    })

}

