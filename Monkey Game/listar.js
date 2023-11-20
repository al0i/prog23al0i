$(function() {
    $(document).on('click','#btListar',function(){
        $.ajax({
            url:'http://localhost:5000/retornar_pessoas',
            method:'GET',
            dataType:'json',
            success:listar_pessoas,
            error:function(){
                alert("Erro ao ler dados, verifique o backend");
            }
        });

        function listar_pessoas(retorno){
            if(retorno.resultado=='ok'){
                $('#corpoTabelaPessoas').empty();
                pessoas=retorno.detalhes;
                for (var i in pessoas){
                    lin=`<tr>
                        <td>${pessoas[i].nome}</td>
                        <td>${pessoas[i].email}</td>
                        <td><img src="http://localhost:5000/get_image/${pessoas[i].id}" height=100 width=100></td>
                        <tr>`;
                    $('#corpoTabelaPessoas').append(lin);
                }
            } else{
                alert('erro no retorno: '+retorno.detalhes);
            }
        }
    });
});