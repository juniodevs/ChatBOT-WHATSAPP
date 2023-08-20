<?php
$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'chatbot';
$conn = mysqli_connect($servidor, $usuario, $senha, $banco);
// if (!$conn){
//     //echo "Erro ao conectar ao banco de dados";
// }
// else{
//    // echo "Conectado ao banco de dados";
// }

$numero_telefone = $_GET['telefone'];
$msg = $_GET['msg'];
$usuario = $_GET['usuario'];

#echo "*Telefone*: $numero_telefone *MSG*: $msg *Usuario*: $usuario";


$sql = "SELECT * FROM usuario WHERE telefone = '$numero_telefone'";
$query = mysqli_query($conn, $sql);
$total = mysqli_num_rows($query);

while ($rows_usuarios = mysqli_fetch_array($query)){
    $status = $rows_usuarios['status'];
    $id = $rows_usuarios['id'];
}


?>
<?php
if ($total == 0){
    $sql = "INSERT INTO usuario (telefone, status) VALUES ('$numero_telefone', '1')";
    $query = mysqli_query($conn, $sql);
    if ($query){
        echo "Bem-vindo ao nosso Chat Bot!";
    }
}

if($total >= 1)
{
}
?>

<?php

// $sql = "SELECT * FROM bot WHERE id  > 0";
// $query = mysqli_query($conn, $sql);

// while ($rows_usuarios = mysqli_fetch_array($query)){
//     $nome = $rows_usuarios['nome'];

//     echo "Nome: ".$nome."<br>";
// }

// $nome = "Pedro";
// $telefone = "123456";

// $sql ="UPDATE bot SET nome = '$nome', telefone = '$telefone'";

// $query = mysqli_query($conn, $sql);

// if (!$query){
//     echo "Erro ao atualizar dados";
// }
// else{
//     echo "Dados atualizados com sucesso";
// }

// $sql = "INSERT INTO bot (nome, telefone) VALUES ('$nome', '$telefone')";

// $query = mysqli_query($conn, $sql);

// if (!$query){
//     echo "Erro ao inserir dados";
// }
// else{
//     echo "Dados inseridos com sucesso";
// }
