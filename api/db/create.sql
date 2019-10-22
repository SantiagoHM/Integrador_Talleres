CREATE TABLE `evergreen`.`mediciones_` (
  `fecha` VARCHAR(30) NOT NULL,
  `origen` VARCHAR(30) NOT NULL,
  `valor` INT(10) NOT NULL,
  `codigoSensor` INT(10) NOT NULL,
  `observacion` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`fecha`));
