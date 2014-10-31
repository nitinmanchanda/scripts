<?php
$urls = array(
	"http://www.limeroad.com/women-clothing/ethnic-indian-wear",
	"http://www.limeroad.com/alessia/bangles",
	"http://www.limeroad.com/test",
	"http://www.limeroad.com/kya-cheez-hai/beauty",
	"http://www.limeroad.com/posy-samriddh/",
	"http://www.limeroad.com/home-furnishings/work-nook"
	);

function get_http_response_code($url) {
    $headers = get_headers($url);
    return substr($headers[0], 9, 3);
}

foreach ($urls as $url) {
	
	$needle = "Please come back soon. We won't disappoint you!";
	$responseCode = get_http_response_code($url);

	echo "\n".$url."(HTTP status: ".$responseCode.") => ";
	
	try {
		if($responseCode != "200") {
			echo 'Invalid page!';
			continue;
		}
		$contents = file_get_contents($url);
        if(strpos($contents, $needle)!== false) {
    	        echo 'Live but no products!';
    	} else {
            	echo 'Its working!';
    	}
	} catch(Exception $e) {
		echo 'exception thrown';
	}
}
echo "\nDone!\n";







?>
