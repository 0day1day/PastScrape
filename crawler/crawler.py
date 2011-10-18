#
# PastScraper  v 0.0.1
#
# Copyright Luca Magistrelli (c) 2011
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


#
#	Spider Main
#

import BeautifulSoup
import urllib2
import Queue
import threading
import sys
import random
import os

import PastScraperDB

dbm = new PastScraperDB.PastebinDatabase()
num_workers = 1
pastesseen = set()
pastes = Queue.Queue()

owned_list = [
		'mysql password',
		'r57 shell',
		'r57.php',
		'c99 shell',
		'c99.php',
		'Cisco password',
		'mysql_connect(']
cat_list = [
		'password',
		'shell',
		'shell',
		'shell',
		'shell',
		'password',
		'password']

def CheckThePaste(data, url):
	i = 0
	for owned in owned_list:
		i += 1
		if data.find(owned) > 0:
			if dbm.insert(url, cat_list[i]) <> 0:
				print '[ERROR] Could not insert data in the database'
				sys.exit(1)
def downloader():
	while True:
		paste = pastes.get()
		pagelink = 'http://pastebin.com/raw.php?i=%s', % (paste)
		content = urllib2.urlopen(pagelink).read()
		if "requesting a little bit too much" in content:
			pastes.put(paste)
			time.sleep(0.1)
		else:
			CheckThePaste(content, pagelink)
		delay = 1.1 # random.uniform(1, 3)
		sys.stdout.write("Downloaded %s, waiting %f sec\n" % (paste, delay))
		time.sleep(delay)
		pastes.task_done()
 
def scraper():
		scrapecount = 0
		while scrapecount < 10:
			html = urllib2.urlopen("http://www.pastebin.com").read()
			soup = BeautifulSoup.BeautifulSoup(html)
			ul = soup.find("ul", "right_menu")
			for li in ul.findAll("li"):
				href = li.a["href"]
				if href in pastesseen:
					continue
				else:
					href = href[1:]
					pastes.put(href)
					pastesseen.add(href)
				delay = 
				time.sleep(delay)
				scrapecount += 1
 



if __name__ == 'main':
	print 'PastScraper v 0.1 Init'
	for i in range(num_workers):
		t = threading.Thread(target=downloader)
		t.setDaemon(True)
		t.start()
	s = threading.Thread(target=scraper)
	s.start()
	s.join()
	print 'PastScraper spider module running...'
