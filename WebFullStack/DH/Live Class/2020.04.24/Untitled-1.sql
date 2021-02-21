create database fakeinstagram;
use fake instagram;
CREATE TABLE usuarios ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(190) NOT NULL,
    email VARCHAR(190) NOT NULL,
    senha varchar(190) NOT NULL
);

CREATE TABLE seguidores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuarios_id int,
    seguidor_usuario_id int,
    FORENG KEY (usuarios_id) REFERENCES usuarios(id),
    FORENG KEY (seguidor_usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto TEXT NOT NULL,
    publicacoes_id INT,
    usuarios_id INT,
    FORENG KEY (publicacoes_id) REFERENCES publicacoes(id),
    FORENG KEY (usuarios_id) REFERENCES usuarios(id),
)

