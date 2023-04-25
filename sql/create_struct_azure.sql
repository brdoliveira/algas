CREATE TABLE dados (
	id INT PRIMARY KEY IDENTITY(1,1),
	value FLOAT NOT NULL,
	time_used FLOAT NOT NULL,
	datetime_insert DATETIME NOT NULL
);

CREATE TABLE dados_maquinas (
	id INT PRIMARY KEY IDENTITY(1,1),
	name VARCHAR(255),
	time_used FLOAT NOT NULL,
	datetime_insert DATETIME NOT NULL
);