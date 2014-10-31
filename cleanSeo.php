<? 
set_time_limit(0); 

$dbName = "lradmin"; 
$dbUser = "root"; 
$dbPass = ""; 
$dbHost = "localhost"; 

$connection = mysql_connect($dbHost, $dbUser, $dbPass) 
       or die("Could not connect : " . mysql_error()); 

mysql_select_db($dbName)  
    or die("Could not select database"); 

$mtime = microtime(); 
$mtime = explode(" ",$mtime); 
$mtime = $mtime[1] + $mtime[0]; 
$starttime = $mtime;  

/********************************** 
* General Code Generating Script  * 
**********************************/ 

$pageType = 'category';
$dbName = "seo";

$sql = "SELECT seoUrl, COUNT(pageId) AS instances FROM ".$dbName." WHERE pageType = '".$pageType."' GROUP BY seoUrl ORDER BY instances";
$data = mysql_query($sql); 
$count = 0;
$duplicateCases = 0;
while (($dataArray = mysql_fetch_row($data)) != NULL) {
    if($dataArray[1] > 1) {
        ++$duplicateCases;
        removeDuplicates($dbName, $pageType, $dataArray[0]);
    }
    $count += $dataArray[1];
}

echo "Total Rows Processed: ".$count."\n";
echo "Duplicate Cases: ".$duplicateCases."\n";

function removeDuplicates($dbName, $pageType, $seoUrl) {
    $sql = "SELECT id FROM ".$dbName." WHERE pageType = '".$pageType."' AND seoUrl = '".$seoUrl."' ORDER BY id DESC";
    $data = mysql_query($sql); 
    $latestEntry = TRUE;
    $rowsDeleted = 0;
    while (($dataArray = mysql_fetch_row($data)) != NULL) {
        if(!$latestEntry) {
            $sql = "DELETE FROM ".$dbName." WHERE id = '".$dataArray[0]."' AND pageType = '".$pageType."' AND seoUrl = '".$seoUrl."'";
            mysql_query($sql);
            echo "Row deleted, where id = ".$dataArray[0]."\n";
            ++$rowsDeleted;
        } else {
            $latestEntry = FALSE;
        }
    }
    echo "Rows deleted for ".$seoUrl.": ".$rowsDeleted."\n";
}
/********************************** 
* Handle Script Execution Time    * 
**********************************/ 
$mtime = microtime(); 
$mtime = explode(" ",$mtime); 
$mtime = $mtime[1] + $mtime[0]; 
$endtime = $mtime; 
$totaltime = ($endtime - $starttime); 
echo "Total Time Taken For Execution: ".$totaltime." Seconds\n";  
?>