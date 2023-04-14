var DELETE_ID;
var EDIT_ID;
$(function(){
    bindBtnAddEvent();
    bindBtnSaveEvent();
    bindBtnDeleteEvent();
    bindBtnConfirmDeleteEvent();
    bindBtnEditEvent();

})

function bindBtnAddEvent(){
    $("#btnAdd").click(function(){
        // 将正在编辑的ID设置为空
        EDIT_ID = undefined;
        // 清空对话框中的数据
        $("#formAdd")[0].reset();
        // 修改对话框的标题
        $("#myModalLabel").text("新建");
        // 点击新建按钮，显示对话框
        $('#myModal').modal('show');

    });


}

function bindBtnSaveEvent(){
    $("#btnSave").click(function(){
        // 清除错误信息
        $(".error-msg").empty();
        if(EDIT_ID){
            //编辑
            doEdit();
        }else{
            //添加
            doAdd();
        }

    });
}

function doAdd(){
    console.log($("#formAdd").serialize());
    // 向后台发送请求
    $.ajax({
            url: "/order/add/",
            type: "post",
            data:$("#formAdd").serialize(),
            dataType:"JSON",
            success:function(res){
                if(res.status){
                    alert("创建成功111111");
                    // 清空表单
                    $("#formAdd")[0].reset();
                    //关闭对话框
                    $("#myModal").modal('hide');

                    // 刷新页面
                    location.reload();
                }else{
                    $.each(res.error,function(name,errorList){
                            $("#id_"+name).next().text(errorList[0]);
                    });
                }
            },


        });
}

function doEdit(){
    // 向后台发送请求
    $.ajax({
            url: "/order/edit/" + "?uid=" + EDIT_ID,
            type: "post",
            data:$("#formAdd").serialize(),
            dataType:"JSON",
            success:function(res){
                if(res.status){
                    // 清空表单
                    $("#formAdd")[0].reset();

                    //关闭对话框
                    $("#myModal").modal('hide');

                    // 刷新页面
                    location.reload();
                }else{
                    if(res.tips){
                        alert(res.tips);
                    }else{
                        $.each(res.error,function(name,errorList){
                            $("#id_"+name).next().text(errorList[0]);
                        });
                    }
                }
            },


        });

}


function bindBtnDeleteEvent(){
    $(".btn-delete").click(function(){
        // 点击删除，显示对话框
        $('#deleteModal').modal('show');

        // 获取当前行的ID并赋值给全局变量
        DELETE_ID = $(this).attr("uid");

    });

}

function bindBtnConfirmDeleteEvent(){
$("#btnConfirmDelete").click(function(){
        // 点击确认删除按钮，将全局变量中设置的那个要删除ID发送到后台
    $.ajax({
        url: "/order/delete/",
        type: "GET",
        data: {
            uid: DELETE_ID,
        },
        dataType: "JSON",
        success: function(res){
            if(res.status){
                // alert("删除成功")

                // 隐藏删除框
                //$("#deleteModal").modal('hide');

                // 在页面上将当前一行数据删除（js）
               // $("tr[uid='" + DELETE_ID + "']").remove();

                // 要删除的ID置空
               // DELETE_ID = 0;

               location.reload();

            }else{
                // 删除失败
                alert(res.error);
            }
        }
    });

});

}

function bindBtnEditEvent(){
    $(".btn-edit").click(function(){
        // 清空对话框中的数据
        $("#formAdd")[0].reset();

        var uid = $(this).attr("uid");
        EDIT_ID = uid;
        // 发送Ajax去后端获取当前行的相关数据
        $.ajax({
            url:"/order/detail/",
            type:"get",
            data:{
                uid:uid
            },
            dataType:"JSON",
            success:function(res){
                 if(res.status){
                    console.log(res.data)
                    // 将数据赋值到对话框中的标签中
                    $.each(res.data,function(name,value){
                        $("#id_" + name).val(value);
                    });
                    // 修改对话框的标题
                    $("#myModalLabel").text("编辑");
                    // 点击新建按钮，显示对话框
                    $('#myModal').modal('show');

                 }else{
                    alert(res.error);
                 }
            }

        });
    });


}