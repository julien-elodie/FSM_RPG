/**
 * radio 可单选可点击取消选中
 * link:https://blog.csdn.net/u011704894/article/details/46877869
 * 原文有误，已修改
 */
$(document).ready(function () {
    $("input:radio").click(function () {
        var domName = $(this).attr('name');
        var checkedState = $(this).attr('checked');
        $("input:radio[name='" + domName + "']").attr('checked', false);
        $(this).attr('checked', true);
        if (checkedState == 'checked') {
            $(this).attr('checked', false);
            $(this)[0].checked = false;
        }
    });
});