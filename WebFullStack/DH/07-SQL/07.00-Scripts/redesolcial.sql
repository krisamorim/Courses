-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema redesocial
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema redesocial
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `redesocial` DEFAULT CHARACTER SET utf8 ;
USE `redesocial` ;

-- -----------------------------------------------------
-- Table `redesocial`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redesocial`.`users` (
  `idusers` INT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL,
  `username` VARCHAR(10) NULL,
  `phone` VARCHAR(20) NULL,
  `dtnasc` DATE NULL,
  `registro` TIMESTAMP(6) NULL,
  PRIMARY KEY (`idusers`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redesocial`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redesocial`.`comentarios` (
  `idcomentarios` INT NOT NULL AUTO_INCREMENT,
  `comentario` LONGTEXT NULL,
  PRIMARY KEY (`idcomentarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `redesocial`.`users_has_comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redesocial`.`users_has_comentarios` (
  `users_idusers` INT NOT NULL,
  `comentarios_idcomentarios` INT NOT NULL,
  PRIMARY KEY (`users_idusers`, `comentarios_idcomentarios`),
  INDEX `fk_users_has_comentarios_comentarios1_idx` (`comentarios_idcomentarios` ASC) VISIBLE,
  INDEX `fk_users_has_comentarios_users_idx` (`users_idusers` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_comentarios_users`
    FOREIGN KEY (`users_idusers`)
    REFERENCES `redesocial`.`users` (`idusers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_comentarios_comentarios1`
    FOREIGN KEY (`comentarios_idcomentarios`)
    REFERENCES `redesocial`.`comentarios` (`idcomentarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
