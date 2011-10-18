<?

/*
  PastScraper  v 0.0.1

  Copyright Luca Magistrelli (c) 2011

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.
 
  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
*/

/*
#
#	PastScraper Website index
#
*/

include_once 'dbconnect.php';
require_once 'templates.php';

szHeader();

$sqlcat = "SELECT * FROM categories ORDER BY catid DESC";
$query = mysql_query($query) or die(mysql_error());
while($row = mysql_fetch_rows($query)
{

	echo '<table class="ExploitTable">';
	echo '<tbody>';
	echo '<tr class="TableHeader">';
	echo '<td>';
	echo $row['catname'];
	echo '</td>';
	echo '</tr>';
	$sqllinks = "SELECT * FROM pastebin_links WHERE catid = ".$row['catid']." ORDER BY id LIMIT 0,10";
	$querylinks = mysql_query($sqllinks) or die(mysql_error());
	while($row2 = mysql_fetch_rows($querylinks)
	{
		extract($row2);
		echo '<tr>';
		echo '<td>'.$date_insert.'</td>';
		echo '<td><a href="'.$link.'">'.$link'.</a></td>';
		echo '</tr>';
	}
	echo '</tbody>';
	echo '</table>';
}

szFooter();

?>
