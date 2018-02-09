-- phpMyAdmin SQL Dump
-- version 4.2.12deb2+deb8u2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Ven 09 Février 2018 à 10:37
-- Version du serveur :  5.5.59-0+deb8u1
-- Version de PHP :  5.6.33-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `tutorat`
--

-- --------------------------------------------------------

--
-- Structure de la table `classes`
--

CREATE TABLE IF NOT EXISTS `classes` (
`id` int(11) NOT NULL,
  `niveau` varchar(50) NOT NULL,
  `specialites` varchar(50) NOT NULL,
  `numero` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Contenu de la table `classes`
--

INSERT INTO `classes` (`id`, `niveau`, `specialites`, `numero`) VALUES
(1, 'Terminale', 'Scientifique', 5);

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

CREATE TABLE IF NOT EXISTS `matieres` (
  `nom` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `matieres`
--

INSERT INTO `matieres` (`nom`) VALUES
('Français'),
('ISN'),
('Mathématiques'),
('Science de l''ingénieur');

-- --------------------------------------------------------

--
-- Structure de la table `niveaux`
--

CREATE TABLE IF NOT EXISTS `niveaux` (
`id` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Contenu de la table `niveaux`
--

INSERT INTO `niveaux` (`id`, `nom`) VALUES
(1, 'Seconde'),
(2, 'Première'),
(3, 'Terminale'),
(4, 'CPGE première année'),
(5, 'CPGE deuxième année');

-- --------------------------------------------------------

--
-- Structure de la table `offres`
--

CREATE TABLE IF NOT EXISTS `offres` (
`id` int(11) NOT NULL,
  `auteur` varchar(50) NOT NULL,
  `niveau` varchar(15) NOT NULL,
  `matiere` varchar(15) NOT NULL,
  `date_time` datetime NOT NULL COMMENT 'date de la demande',
  `participant` varchar(50) NOT NULL,
  `participant2` varchar(50) DEFAULT NULL,
  `disponible` tinyint(1) NOT NULL DEFAULT '0',
  `debut_j1` time DEFAULT NULL,
  `fin_j1` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `specialites`
--

CREATE TABLE IF NOT EXISTS `specialites` (
  `nom` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `specialites`
--

INSERT INTO `specialites` (`nom`) VALUES
('Economique et sociale'),
('Littéraire'),
('Scientifique');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `nom` varchar(50) NOT NULL DEFAULT '',
  `mdp` varchar(15) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `niveau` varchar(15) NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Contenu de la table `users`
--

INSERT INTO `users` (`nom`, `mdp`, `mail`, `niveau`, `admin`) VALUES
('ced', '', '', '', 0),
('olivier', '', '', '', 0);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `classes`
--
ALTER TABLE `classes`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `matieres`
--
ALTER TABLE `matieres`
 ADD PRIMARY KEY (`nom`);

--
-- Index pour la table `niveaux`
--
ALTER TABLE `niveaux`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `offres`
--
ALTER TABLE `offres`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `specialites`
--
ALTER TABLE `specialites`
 ADD PRIMARY KEY (`nom`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
 ADD PRIMARY KEY (`nom`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `classes`
--
ALTER TABLE `classes`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `niveaux`
--
ALTER TABLE `niveaux`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT pour la table `offres`
--
ALTER TABLE `offres`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
