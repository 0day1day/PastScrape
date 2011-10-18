

CREATE TABLE categories (
	'catid' int(100) NOT NULL auto_increment,
	'catname' varchar(100) NOT NULL
	PRIMARY_KEY('catid')
);

INSERT INTO categories (catid, catname) VALUES ('1', 'Password');
INSERT INTO categories (catid, catname) VALUES ('2', 'Shell');
INSERT INTO categories (catid, catname) VALUES ('3', '...');
CREATE TABLE pastebin_links(
	'id' int(100) NOT NULL auto_increment,
	'link' varchar(100) NOT NULL,
	'catid' int(100) NOT NULL,
	'date_insert' varchar(50) NOT NULL
);
