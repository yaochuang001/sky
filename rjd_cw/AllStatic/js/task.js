$(function(){

    bindBtn1Event();
    bindBtn2Event();
    bindBtn3Event();
    bindBtnAddEvent();
})

function bindBtn1Event(){
    $("#btn1").click(function(){
        $.ajax({
            url: '/task/ajax/',
            type: 'post',
            data: {
                n1: 123,
                n2: 345,
            },
            dataType:"JSON",
            success: function(res){
                console.log(res);
                console.log(res.status);
                console.log(res.data);
            }
        })

    })

}

function bindBtn2Event(){
    $("#btn2").click(function(){
        $.ajax({
            url: '/task/ajax/',
            type: 'post',
            data: {
                user: $("#txtUser").val(),
                age: $("#txtAge").val(),
            },
            dataType:"JSON",
            success: function(res){
                console.log(res);
                console.log(res.status);
                console.log(res.data);
            }
        })

    })

}

function bindBtn3Event(){
    $("#btn3").click(function(){
        $.ajax({
            url: '/task/ajax/',
            type: 'post',
            data:$("#form3").serialize(),
            dataType:"JSON",
            success: function(res){
                console.log(res);
                console.log(res.status);
                console.log(res.data);
            }
        })

    })

}

function bindBtnAddEvent(){
    $("#btnAdd").click(function(){

        $(".error-msg").text("");

        $.ajax({
            url: '/task/add/',
            type: 'post',
            data:$("#formAdd").serialize(),
            dataType:"JSON",
            success: function(res){
                if(res.status){
                    alert("添加成功");
                    location.reload();
                }else{
                    $.each(
                        res.error,
                        function(name,data){
                            $("#id_" + name).next().text(data[0]);
                        }
                    )
                }
            }
        })

    })

}

