$(function () {
  $("#fileUpload").on('change', uploadPhoto);
  $('#changePasswordForm').submit(changePassword);
  $('#followersButton').click(followersApi)
  $('#followingButton').click(followersApi)
  $('#followersButton').click(fun_prof);
});

const error_class_name = "has-error"


function followersApi(){

  let button = $(this)
   $.ajax({
    type: 'GET',
    url: button.data('href'),
    success: function (data) {
        console.log(data)
        renderModal(data, button)
        $('#followerModal').modal('show');
    },
    error: function (data) {
      console.log('error', data)
    }
  })
}


function uploadPhoto(e) {
  e.preventDefault()
  let data = new FormData();
  let files = $(this)[0].files;
  data.append('avatar', files[0]);

  $.ajax({
    type: 'POST',
    url: $(this).data('href'),
    data: data,
    contentType: false,
    processData: false,
    success: function (data) {
      $("#avatar").attr("src", data.avatar);
    },
    error: function (data) {
      console.log('error', data)
    }
  })
}

function changePassword(e) {
  e.preventDefault()
  console.log('click')
  let form = $(this)

  $.ajax({
    type: form.attr("method"),
    url: form.attr("action"),
    data: form.serialize(),
    success: function (data) {
      console.log('success', data)
    },
    error: function (data) {
      $(".help-block").remove()
      let groups = ['#oldPasswordForm', '#newPassword1Form', '#newPassword2Form']
      for (let group of groups) {
        $(group).removeClass(error_class_name);
      }
      if (data.responseJSON.old_password) {
        help_block("#oldPasswordForm", data.responseJSON.old_password)
      }
      if (data.responseJSON.new_password1) {
        help_block("#newPassword1Form", data.responseJSON.new_password1)
      }
      if (data.responseJSON.new_password2) {
        help_block("#newPassword2Form", data.responseJSON.new_password2)
      }
    }
  })

}

function help_block(group, variable) {
  $(group).addClass(error_class_name);
  $(group).append('<div class="help-block">' + variable + "</div>");
}


function renderModal(data, button) {
  $('#followModalTitle').text(button.text())
  followBodyRender(data, button)

}

function followBodyRender(data, button) {
  user_list = data.results
  console.log(user_list, data)
  let body = $('#followModalBody')
  let followUrl = button.data('follow-actions')

  body.empty()
  $.each(user_list, function(i){ //Loop the array
   var templateString = `
      <div class="user">
        <p>
          <img src="${user_list[i].avatar}" class="avatar img-circle img-thumbnail" width=50px>
          <a href='${user_list[i].profile_url}'> ${user_list[i].full_name} </a>
          <button class="btn btn-primary followMe" data-id="${user_list[i].id}" data-href='${followUrl}'> Follow </button>
        </p>
      </div>
   `
   body.append(templateString);
  })


}

function fun_prof(e){
  let button = $(this)
  let data = {
  'user_id':1
  }
  e.preventDefault();
  $.ajax({
      url: button.data('user_by_id'),
      type: 'GET',
      dataType: "json",
      data: data,
     success: function (data) {
      console.log('success', data)},
     error: function (data) {
      console.log('error', data)}
  })
}
