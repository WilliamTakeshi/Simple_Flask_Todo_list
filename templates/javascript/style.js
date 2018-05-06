var modal = document.getElementById('CreateTaskModal');
var btn = document.getElementById("CreateTaskBtn");
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
// Submit create task modal
$('#form-create-todo').submit(function(e){
    e.preventDefault();
    $.ajax({
        url:'/v0/task',
        type:'post',
        data:$('#form-create-todo').serialize(),
        success:function(){
            document.location.href="{{ url_for('task') }}";
        },
        error:function(request, status, error){
            console.log(request.responseText);
        }
    });
});


$('#UpdateTaskModal').on('show.bs.modal', function(e) {
    var id = $(e.relatedTarget).data('id');
    var title = $(e.relatedTarget).data('title');
    var description = $(e.relatedTarget).data('description');
    $(e.currentTarget).find('input[name="id"]').val(id);
    $(e.currentTarget).find('input[name="title"]').val(title);
    $(e.currentTarget).find('input[name="description"]').val(description);
});
// Submit create task modal
$('#form-update-todo').submit(function(e){
    e.preventDefault();
    id = $('#form-update-todo')[0][0].value;
    $.ajax({
        url:'/v0/task/' + id,
        type:'put',
        data:$('#form-update-todo').serialize(),
        success:function(){
            console.log($('#form-update-todo').serialize());
            document.location.href="{{ url_for('task') }}";
        },
        error:function(request, status, error){
            console.log(request.responseText);
        }
    });
});


function deleteTask(taskid){
    console.log(taskid);
    var currentUrl = window.location.href
    var deleteTaskUrl = '/v0/task/' + taskid
    var deleteTaskMethod = "DELETE";
    var data = {};
    var taskrowid = "#taskrow" + taskid
    $.ajax({
        url: deleteTaskUrl,
        method: deleteTaskMethod,
        data: data,
        success: function(data){
            console.log("working!")
            $(taskrowid).toggle()
          },          
        error: function(errorData){
            console.log(errorData)
          }  
      })  
}