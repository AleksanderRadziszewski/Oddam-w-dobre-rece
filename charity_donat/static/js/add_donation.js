
    var button_dalej = document.getElementById("dalej");
    var checkboxes = document.querySelectorAll("#my-checkbox");
    var array = [];

    button_dalej.addEventListener("click", function () {

      for (var step = 0; step < checkboxes.length; step++) {
        if (checkboxes[step].checked) {
          array.push(checkboxes[step]);
        }
      }
      $.get({
        url: "/add_donation/",
        data: {
          csrfmiddlewaretoken: csrftoken,
          list_checked: array
        },
        function(data, status) {
          alert(status)
        }
      })
    });


