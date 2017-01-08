/*
        var obj = {};
        obj['value'] = $("#text-post").val();
        sendAjaxData(obj);
        */
      });

      function sendAjaxData(content) {
        var submit = $.ajax({
                url: 'http://192.168.1.107:3333/', 
                type: 'POST', 
                data: content,
                error: function(error) {
                console.log("Error - AJAX");
              }
            });
              submit.success(function (data) {
                var success = data;
                console.log(data);
            });
      };