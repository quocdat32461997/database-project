-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Spy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Spy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Spy` DEFAULT CHARACTER SET utf8 ;
USE `Spy` ;

-- -----------------------------------------------------
-- Table `Spy`.`AGENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`AGENT` (
  `Agent_id` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Status` VARCHAR(45) NULL,
  `Salary` INT NULL,
  `Emergency_contact_line` INT NULL,
  PRIMARY KEY (`Agent_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`FIREARM`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`FIREARM` (
  `Origin` VARCHAR(45) NULL,
  `Caliber` INT NULL,
  `Type` VARCHAR(45) NULL,
  `Make` VARCHAR(45) NULL,
  `Serial_no` INT NOT NULL,
  `Cost` INT NULL,
  `Agent_id` INT NULL,
  PRIMARY KEY (`Serial_no`),
  INDEX `Agent_id_idx` (`Agent_id` ASC) VISIBLE,
  CONSTRAINT `FA_Agent_id`
    FOREIGN KEY (`Agent_id`)
    REFERENCES `Spy`.`AGENT` (`Agent_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`TARGET`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`TARGET` (
  `Target_code_name` VARCHAR(45) NOT NULL,
  `Legal_name` VARCHAR(45) NULL,
  `Affiliation` VARCHAR(45) NULL,
  PRIMARY KEY (`Target_code_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`UNIT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`UNIT` (
  `Unit_id` INT NOT NULL,
  `Budget` INT NULL,
  `Target_code_name` VARCHAR(45) NULL,
  PRIMARY KEY (`Unit_id`),
  INDEX `Target_code_name_idx` (`Target_code_name` ASC) VISIBLE,
  CONSTRAINT `U_Target_code_name`
    FOREIGN KEY (`Target_code_name`)
    REFERENCES `Spy`.`TARGET` (`Target_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`SPY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`SPY` (
  `Spy_code_name` VARCHAR(45) NOT NULL,
  `Specialty` VARCHAR(45) NULL,
  `Target_code_name` VARCHAR(45) NULL,
  PRIMARY KEY (`Spy_code_name`),
  INDEX `Target_code_name_idx` (`Target_code_name` ASC) VISIBLE,
  CONSTRAINT `SPY_Target_code_name`
    FOREIGN KEY (`Target_code_name`)
    REFERENCES `Spy`.`TARGET` (`Target_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`HOME SPY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`HOME_SPY` (
  `Spy_code_name` VARCHAR(45) NULL,
  `Current_location` VARCHAR(45) NULL,
  `Unit_id` INT NULL,
  `Agent_id` INT NOT NULL,
  PRIMARY KEY (`Agent_id`),
  INDEX `Spy_code_name_idx` (`Spy_code_name` ASC) VISIBLE,
  INDEX `Unit_id_idx` (`Unit_id` ASC) VISIBLE,
  CONSTRAINT `HS_Agent_id`
    FOREIGN KEY (`Agent_id`)
    REFERENCES `Spy`.`AGENT` (`Agent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `HS_Spy_code_name`
    FOREIGN KEY (`Spy_code_name`)
    REFERENCES `Spy`.`SPY` (`Spy_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `HS_Unit_id`
    FOREIGN KEY (`Unit_id`)
    REFERENCES `Spy`.`UNIT` (`Unit_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`ALIAS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`ALIAS` (
  `Spy_code_name` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `Occupation` VARCHAR(45) NULL,
  PRIMARY KEY (`Spy_code_name`),
  CONSTRAINT `AL_Spy_code_name`
    FOREIGN KEY (`Spy_code_name`)
    REFERENCES `Spy`.`SPY` (`Spy_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`OTHER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`OTHER` (
  `Agent_id` INT NOT NULL,
  `Occupation` VARCHAR(45) NULL,
  PRIMARY KEY (`Agent_id`),
  CONSTRAINT `OT_Agent_id`
    FOREIGN KEY (`Agent_id`)
    REFERENCES `Spy`.`Agent` (`Agent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Spy`.`GADGET`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`GADGET` (
  `Service_tag` INT NOT NULL,
  `Cost` INT NULL,
  `Description` VARCHAR(45) NULL,
  `Agent_id` INT NULL,
  PRIMARY KEY (`Service_tag`),
  INDEX `Agent_id_idx` (`Agent_id` ASC) VISIBLE,
  CONSTRAINT `G_Agent_id`
    FOREIGN KEY (`Agent_id`)
    REFERENCES `Spy`.`AGENT` (`Agent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`FOREIGN SPY ORGANIZATION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`FOREIGN_SPY_ORGANIZATION` (
  `Org_name` VARCHAR(45) NOT NULL,
  `Origin` VARCHAR(45) NULL,
  `Relationship` VARCHAR(45) NULL,
  PRIMARY KEY (`Org_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`FOREIGN SPY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`FOREIGN_SPY` (
  `Spy_code_name` VARCHAR(45) NOT NULL,
  `Org_name` VARCHAR(45) NULL,
  PRIMARY KEY (`Spy_code_name`),
  INDEX `Org_name_idx` (`Org_name` ASC) VISIBLE,
  CONSTRAINT `FS_Spy_code_name`
    FOREIGN KEY (`Spy_code_name`)
    REFERENCES `Spy`.`SPY` (`Spy_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FS_Org_name`
    FOREIGN KEY (`Org_name`)
    REFERENCES `Spy`.`FOREIGN_SPY_ORGANIZATION` (`Org_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`COMMON LOCATION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`COMMON_LOCATION` (
  `Target_code_name` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NULL,
  PRIMARY KEY (`Target_code_name`),
  CONSTRAINT `CL_Target_code_name`
    FOREIGN KEY (`Target_code_name`)
    REFERENCES `Spy`.`TARGET` (`Target_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`TARGET SIGHTING`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`TARGET_SIGHTING` (
  `Target_code_name` VARCHAR(45) NOT NULL,
  `Date` DATE NULL,
  `Address` VARCHAR(45) NULL,
  PRIMARY KEY (`Target_code_name`),
  CONSTRAINT `TS_Target_ code_name`
    FOREIGN KEY (`Target_code_name`)
    REFERENCES `Spy`.`TARGET` (`Target_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`FOREIGN SPY SIGHTING`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`FOREIGN_SPY_SIGHTING` (
  `Spy_code_name` VARCHAR(45) NOT NULL,
  `Date` DATE NULL,
  `Address` VARCHAR(45) NULL,
  PRIMARY KEY (`Spy_code_name`),
  CONSTRAINT `FSS_Spy_code_name`
    FOREIGN KEY (`Spy_code_name`)
    REFERENCES `Spy`.`SPY` (`Spy_code_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`OPERATOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`OPERATOR` (
  `Agent_id` INT NOT NULL,
  `Unit_id` INT NULL,
  PRIMARY KEY (`Agent_id`),
  INDEX `Unit_id_idx` (`Unit_id` ASC) VISIBLE,
  CONSTRAINT `O_Agent_id`
    FOREIGN KEY (`Agent_id`)
    REFERENCES `Spy`.`AGENT` (`Agent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `O_Unit_id`
    FOREIGN KEY (`Unit_id`)
    REFERENCES `Spy`.`UNIT` (`Unit_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Spy`.`MEANS OF CONTACT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Spy`.`MEANS_OF_CONTACT` (
  `Agent_id` INT NOT NULL,
  `Contact_line` INT NULL,
  `Sattelite_link_address` VARCHAR(45) NULL,
  `Delivery_point` VARCHAR(45) NULL,
  PRIMARY KEY (`Agent_id`),
  CONSTRAINT `MOC_Agent_id`
    FOREIGN KEY (`Agent_id`)
    REFERENCES `Spy`.`AGENT` (`Agent_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
