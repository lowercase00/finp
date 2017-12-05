<?php  
//action.php
$connect = mysqli_connect('localhost', 'root', '', 'base_teste');

$input = filter_input_array(INPUT_POST);

$data = mysqli_real_escape_string($connect, $input["data"]);
$credito = mysqli_real_escape_string($connect, $input["credito"]);
$debito = mysqli_real_escape_string($connect, $input["debito"]);
$descricao = mysqli_real_escape_string($connect, $input["descricao"]);
$valor = mysqli_real_escape_string($connect, $input["valor"]);

if($input["action"] === 'edit')
{
 $query = "
		 UPDATE ledger_teste 
		 SET 
			data = '".$data."', 
			credito = '".$credito."',
			debito = '".$debito."',
			descricao = '".$descricao."', 
			valor = '".$valor."'
		WHERE id = '".$input["id"]."'
 		";

 mysqli_query($connect, $query);

}

if($input["action"] === 'delete')
{
 $query = "
		 DELETE FROM ledger_teste
		 WHERE id = '".$input["id"]."'
 		";
 mysqli_query($connect, $query);
}

echo json_encode($input);

?>