    //등록버튼
    document.getElementById("regbtn").onclick = function(){

        var allergy_length=document.getElementsByName("allergy_check").length;
        var allergy_arr=[];
        var j=0;

        //알레르기 요소가 선택됐을 시 (체크박스가 선택됐을 시), 선택된 알레르기(체크박스)의 value 값을 배열에 저장
        for(var i=0; i<allergy_length; i++){
            if(document.getElementsByName("allergy_check")[i].checked==true){
                allergy_arr[j]=document.getElementsByName("allergy_check")[i].value;
                j++
            }
        }

        //배열데이터를 menuUpload의 allergylist 로 전달해주기
        window.opener.document.getElementById("allergylist").value = allergy_arr;
        
        //선택된 알레르기의 개수가 0개가 아니면, menuUpload 의 알레르기 체크박스를 선택된 상태로 유지시키기
        if(j!=0){
            window.addEventListener('unload', function(event) {
            this.window.opener.document.getElementById("allergy").checked = true;});
        }

        window.close();
    }

    //취소버튼
    document.getElementById("xbtn").onclick = function(){
        window.close();
    }