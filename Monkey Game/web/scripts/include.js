$(function() {
    $(document).on('click', '#btnInclude', function(){
        if (!$('#sprite').val()){
            alert('Please upload a file!');
        }else{
            var spriteData = new FormData($('#formInclude')[0]);

            $.ajax({
                url:'http://localhost:5000/save_image',
                method:'POST',
                data:spriteData,
                contentType:false,
                cache:false,
                processData:false,
                success:function(){
                    alert("Success!");
                }, error:function(){
                    alert("Error!")
                }
            });
        };
    });
});