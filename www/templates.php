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
#	PastScraper Website template functions
#
*/

function szHeader()
{
?>
<html xmlns='http://www.w3.org/1999/xhtml'>
<head>
	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
	<meta http-equiv='Content-Language' content='en' /><title>
	<title>PastScraper v 0.01</title>
	<link type='text/css' rel='stylesheet' href='style.css' />
</head>
<body>
	<div class='MainDiv'>
	<div class="CenterDiv">

<?
}

function szFooter()
{
?>
<p class="FooterP">
<small>PastScraper v 0.0.1</small><br/>
This is a simple web page for listening the pastebin's links crawled by PastScraper Spider<br/>
PastScraper Copyright(c) Luca Magistrelli
</p>
</div>
</div>
</body>
</html>
<?
}
?>
