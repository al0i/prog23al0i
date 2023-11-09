$(function () {
    $(document).on('click', '#btIncluir', function() {
        var dados_foto = new FormData($('#meuform')[0]);
        $.ajax({
            url: 'http://localhost:5000/save_image',
            method:'POST',
            data: dados_foto,
            contentType:false,
            cache:false,
            processData: false,
            sucess: function(data){
                alert("Enviou a foto direitinho!");
                //inserePessoaNoBanco();
            }, error: function(data){
                alert("Deu ruim na foto :(");
            }
        });
    })
})