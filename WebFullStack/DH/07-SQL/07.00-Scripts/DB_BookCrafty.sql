/* Comandos para  o DB BookCrafty*/
create database bookcrafty;
use bookcrafty;

create table `bookcrafty`.`editora` ( 
`id` int auto_increment,
`nome` varchar(20),
Primary key (`id`)
);

create table `bookcrafty`.`categoria` (
	`id` int auto_increment,
    `nome` varchar(20),
    primary key (`id`)
);

create table `bookcrafty`.`produto` (
	`id` int auto_increment,
    `nome` varchar(20),
    `descricao` text(90),
    `preco` float,
    `fk_categoria` int,
    `fk_editora` int,
    primary key (`id`),
    foreign key (`fk_categoria`) references `bookcrafty`.`categoria`(`id`),
    foreign key (`fk_editora`) references `bookcrafty`.`editora`(`id`)
);

ALTER TABLE `bookcrafty`.`produto` ADD `imagem` varchar(30);
INSERT INTO `bookcrafty`.`produto` (`nome`, `descricao`, `preco`) values ('Harry Pother', 'Filme de magia', 19.9), ('Vingadores', 'Ação fictícia',39.9);
update `bookcrafty`.`produto` set `imagem`='./imgs/harry.jpg' where id=1;
update `bookcrafty`.`produto` set `imagem`='./imgs/vingadores.jpg' where id=2;
update `bookcrafty`.`produto` set `nome`='Matrix', `descricao`='Acao cientifica', `preco`=9.9, `imagem`='./imgs/matrix.jpg' where `id`=3;
update `bookcrafty`.`produto` set `nome`='Interestelar', `descricao`='Acao cientifica', `preco`=19.9, `imagem`='./imgs/interestelar.jpg' where `id`=4;


CREATE TABLE `bookcrafty`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `senha` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bookcrafty`.`usuario` (`nome`, `email`, `senha`) VALUES ('Kris','kris.a.furtado@gmail.com','abc123');


