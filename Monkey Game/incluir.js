$(function(){
    $(document).on("click", "btIncluir", function () {

        var dados_foto = new FormData($('#meuform')[0]);
        $.ajax({
            url: 'http://localhost:5000/save_image',
            method: 'POST',
            data: dados_foto,
            contentType: false,
            cache: false,
            praocessData: false,
            sucess: function(data){
                alert("enviou a foto direitinho!");
                inserePessoasNoBanco();
            },
            error: function(data){
                alert("Deu ruim!");
            }
        });

        function inserePessoaNoBanco() {
            //pegar dados na tela
                //nome = $("campoNome").val();
                //email = $("campoEmail").val();

            // C:\\fakepath\\olho.jpg"
            // esse fakepath vem de algum lugar da biblioteca utilizada
            // só conta a contrabarra uma vez, inicia do zero
            nome_foto = $('#campoFoto').val().substr(12);

            var dados = JSON.stringify({nome_foto:nome_foto});
            $.ajax({
                url: 'http://localhost:5000/incluir_pessoa',
                method: 'POST',
                dataType: 'json',
                data: dados,
                success: pessoa_incluida,
                error: erroAoIncluirPessoa
            });
            function pessoa_incluida(retorno){
                if(retorno.resultado == 'ok') {
                    alert("pess0a cadastrada com sucesso!");
                } else{
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            }
            function arroAoIncluirPessoa(retorno){
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoIncluirPessoa(retorno){
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }
    })
});