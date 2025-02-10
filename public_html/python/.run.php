<?php
$output=null;
$retval=null;
exec('./jupyter/.run.sh', $output, $retval);
//echo "Returned with status $retval and output:\n";
$data = ["success"=>true,"message"=>"Successfully started jupyter!"];
header('Content-Type: application/json; charset=utf-8');
if($output){
	$link = $output[1];
	$parsedUrl = parse_url($link);
	$port = $parsedUrl['port'];
	parse_str($parsedUrl['query'], $queryParams);
	$tokenParts = explode(' :: ', $queryParams['token']);
	$token = $tokenParts[0];
	$data['port']=$port;
	$data['token']=$token;
}else{
	$data['success']=false;
	$data['message']='Cannot start server, please try again later!';
}
echo json_encode($data);
exit;
