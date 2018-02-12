-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  lun. 12 fév. 2018 à 12:59
-- Version du serveur :  5.7.19
-- Version de PHP :  5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
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
  `id`      INT(11)     NOT NULL AUTO_INCREMENT,
  `niveau`  VARCHAR(50) NOT NULL,
  `filiere` VARCHAR(15) NOT NULL,
  `numero`  INT(11)     NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 2
  DEFAULT CHARSET = utf8;

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
  `id`  INT(11)     NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 16
  DEFAULT CHARSET = utf8;

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
  `nom` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`nom`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

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
  ('Mathèmatiques'),
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
  `id`  INT(11)     NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 6
  DEFAULT CHARSET = utf8;

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
  `id`           INT(11)     NOT NULL AUTO_INCREMENT,
  `auteur`       VARCHAR(50) NOT NULL,
  `niveau`       VARCHAR(30) NOT NULL,
  `filiere`      VARCHAR(30) NOT NULL,
  `matiere`      VARCHAR(30) NOT NULL,
  `date_time`    DATETIME    NOT NULL
  COMMENT 'date de la demande',
  `participant`  VARCHAR(50)          DEFAULT NULL,
  `participant2` VARCHAR(50)          DEFAULT NULL,
  `disponible`   TINYINT(1)  NOT NULL DEFAULT '0',
  `debut_j1`     TIME                 DEFAULT NULL,
  `fin_j1`       TIME                 DEFAULT NULL,
  `debut_j2`     TIME                 DEFAULT NULL,
  `fin_j2`       TIME                 DEFAULT NULL,
  `debut_j3`     TIME                 DEFAULT NULL,
  `fin_j3`       TIME                 DEFAULT NULL,
  `debut_j4`     TIME                 DEFAULT NULL,
  `fin_j4`       TIME                 DEFAULT NULL,
  `debut_j5`     TIME                 DEFAULT NULL,
  `fin_j5`       TIME                 DEFAULT NULL,
  `debut_j6`     TIME                 DEFAULT NULL,
  `fin_j6`       TIME                 DEFAULT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 7
  DEFAULT CHARSET = utf8;

--
-- Déchargement des données de la table `offres`
--

INSERT INTO `offres` (`id`, `auteur`, `niveau`, `filiere`, `matiere`, `date_time`, `participant`, `participant2`, `disponible`, `debut_j1`, `fin_j1`, `debut_j2`, `fin_j2`, `debut_j3`, `fin_j3`, `debut_j4`, `fin_j4`, `debut_j5`, `fin_j5`, `debut_j6`, `fin_j6`)
VALUES
  (1, 'Marco Desmoulins', 'Terminale', 'S', 'Mathématiques', '2018-02-22 00:00:00', NULL, NULL, 1, NULL, NULL, NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL,
                                                                                                               NULL),
  (2, 'Tao Blancheton', 'Terminale', 'S', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL,
                                                                                                   NULL, NULL, NULL,
                                                                                                   NULL, NULL, NULL,
                                                                                                   NULL),
  (3, 'Antoine Labarussias', 'Terminale', 'S', 'Science de l\'ingénieur', '2018-02-22 00:00:00', NULL, NULL, 1, NULL,
      NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
  (4, 'Jean Kévin', 'Seconde', 'Aucune filière (2nd)', 'Français', '2018-02-22 00:00:00', NULL, NULL, 1, NULL, NULL,
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
  (5, 'Alexis Ducont', 'Première', 'L', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL,
                                                                                                 NULL, NULL, NULL, NULL,
                                                                                                 NULL, NULL),
  (6, 'Lola Blachard', 'Seconde', 'Aucune filière (2nd)', 'Science de l\'ingénieur', '2018-02-22 00:00:00', NULL, NULL,
      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `nom`     VARCHAR(50) NOT NULL DEFAULT '',
  `mdp`     VARCHAR(15) NOT NULL,
  `mail`    VARCHAR(50) NOT NULL,
  `niveau`  VARCHAR(15) NOT NULL,
  `filiere` VARCHAR(15) NOT NULL,
  `admin`   TINYINT(1)  NOT NULL DEFAULT '0',
  `ban`     TINYINT(1)  NOT NULL DEFAULT '0',
  PRIMARY KEY (`nom`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`nom`, `mdp`, `mail`, `niveau`, `filiere`, `admin`, `ban`) VALUES
  ('Jean Kévin', 'mdp', 'jk@gmail.com', 'Terminale', 'S', 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
