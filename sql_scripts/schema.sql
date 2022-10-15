CREATE DATABASE IF NOT EXISTS login_test;
USE login_test;

CREATE TABLE IF NOT EXISTS logininfo(
	id INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR(20) NOT NULL UNIQUE,
	display_name VARCHAR(20) NOT NULL,
	email VARCHAR(255) NOT NULL,
	hashed_pin CHAR(4) NOT NULL,

	PRIMARY KEY (id),
	CHECK (LENGTH(username) > 0),
	CHECK (LENGTH(display_name) > 0)
);