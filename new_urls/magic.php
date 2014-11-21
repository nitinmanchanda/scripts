<?php
function get_http_response_code($url) {
    $headers = get_headers($url);
    return substr($headers[0], 9, 3);
}

function getRedirectUrl($url) {
    $headers = get_headers($url);
    return str_replace('Location: ', '', $headers[2]);
}

$categories = fopen("cat.csv", "r");
$categoryMap = array();

while (! feof($categories)) {
	$row = fgetcsv($categories);
	$categoryUrl = $row[0];
	$categoryId = $row[1];

	if(! in_array($categoryUrl, $categoryMap)) {
		$categoryMap[$categoryUrl] = $categoryId;
	}
}
fclose($categories);

$input = fopen("raw_input.csv", "r");
$output = fopen("output.csv", "w");

$counter = 0;
$urlsProcessed = array();

while (! feof($input)) {
	$row = fgetcsv($input);
	$url = $row[0];

	$redirectUrl = "";
	$wrongRedirect = "";
	$categoryId = "";
	$isDuplicate = "";
	$newUrl = "";
	$numberOfProducts = "";

	$finalData = array();

	if (in_array($url, $urlsProcessed)) {
		$isDuplicate = "Yes";
	} else {
		array_push($urlsProcessed, $url);
		$responseCode = get_http_response_code($url);

		try {
			if($responseCode == "301" || $responseCode == "302") {
				$redirectUrl = getRedirectUrl($url);
			} else if($responseCode != "200") {
				$wrongRedirect = "Invalid";
			} else {
				$contents = file_get_contents($url);

	    		if (preg_match('/span class="count">([0-9]+)<\/span> results/', $contents, $matches) and isset($matches[1])) {
	    			$numberOfProducts = $matches[1];
	    		}

	    		$categoryUrl = str_replace('http://www.limeroad.com', '', $url);
	    		
	    		if(in_array($categoryUrl, array_keys($categoryMap))) {
	    			$categoryId = $categoryMap[$categoryUrl];
	    		} else {
	    			$categoryId = "Old category - Serving from redis cache!";
	    		}
			}
		} catch(Exception $e) {
			echo 'exception thrown';
		}
	}

	$finalData[0] = $url;
	$finalData[1] = $redirectUrl;
	$finalData[2] = $wrongRedirect;
	$finalData[3] = $categoryId;
	$finalData[4] = $isDuplicate;
	$finalData[5] = $newUrl;
	$finalData[6] = $numberOfProducts;

	fputcsv($output, $finalData);

	++$counter;
	if ($counter % 10 == 0) {
		echo "URLs Processed: {$counter}\n";
	}
}
fclose($input);
fclose($output);
echo "\n";
?>
