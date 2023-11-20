$(function(){
    $(document).on('click', '#btIncluir', function(){
        var dados_foto = new FormData($('#meuform')[2]);

        $.ajax({
            url:'http://localhost:5000/save_image',
            method: 'POST',
            data: dados_foto,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data){
                alert("Enviou a foto direitinho!");
                inserePessoaNoBanco();
            },
            error: function(data){
                alert('Deu ruim na foto!');
            }
        });

        function inserePessoaNoBanco() {
            nome = $('#campoNome').val();
            email = $("campoEmail").val();
            nome_foto = $('#campoFoto').val().substr(12);

            var dados = JSON.stringify({nome:nome, email:email, nome_foto:nome_foto});
            $.ajax({
                url:'http://localhost:5000/incluir_pessoa',
                method:'POST',
                dataType:'json',
                data:dados,
                success: pessoa_incluida,
                error:erroAoIncluirPessoa
            });
            function pessoa_incluida(retorno){
                if (retorno.resultado=='ok'){
                    alert("Pessoa cadastrada com sucesso!");
                    $("#campoNome").val();
                    $('#campoEmail').val();
                }else{
                    alert(retorno.resultado + ':' + retorno.detalhes);
                }
            }
            function erroAoIncluirPessoa(retorno){
                alert("ERRO:" + retorno.resultado + ':' + retorno.detalhes);
            }
        }
    });
});