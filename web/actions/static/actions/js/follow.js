$(function () {
 $('.followMe').click(followerApi)
});

function followerApi(){
let button = $(this)
console.log('click')
let data = {
'user_id': button.data('id')
}
//  this.innerHTML =
//      (this.innerHTML === 'Отписаться') ? this.innerHTML = 'Скрыть всё' : this.innerHTML = 'Отписаться';
$.ajax({
    url: button.data('href'),
    type: 'POST',
    dataType: "json",
    data: data,
     success: function (data) {
      console.log('success', data)},
     error: function (data) {
      console.log('error', data)}
  })

}


//const btn = document.querySelectorAll('.btn > span');
//for (let i = 0; i < btn.length; i++) {
//  btn[i].addEventListener('click', function fun_action(e) {
//
//    this.innerHTML =
//      (this.innerHTML === 'Отписаться') ? this.innerHTML = 'Скрыть всё' : this.innerHTML = 'Отписаться';
//  })
//}

//$.ajax({
//    url: form.(data: 'subscriber_to_user'),
//    type: form.attr("method"),
//    dataType: "json",
//    data: form.serialize(),
//     success: function (data) {
//      console.log('success', data)},
//     error: function (data) {
//      console.log('error', data)}
//  })


//}
//$(function () {
//  $('#followersButton').click(fun_prof);
//});
//
//function fun_prof(e){
//  let form = $(this)
//  e.preventDefault();
//  $.ajax({
//      url: form.(data:'user_by_id');
//      type: form.attr("method"),
//      dataType: "json",
//        data: form.serialize(),
//     success: function (data) {
//      console.log('success', data)},
//     error: function (data) {
//      console.log('error', data)}
//  })
//}
