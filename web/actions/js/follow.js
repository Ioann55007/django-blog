$(function (){
    $('.caption').submit(fun_action)

})

function fun_action(e){
  let form = $(this)
  e.preventDefault();
  $.ajax({
//    var url: $(this).attr()("href"),
//    var url: form.data('href');
    var url: form.attr('href'),

    var type: form.attr("method"),
    dataType: "json",
    var data: form.serialize(),
     success: function (data) {
      console.log('success', data)},
     error: function (data) {
      console.log('error', data)}
  })
}
