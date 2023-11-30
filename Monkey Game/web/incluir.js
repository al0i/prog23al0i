$(function() {
    $(document).on('click', '#btIncluir', function(){
        if (!$('#campoImagem').val()){
            alert('Please upload file');
        }else{
            var dados_foto = new FormData($('#meuform')[0]);

            $.ajax({
                url:'http://localhost:5000/save_image',
                method:'POST',
                data:dados_foto,
                contentType:false,
                cache:false,
                processData:false,
                success:function(data){
                    alert("Success!");
                }, error:function(data){
                    alert("Error!")
                }
            });
        };
    });
});