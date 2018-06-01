-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 01 juin 2018 à 22:19
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `demandes`
--

INSERT INTO `demandes` (`id`, `auteur`, `classe`, `matiere`, `date_time`, `tuteur`, `disponible`, `horaires`) VALUES
(1, 'antoinelabarussias@orange.fr', 'TS5', 'LATIN', '2018-04-12 09:59:06', NULL, 1, '110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `offres`
--

INSERT INTO `offres` (`id`, `auteur`, `filiere`, `matiere`, `date_time`, `participant`, `participant2`, `disponible`, `horaires`) VALUES
(1, 'marco.desmoulins@lilo.org', 'Terminale S', 'MATHEMATIQUES', '2018-02-22 00:00:00', 'antoinelabarussias@orange.fr', NULL, 1, '110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
(3, 'antoinelabarussias@orange.fr', 'Terminale S', 'SCIENCES INGENIEUR', '2018-02-22 00:00:00', NULL, NULL, 1, '110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
(4, 'antoinelabarussias@orange.fr', 'Seconde', 'FRANCAIS', '2018-02-22 00:00:00', NULL, NULL, 0, '110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
(5, 'antoinelabarussias@orange.fr', 'Terminale S', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, '110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
(6, 'antoinelabarussias@orange.fr', 'Première S', 'SCIENCES INGENIEUR', '2018-02-22 00:00:00', NULL, NULL, 1, '110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000');

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
('Admin', 'e094c2e2b01827b369b77c505653983e95ea8886b86ea924884075ee55c97064', 'admin@tutorat.fr', 'ADMIN', 0),
('Antoine Labarussias', '1f0dea80a1af4eefa352c04bdaaa79f79433a7b458aaeaa927cb73ac9f63326a', 'antoinelabarussias@orange.fr', 'TS5', 0),
('Marco Desmoulins', '7c8ccc86c11654af029457d90fdd9d013ce6fb011ee8fdb1374832268cc8d967', 'marco.desmoulins@lilo.org', 'TS5', 0),
('Tao Mesnard', 'f5b761a6e115564c7770181c7f4c02b4994b9565a66cfeb379d93a4c7d08608f', 'taotom63@gmail.com', '1ES1', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
