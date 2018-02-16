-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  ven. 16 fév. 2018 à 15:57
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `niveau` varchar(50) NOT NULL,
  `filiere` varchar(15) NOT NULL,
  `numero` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `classes`
--

INSERT INTO `classes` (`id`, `niveau`, `filiere`, `numero`) VALUES
(1, 'Terminale', 'S', 5);

-- --------------------------------------------------------

--
-- Structure de la table `filieres`
--

DROP TABLE IF EXISTS `filieres`;
CREATE TABLE IF NOT EXISTS `filieres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `filieres`
--

INSERT INTO `filieres` (`id`, `nom`) VALUES
(1, 'Aucune filière (2nd)'),
(2, 'S'),
(3, 'ES'),
(4, 'L'),
(5, 'MPSI'),
(6, 'PCSI'),
(7, 'MP'),
(8, 'MP*'),
(9, 'PSI'),
(10, 'PC'),
(11, 'PC*'),
(12, 'BCPST'),
(13, 'ECE'),
(14, 'ECS'),
(15, 'HK/K');

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

DROP TABLE IF EXISTS `matieres`;
CREATE TABLE IF NOT EXISTS `matieres` (
  `nom` varchar(50) NOT NULL,
  PRIMARY KEY (`nom`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `matieres`
--

INSERT INTO `matieres` (`nom`) VALUES
('(Spé) Grec'),
('(Spé) Latin'),
('Allemand'),
('Anglais'),
('CAV'),
('Chinois'),
('Espagnol'),
('Français'),
('Histoire-Géographie'),
('ISN'),
('Littérature'),
('Littérature en langue vivante étrangère'),
('LVA'),
('Mathématiques'),
('Philosophie'),
('Physique-Chime'),
('Russe'),
('Sciences'),
('SES'),
('SI'),
('Spé Eco'),
('Spé Maths'),
('Spé Physique'),
('Spé Sciences sociales et politiques'),
('Spé SVT'),
('SVT');

-- --------------------------------------------------------

--
-- Structure de la table `niveaux`
--

DROP TABLE IF EXISTS `niveaux`;
CREATE TABLE IF NOT EXISTS `niveaux` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `niveaux`
--

INSERT INTO `niveaux` (`id`, `nom`) VALUES
(1, 'Seconde'),
(2, 'Première'),
(3, 'Terminale'),
(4, 'CPGE 1ère année'),
(5, 'CPGE 2ème année');

-- --------------------------------------------------------

--
-- Structure de la table `offres`
--

DROP TABLE IF EXISTS `offres`;
CREATE TABLE IF NOT EXISTS `offres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `auteur` varchar(50) NOT NULL,
  `niveau` varchar(30) NOT NULL,
  `filiere` varchar(30) NOT NULL,
  `matiere` varchar(30) NOT NULL,
  `date_time` datetime NOT NULL COMMENT 'date de la demande',
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
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 7
  DEFAULT CHARSET = utf8;

--
-- Déchargement des données de la table `offres`
--

INSERT INTO `offres` (`id`, `auteur`, `niveau`, `filiere`, `matiere`, `date_time`, `participant`, `participant2`, `disponible`, `debut_j0`, `fin_j0`, `debut_j1`, `fin_j1`, `debut_j2`, `fin_j2`, `debut_j3`, `fin_j3`, `debut_j4`, `fin_j4`, `debut_j5`, `fin_j5`) VALUES
  (1, 'Marco Desmoulins', 'Terminale', 'S', 'Mathématiques', '2018-02-22 00:00:00', NULL, NULL, 1, '08:00:00',
      '09:00:00', '16:00:00', '17:00:00', '14:00:00', '16:00:00', NULL, NULL, NULL, NULL, NULL, NULL),
  (2, 'Tao Blancheton', 'Terminale', 'S', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, '15:00:00', '16:00:00', NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               '09:00:00',
                                                                                                               '10:00:00',
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               '08:00:00',
                                                                                                               '09:00:00'),
  (3, 'Antoine Labarussias', 'Terminale', 'S', 'SI', '2018-02-22 00:00:00', NULL, NULL, 1, '13:00:00', '14:00:00',
    '17:00:00', '18:00:00', NULL, NULL, '14:00:00', '15:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(4, 'Jean Kévin', 'Seconde', 'Aucune filière (2nd)', 'Français', '2018-02-22 00:00:00', NULL, NULL, 1, '08:00:00', '10:00:00', '11:00:00', '13:00:00', NULL, NULL, '15:00:00', '16:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(5, 'Alexis Ducont', 'Première', 'L', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, '10:00:00', '11:00:00', NULL, NULL, NULL, NULL, '08:00:00', '09:00:00', NULL, NULL, NULL, NULL),
  (6, 'Lola Blachard', 'Seconde', 'Aucune filière (2nd)', 'SI', '2018-02-22 00:00:00', NULL, NULL, 1, '15:00:00',
      '16:00:00', NULL, NULL, '17:00:00', '18:00:00', '10:00:00', '11:00:00', NULL, NULL, '09:00:00', '10:00:00');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `nom` varchar(50) NOT NULL DEFAULT '',
  `mdp` varchar(15) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `niveau` varchar(15) NOT NULL,
  `filiere` varchar(15) NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  `ban` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`nom`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`nom`, `mdp`, `mail`, `niveau`, `filiere`, `admin`, `ban`) VALUES
('Antoine Labarussias', 'antoine', 'antoinelabarussias@orange.fr', 'Terminale', 'S', 1, 0),
('Marco Desmoulins', 'marco', 'markopelo@gmail.com', 'Terminale', 'S', 1, 0),
('Tao Blancheton', 'tao', 'taotom63@gmail.com', 'Terminale', 'S', 1, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;