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
#	Spider Database function(only with MySql)
#


import sys
import time
import datetime

#check if MySqldb is installed
try:
	import MySQLdb
except ImportError, why:
    sys.stderr.write("[FATAL] missing dependency: MySqldb (http://sourceforge.net/projects/mysql-python/)\n")
    sys.exit(1)

#database configuration 
host=""
userdb = ""
pwddb = ""
dbname = ""

#do not modify this
db = ""

class PastebinDatabase():
	
	def __init__(self):
		try:
			self.db=MySQLdb.connect(host,userdb,pwddb,dbname)
		except:
			print '[ERROR] Database connection failure'
			sys.exit(1)
	
	def insert(self, url, cat):
		cursor = self.db.cursor()
		sqlcat = "SELECT catid FROM categories WHERE catname = '%s'" % (cat)
		try:
		   	cursor.execute(sqlcat)
			results = cursor.fetchall()
   			for row in results:
      				catid = row[0]
		except:
			print "[ERROR] unable to fecth catid"
			return 1
		sql = "INSERT INTO pastebin_links(link, cat, date_insert) VALUES ('%s', '%s', '%s')" % (url, catid, datetime.datetime.today().strftime("%Y-%m-%d"))
		try:
			cursor.execute(sql)
			self.db.commit
		except:
			print '[ERROR] Error with the query: '  + sql
			self.db.rollback()
			return 1
		return 0

