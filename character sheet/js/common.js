/**
 * radio 可单选可点击取消选中
 * link:https://blog.csdn.net/wangjun5159/article/details/52179847
 */
$(document).ready(function () {
    /*鼠标点击下去的时候，决定是否选中*/
    $("input:radio").bind("mousedown", function (event) {
        var radioChecked = $(this).prop("checked");
        $(this).prop('checked', !radioChecked);
        return false;
    });

    /*阻止click事件默认行为*/
    $("input:radio").click(function (event) {
        return false;
    });
});