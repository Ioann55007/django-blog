$(function () {
 $('.followMe').click(followerApi)
});

function followerApi(){
let button = $(this)
console.log('click')
let data = {
'user_id': button.data('id')
}

$.ajax({
    url: button.data('href'),
    type: 'POST',
    dataType: "json",
    data: data,
     success: function (data) {
     button.text(data.follower_status)
      console.log('success', data)},
     error: function (data) {
      console.log('error', data)}
  })
}
