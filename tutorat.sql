-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 02 juin 2018 à 13:44
-- Version du serveur :  5.7.19
-- Version de PHP :  5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `tutorat`
--

-- --------------------------------------------------------

--
-- Structure de la table `classes`
--

DROP TABLE IF EXISTS `classes`;
CREATE TABLE IF NOT EXISTS `classes` (
  `NOM` varchar(6) NOT NULL,
  `classement` int(11) NOT NULL,
  PRIMARY KEY (`NOM`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `classes`
--

INSERT INTO `classes` (`NOM`, `classement`) VALUES
('1ES1', 1),
('1ES2', 1),
('1ES3', 1),
('1L1', 1),
('1LES', 1),
('1S1', 1),
('1S2', 1),
('1S3', 1),
('1S4', 1),
('1S5', 1),
('2G01', 0),
('2G02', 0),
('2G03', 0),
('2G04', 0),
('2G05', 0),
('2G06', 0),
('2G07', 0),
('2G08', 0),
('2G09', 0),
('2G10', 0),
('2G11', 0),
('ADMIN', 2000),
('BCPST1', 3),
('BCPST2', 3),
('ECE1', 3),
('ECE2', 3),
('ECS1', 3),
('ECS2', 3),
('HK1', 3),
('HK2', 3),
('KH', 4),
('MP', 4),
('MPSI1', 3),
('MPSI2', 3),
('MPX', 4),
('PC', 4),
('PCSI1', 3),
('PCSI2', 3),
('PCX', 4),
('PSI', 4),
('TES1', 2),
('TES2', 2),
('TES3', 2),
('TL-ES', 2),
('TL1', 2),
('TS1', 2),
('TS2', 2),
('TS3', 2),
('TS4', 2),
('TS5', 2),
('UPE2A', 0);

-- --------------------------------------------------------

--
-- Structure de la table `demandes`
--

DROP TABLE IF EXISTS `demandes`;
CREATE TABLE IF NOT EXISTS `demandes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `auteur` varchar(50) NOT NULL,
  `classe` varchar(30) NOT NULL,
  `matiere` varchar(30) NOT NULL,
  `date_time` datetime NOT NULL,
  `tuteur` varchar(50) DEFAULT NULL,
  `disponible` tinyint(1) NOT NULL DEFAULT '0',
  `horaires` varchar(300) NOT NULL DEFAULT '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `filieres`
--

DROP TABLE IF EXISTS `filieres`;
CREATE TABLE IF NOT EXISTS `filieres` (
  `nom` varchar(50) NOT NULL,
  `classement` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `filieres`
--

INSERT INTO `filieres` (`nom`, `classement`) VALUES
('CPGE ECE', 3),
('CPGE ECS', 3),
('CPGE HK', 3),
('CPGE KH', 4),
('CPGE MP', 4),
('CPGE MP*', 4),
('CPGE MPSI', 3),
('CPGE PC', 4),
('CPGE PC*', 4),
('CPGE PCSI', 3),
('CPGE PSI', 4),
('Première ES', 1),
('Première L', 1),
('Première S', 1),
('Seconde', 0),
('Terminale ES', 2),
('Terminale L', 2),
('Terminale S', 2);

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

DROP TABLE IF EXISTS `matieres`;
CREATE TABLE IF NOT EXISTS `matieres` (
  `LIBELLE` varchar(27) NOT NULL,
  PRIMARY KEY (`LIBELLE`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `matieres`
--

INSERT INTO `matieres` (`LIBELLE`) VALUES
('ALLEMAND EURO'),
('ALLEMAND LV1'),
('ALLEMAND LV2'),
('ANGLAIS EURO 1'),
('ANGLAIS LV1'),
('ANGLAIS LV2'),
('BIA'),
('CHINOIS LV1'),
('CHINOIS LV2'),
('ESPAGNOL LV1'),
('ESPAGNOL LV2'),
('FRANCAIS'),
('GREC ANCIEN'),
('HISTOIRE-GEOGRAPHIE'),
('ISN'),
('ITALIEN EURO'),
('ITALIEN LV1'),
('ITALIEN LV2'),
('LATIN'),
('LITTER.ETRANG.EN LVE'),
('LITTERATURE'),
('MATH. SPE'),
('MATHEMATIQUES'),
('PHILOSOPHIE'),
('PHYSIQUE-CHIMIE'),
('RUSSE LV3'),
('SC. ECONO.& SOCIALES'),
('SC. SOCIALES ET POLITIQUE'),
('SCIENCES'),
('SCIENCES INGENIEUR'),
('SCIENCES VIE & TERRE');

-- --------------------------------------------------------

--
-- Structure de la table `offres`
--

DROP TABLE IF EXISTS `offres`;
CREATE TABLE IF NOT EXISTS `offres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `auteur` varchar(50) NOT NULL,
  `filiere` varchar(30) NOT NULL,
  `matiere` varchar(30) NOT NULL,
  `date_time` datetime NOT NULL,
  `participant` varchar(50) DEFAULT NULL,
  `participant2` varchar(50) DEFAULT NULL,
  `disponible` tinyint(1) NOT NULL DEFAULT '0',
  `horaires` varchar(300) NOT NULL DEFAULT '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `register`
--

DROP TABLE IF EXISTS `register`;
CREATE TABLE IF NOT EXISTS `register` (
  `nom` varchar(50) NOT NULL,
  `mdp` varchar(1000) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `classe` varchar(50) NOT NULL,
  `code` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `nom` varchar(50) NOT NULL,
  `mdp` varchar(1000) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `classe` varchar(50) NOT NULL,
  `ban` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`nom`, `mdp`, `mail`, `classe`, `ban`) VALUES
('Admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin@tutorat.fr', 'ADMIN', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
