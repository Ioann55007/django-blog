$(function () {
 $('.followMe').click(followerApi)
 $('#followersButton').click(def_followers)
 $('#followeringButton').click(def_following)
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

function def_followers(){
let button = $(this)
console.log('click')
let data = {'user_profile':profile}
}

$.ajax({
    url: button.data('href'),
    type: 'get',
    dataType: "json",
    data: data,
     success: function (data) {
     button.text(data.user_profile)
      console.log('success', data)},
     error: function (data) {
      console.log('error', data)}
  })
}

function def_following(){
let button = $(this)
console.log('click')
let data = {'user_profile':profile}
}

$.ajax({
    url: button.data('href'),
    type: 'get',
    dataType: "json",
    data: data,
     success: function (data) {
     button.text(data.user_profile)
      console.log('success', data)},
     error: function (data) {
      console.log('error', data)}
  })
}
