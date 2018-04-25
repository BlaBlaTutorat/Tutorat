-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 12 avr. 2018 à 08:00
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
  PRIMARY KEY (`NOM`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `classes`
--

INSERT INTO `classes` (`NOM`) VALUES
('1ES1'),
('1ES2'),
('1ES3'),
('1L1'),
('1LES'),
('1S1'),
('1S2'),
('1S3'),
('1S4'),
('1S5'),
('2G01'),
('2G02'),
('2G03'),
('2G04'),
('2G05'),
('2G06'),
('2G07'),
('2G08'),
('2G09'),
('2G10'),
('2G11'),
('ADMIN'),
('BCPST1'),
('BCPST2'),
('ECE1'),
('ECE2'),
('ECS1'),
('ECS2'),
('HK1'),
('HK2'),
('KH'),
('MP'),
('MPSI1'),
('MPSI2'),
('MPX'),
('PC'),
('PCSI1'),
('PCSI2'),
('PCX'),
('PSI'),
('TES1'),
('TES2'),
('TES3'),
('TL-ES'),
('TL1'),
('TS1'),
('TS2'),
('TS3'),
('TS4'),
('TS5'),
('UPE2A');

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
  `debut_j0` time DEFAULT NULL,
  `fin_j0` time DEFAULT NULL,
  `debut_j1` time DEFAULT NULL,
  `fin_j1` time DEFAULT NULL,
  `debut_j2` time DEFAULT NULL,
  `fin_j2` time DEFAULT NULL,
  `debut_j3` time DEFAULT NULL,
  `fin_j3` time DEFAULT NULL,
  `debut_j4` time DEFAULT NULL,
  `fin_j4` time DEFAULT NULL,
  `debut_j5` time DEFAULT NULL,
  `fin_j5` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `demandes`
--

INSERT INTO `demandes` (`id`, `auteur`, `classe`, `matiere`, `date_time`, `tuteur`, `disponible`, `debut_j0`, `fin_j0`, `debut_j1`, `fin_j1`, `debut_j2`, `fin_j2`, `debut_j3`, `fin_j3`, `debut_j4`, `fin_j4`, `debut_j5`, `fin_j5`) VALUES
(1, 'antoinelabarussias@orange.fr', 'TS5', 'LATIN', '2018-04-12 09:59:06', NULL, 1, NULL, NULL, '14:00:00', '14:30:00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'taotom63@gmail.com', 'TS5', 'PHILOSOPHIE', '2018-04-12 10:00:09', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '08:00:00', '09:00:00');

-- --------------------------------------------------------
CREATE TABLE `filieres` (
  `nom` varchar(50) NOT NULL,
  `classement` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Contenu de la table `filieres`
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
  `debut_j0` time DEFAULT NULL,
  `fin_j0` time DEFAULT NULL,
  `debut_j1` time DEFAULT NULL,
  `fin_j1` time DEFAULT NULL,
  `debut_j2` time DEFAULT NULL,
  `fin_j2` time DEFAULT NULL,
  `debut_j3` time DEFAULT NULL,
  `fin_j3` time DEFAULT NULL,
  `debut_j4` time DEFAULT NULL,
  `fin_j4` time DEFAULT NULL,
  `debut_j5` time DEFAULT NULL,
  `fin_j5` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `offres`
--

INSERT INTO `offres` (`id`, `auteur`, `filiere`, `matiere`, `date_time`, `participant`, `participant2`, `disponible`, `debut_j0`, `fin_j0`, `debut_j1`, `fin_j1`, `debut_j2`, `fin_j2`, `debut_j3`, `fin_j3`, `debut_j4`, `fin_j4`, `debut_j5`, `fin_j5`) VALUES
(1, 'marco.desmoulins@lilo.org', 'Terminale S', 'MATHEMATIQUES', '2018-02-22 00:00:00', 'antoinelabarussias@orange.fr', 'taotom63@gmail.com', 1, '08:00:00', '09:00:00', '16:00:00', '17:00:00', '14:00:00', '16:00:00', NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'taotom63@gmail.com', 'Terminale S', 'ISN', '2018-02-19 14:15:41', 'marco.desmoulins@lilo.org', NULL, 1, '15:00:00', '16:00:00', NULL, NULL, NULL, NULL, '09:00:00', '10:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(3, 'antoinelabarussias@orange.fr', 'Terminale S', 'SCIENCES INGENIEUR', '2018-02-22 00:00:00', 'taotom63@gmail.com', NULL, 1, '13:00:00', '14:00:00', '17:00:00', '18:00:00', NULL, NULL, '14:00:00', '15:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(4, 'antoinelabarussias@orange.fr', 'Seconde', 'FRANCAIS', '2018-02-22 00:00:00', NULL, NULL, 0, '08:00:00', '10:00:00', '11:00:00', '13:00:00', NULL, NULL, '15:00:00', '16:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(5, 'antoinelabarussias@orange.fr', 'Terminale S', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, '10:00:00', '11:00:00', NULL, NULL, NULL, NULL, '08:00:00', '09:00:00', NULL, NULL, NULL, NULL),
(6, 'antoinelabarussias@orange.fr', 'Première S', 'SCIENCES INGENIEUR', '2018-02-22 00:00:00', NULL, NULL, 1, '15:00:00', '16:00:00', NULL, NULL, '17:00:00', '18:00:00', '10:00:00', '11:00:00', NULL, NULL, '09:00:00', '10:00:00');

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
('Admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin@tutorat.fr', 'ADMIN', 0),
('Antoine Labarussias', '1f0dea80a1af4eefa352c04bdaaa79f79433a7b458aaeaa927cb73ac9f63326a', 'antoinelabarussias@orange.fr', 'TS5', 0),
('Marco Desmoulins', '7c8ccc86c11654af029457d90fdd9d013ce6fb011ee8fdb1374832268cc8d967', 'marco.desmoulins@lilo.org', 'TS5', 0),
('Tao Blancheton', 'e07f52f45ffcfe004432b8f96fbe401378c255fbae4ad87ee64cff0cb8a77227', 'taotom63@gmail.com', 'TS5', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
