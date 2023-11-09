$(function () {

    $(document).on('click', '#btListar', function(){
        $.ajax({
            url:'http://localhost:5000/retornar_pessoas',
            method: 'GET',
            dataType: 'json',
            sucess: listar_pessoas,
            error: function(){
                alert("Erro ao ler os dados. Verifique o backend.");
            }
        });

        function listar_pessoas(retorno){
            if (retorno.resultado=='ok'){
                $('#corpoTabelaPessoas').empty();
                pessoas = retorno.detalhes;
                for (var i in pessoas){
                    lin = `<tr>
                            <td><img src="http://localhosto:5000/get_image/${pessoas[i].id}" height=100 width=100></td>
                            </tr>`;
                    $('#corpoTabelaPessoas').append(lin);
                }
            }else{
                alert("Erro no retorno: "+retorno.detalhes);
            }
        }
    });
});