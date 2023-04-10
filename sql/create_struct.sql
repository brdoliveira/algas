CREATE DATABASE dados_algas;
USE dados_algas;

CREATE TABLE IF NOT EXISTS dados (
	id INT AUTO_INCREMENT PRIMARY KEY,
	value FLOAT NOT NULL,
	memory_used FLOAT NOT NULL,
	time_used FLOAT NOT NULL,
	datetime_insert DATETIME NOT NULL
)