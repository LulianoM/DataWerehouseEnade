import sqlite3

print("\n Criando Banco de Dados e Migrando Dados \n")

conn = sqlite3.connect('dadosenade.db')
cursor = conn.cursor()

cursor.execute("""
-- -----------------------------------------------------
-- Schema dadosenade
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dadosenade` DEFAULT CHARACTER SET utf8 ;
USE `dadosenade` ;

-- -----------------------------------------------------
-- Table `dadosenade`.`CURSO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dadosenade`.`CURSO` (
  `CO_GRUPO` INT NOT NULL,
  `CO_MODALIDADE` INT NOT NULL,
  `CO_TURNO_GRADUACAO` INT NULL,
  `nome_modalidade` VARCHAR(45) NULL,
  `nome_turno_curso` VARCHAR(45) NULL,
  PRIMARY KEY (`CO_GRUPO`, `CO_MODALIDADE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dadosenade`.`LOCALIDADE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dadosenade`.`LOCALIDADE` (
  `CO_UF_CURSO` INT NOT NULL,
  `CO_REGIÃO_CURSO` INT NULL,
  `nome_uf` VARCHAR(45) NULL,
  `nome_região` VARCHAR(45) NULL,
  PRIMARY KEY (`CO_UF_CURSO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dadosenade`.`ESTUDANTE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dadosenade`.`ESTUDANTE` (
  `NU_IDADE` INT NOT NULL,
  `TP_SEXO` VARCHAR(1) NULL,
  `QE_COR` VARCHAR(1) NULL,
  PRIMARY KEY (`NU_IDADE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dadosenade`.`TABELA FATO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dadosenade`.`TABELA FATO` (
  `NU_ANO` INT NULL,
  `CO_GRUPO` INT NOT NULL,
  `CO_MODALIDADE` INT NOT NULL,
  `CO_UF_CURSO` INT NULL,
  `CO_REGIÃO_CURSO` INT NULL,
  `NU_IDADE` INT NULL,
  `TP_SEXO` VARCHAR(1) NULL,
  `CO_TURNO_GRADUCAO` INT NULL,
  `CURSO_CO_GRUPO` INT NOT NULL,
  `LOCALIDADE_CO_UF_CURSO` INT NOT NULL,
  `ESTUDANTE_NU_IDADE` INT NOT NULL,
  PRIMARY KEY (`NU_ANO`, `CO_GRUPO`, `CO_MODALIDADE`),
  INDEX `fk_TABELA FATO_CURSO_idx` (`CURSO_CO_GRUPO` ASC) VISIBLE,
  INDEX `fk_TABELA FATO_LOCALIDADE1_idx` (`LOCALIDADE_CO_UF_CURSO` ASC) VISIBLE,
  INDEX `fk_TABELA FATO_ESTUDANTE1_idx` (`ESTUDANTE_NU_IDADE` ASC) VISIBLE,
  CONSTRAINT `fk_TABELA FATO_CURSO`
    FOREIGN KEY (`CURSO_CO_GRUPO`)
    REFERENCES `dadosenade`.`CURSO` (`CO_GRUPO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TABELA FATO_LOCALIDADE1`
    FOREIGN KEY (`LOCALIDADE_CO_UF_CURSO`)
    REFERENCES `dadosenade`.`LOCALIDADE` (`CO_UF_CURSO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TABELA FATO_ESTUDANTE1`
    FOREIGN KEY (`ESTUDANTE_NU_IDADE`)
    REFERENCES `dadosenade`.`ESTUDANTE` (`NU_IDADE`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

""")

conn.close()

print("\n Banco de Dados criado com sucesso \n")

