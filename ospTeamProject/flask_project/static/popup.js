//등록버튼
document.getElementById("regbtn").onclick = function () {

    var allergy_length = document.getElementsByName("allergy_check").length;
    var allergy_arr = [];
    var j = 0;

    //알레르기 요소가 선택됐을 시 (체크박스가 선택됐을 시), 선택된 알레르기(체크박스)의 value 값을 배열에 저장
    for (var i = 0; i < allergy_length; i++) {
        if (document.getElementsByName("allergy_check")[i].checked == true) {
            allergy_arr[j] = document.getElementsByName("allergy_check")[i].value;
            j++
        }
    }

    //배열데이터를 menuUpload의 allergylist 로 전달해주기
    window.opener.document.getElementsByClassName("allergylist").value = allergy_arr;

    //선택된 알레르기의 개수가 0개가 아니면, menuUpload 의 알레르기 체크박스를 선택된 상태로 유지시키기
    if (j != 0) {
        window.addEventListener('unload', function (event) {
            this.window.opener.document.getElementsByClassName("allergy").checked = true;
        });
    }

    window.close();
}

//초기화버튼
document.getElementsByClassName("xbtn").onclick = function () {

    //초기화 버튼을 누를 시, allergylist 의 value가 초기화됨
    window.opener.document.getElementsByClassName("allergylist").value="";

    //초기화 버튼을 누를 시, menuUpload.html의 allergy 체크박스 선택이 해제됨
    window.addEventListener('unload', function (event) {
        this.window.opener.document.getElementsByClassName("allergy").checked = false;
    });
    
    //팝업창을 닫음
    window.close();
}