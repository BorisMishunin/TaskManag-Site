
$(window).load();

function get_filters(type){
    var indexes='';
    $('[id=filter_chosen][type = '+type+']').each(function(indx, element){
        indexes+=':'+$(element).attr('value');
    });
    return indexes;
}

function get_current_page(){
    return $('#current_page').attr('value')
}

function show_table(){
    $.ajax({
        type:"POST",
        url:"/show_tasks/",
        data: {'users': get_filters("0"), 'statuses':get_filters("1"), 'current_page': get_current_page()},
        success: function(html){
            $('#table').html(html);
            setup_select();
            $('.pages').click(function(){
                $('#current_page').attr('id', 'page');
                $(this).attr('id','current_page');
                show_table();
            });
        },
        error : function(xhr,errmsg,err) {
            //alert(xhr.status + ": " + xhr.responseText);
        }
    });
};

function setup_select(){
    $(".select").change(function(event){
            $.ajax({
                 type:"POST",
                 url:"/edit_task/",
                 data: {'value': $( this ).val() // from form
                        },
                 success: function(html){
                     show_table();
                 },
                 error : function(xhr,errmsg,err) {
                    //alert(xhr.status + ": " + xhr.responseText);
                 }
            });

    });
}



$(document).ready(function() {
      show_table();
        //$('[id=filter][type = 0]').hide()


       setInterval(show_table, 30000);
       $('.filter').click(function(){
            if ($(this).attr("id") == 'filter_chosen'){
                $(this).attr("id", "filter");
                //alert(""+get_filters("0")+get_filters("1"));
                show_table();
            }
            else{
                $(this).attr("id", "filter_chosen");
                //alert(""+get_filters("0")+get_filters("1"));
                show_table();
            }
       });
});