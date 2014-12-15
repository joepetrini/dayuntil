if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

function unsave_day(){
    $.post( "/api/remove", { date: current_date })
      .done(function( data ) {
        $('#user-day').hide();
        $('#save-strip').removeClass('saved-day');
        $('#day-form').show();
      });
}

function save_day() {
    var name = $('#day_name').val().trim();

    $.post( "/api/add", { name: name, date: current_date })
      .done(function( data ) {
        $('#day-form').hide();
        $('#save-strip').addClass('saved-day');
        $('#user-day').html(data).show();
      });
}