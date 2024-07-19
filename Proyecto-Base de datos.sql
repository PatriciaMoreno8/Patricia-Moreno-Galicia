create database base_de_usuarios;
use base_de_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
            username VARCHAR(255) PRIMARY KEY,
            password_hash VARCHAR(32)
        );
        
       
      INSERT INTO usuarios (username, password_hash) 
VALUES ('patricia_7', '123456');

SELECT * FROM usuarios       

 INSERT INTO usuarios (username, password_hash) 
VALUES 
('Kevin_7', '123456'),
('Eloi_55', '123456'),
('Sara2', '123456'),
('adrian_88', '123456'),
('edgar', '123456'),
('elias', '123456');

SELECT * FROM usuarios    



       
