function saveItem(item_id) {

  $.ajax({
    url: '/catalog/save/' + item_id,
    type: 'POST',
    success: function(response){
      console.log(response, "success");
      // disable the button and update text
      $("#" + item_id).html("Saved");
      $("#" + item_id).prop('disabled', true);
    },
    error: function(error){
      console.log(error);
    }
  });

}


function removeItem(item_id) {

  $.ajax({
    url: '/catalog/remove/' + item_id,
    type: 'POST',
    success: function(response){
      console.log(response, "success");
      // reload the page
      location.reload(true);
    },
    error: function(error){
      console.log(error);
    }
  });

}