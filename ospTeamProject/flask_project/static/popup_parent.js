var popup;

document.getElementById("allergy").onclick = function(){
    var url = "/allergycheck";

    var name = 'allergy check';

    var width = 600;
    var height = 600;

    var left = (window.screen.width / 2) - (width / 2);

    var windowStatus = 'width=' + width + ',height=' + height + ',left=' + left + ',top=500,scrollbars=yes,status=no,resizable=no,menubar=no,toolbars=no,location=no';

    popup = window.open(url, name, windowStatus);

    /*allergylist의 값이 비어있지 않을 시, 팝업창을 닫아도 menuUpload.html의 allergy 체크박스 선택이 유지되도록 설정*/
    if(document.getElementById("allergylist").value!=""){
        popup.addEventListener('unload', function () {
            document.getElementById("allergy").checked = true;
    })}
    //allergylist에 아무것도 들어있지 않을 때 팝업창을 닫으면 menuUpload.html의 allergy 체크박스 선택이 해제되도록 설정
    else{
        popup.addEventListener('unload', function () {
            document.getElementById("allergy").checked = false;
    })
    }

}

