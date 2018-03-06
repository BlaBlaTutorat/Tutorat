-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  Dim 04 mars 2018 à 11:15
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
  `NUMERO` int(2) DEFAULT NULL,
  `IDENT` int(2) DEFAULT NULL,
  `NOM` varchar(6) DEFAULT NULL,
  `EFFECTIF` int(2) DEFAULT NULL,
  `NIVEAU` varchar(11) DEFAULT NULL,
  `NOTATION` varchar(13) DEFAULT NULL,
  `ETABLISSEMENT` varchar(39) DEFAULT NULL,
  `PRINCIPAUX` varchar(28) DEFAULT NULL,
  `BULLETIN` varchar(14) DEFAULT NULL,
  `RELEVE` varchar(8) DEFAULT NULL,
  `CONSEIL` varchar(10) DEFAULT NULL,
  `FILIERE` varchar(10) DEFAULT NULL,
  `IDONDE` varchar(10) DEFAULT NULL,
  `COMPETENCE` varchar(137) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `classes`
--

INSERT INTO `classes` (`NUMERO`, `IDENT`, `NOM`, `EFFECTIF`, `NIVEAU`, `NOTATION`, `ETABLISSEMENT`, `PRINCIPAUX`, `BULLETIN`, `RELEVE`, `CONSEIL`, `FILIERE`, `IDONDE`, `COMPETENCE`) VALUES
(1, 2, '1ES1', 34, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme BRUNET BEATRICE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(2, 57, '1ES2', 34, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme COMBY AGNES', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(3, 78, '1ES3', 30, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme LEGENDRE ISABELLE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(4, 6, '1L1', 30, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BERTINELLI PHILIPPE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(5, 79, '1LES', 33, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. SABATIER SYLVAIN', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(6, 80, '1S1', 36, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme BONNEROT EVELYNE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(7, 8, '1S2', 35, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BEGGIORA JEAN-PAUL', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(8, 9, '1S3', 35, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme GOUHIER ARMELLE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(9, 10, '1S4', 36, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme FAURE ANNE-MARIE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(10, 11, '1S5', 35, '1ERE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. MANHES JEAN MARC', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(11, 13, '2G01', 37, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BUISSON CLEMENT', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(12, 14, '2G02', 37, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme CRISTINA ANNIE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(13, 15, '2G03', 36, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. MOREAU PHILIPPE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(14, 16, '2G04', 35, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme COURTINAT SOPHIE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(15, 17, '2G05', 35, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. CITRON NICOLAS', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(16, 18, '2G06', 35, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme AMARIDON ESTELLE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(17, 19, '2G07', 34, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BOURRACHOT LUDOVIC', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(18, 20, '2G08', 34, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme PASTRE HELENE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(19, 21, '2G09', 35, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme ROHET FLORENCE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(20, 22, '2G10', 34, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. SERVOIR JEAN LOUIS', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(21, 82, '2G11', 35, '2NDE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme LE BARS VIRGINIE', '2G NOULIN', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(22, 25, 'BCPST1', 48, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. CLAMENS ALEX', '', 'Standard', '', '', '', ''),
(23, 26, 'BCPST2', 46, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. CARIOU FRANCOIS', '', 'Standard', '', '', '', ''),
(24, 27, 'ECE1', 48, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BONNET OLIVIER', '', 'Standard', '', '', '', ''),
(25, 28, 'ECE2', 38, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. SADOURNY MATHIEU', '', 'Standard', '', '', '', ''),
(26, 29, 'ECS1', 28, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. CHASSANIOL ARTHUR', '', 'Standard', '', '', '', ''),
(27, 30, 'ECS2', 35, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme CHABERT CHARLOTTE', '', 'Standard', '', '', '', ''),
(28, 31, 'HK1', 93, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BEDOUELLE THIERRY', '', 'Standard', '', '', '', ''),
(29, 32, 'HK2', 46, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. TISSUT ALAIN', '', 'Standard', '', '', '', ''),
(30, 33, 'KH', 42, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme CABIROL - LACAN BRIGITTE', '', 'Standard', '', '', '', ''),
(31, 34, 'MP', 33, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BALAVOINE DAVID', '', 'Standard', '', '', '', ''),
(32, 35, 'MPSI1', 93, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. DERVIEUX JEAN', '', 'Standard', '', '', '', ''),
(33, 36, 'MPSI2', 45, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. MERTENS MICHEL', '', 'Standard', '', '', '', ''),
(34, 37, 'MPX', 36, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. CANONICO FERNAND', '', 'Standard', '', '', '', ''),
(35, 38, 'PC', 32, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BRUN THIERRY', '', 'Standard', '', '', '', ''),
(36, 63, 'PCSI1', 97, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme SITZ CARMONA NATHALIE', '', 'Standard', '', '', '', ''),
(37, 62, 'PCSI2', 48, 'CPGE1', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. SCHAFTER OLIVIER', '', 'Standard', '', '', '', ''),
(38, 41, 'PCX', 36, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. HADROT SIMON', '', 'Standard', '', '', '', ''),
(39, 42, 'PSI', 39, 'CPGE2', 'Semestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. MALLORDY JEAN FRANCOIS', '', 'Standard', '', '', '', ''),
(40, 43, 'TES1', 35, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. FAYE PASCAL', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(41, 48, 'TES2', 34, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. HAEIN RICHARD', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(42, 83, 'TES3', 34, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. SZYMANSKI JEAN', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(43, 46, 'TL1', 38, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme CHEIX NATHALIE', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(44, 86, 'TL-ES', 37, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. ROUGERIE OLIVIER', '1° BOUSSAHBA', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(45, 49, 'TS1', 31, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme MOIGNOUX MARIE', 'TERM TOURNADRE', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(46, 81, 'TS2', 37, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme LONGUET NICOLE', 'TERM TOURNADRE', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(47, 50, 'TS3', 33, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme LAVEST SYLVIE', 'TERM TOURNADRE', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(48, 51, 'TS4', 29, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'Mme SAINFORT AUDE', 'TERM TOURNADRE', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(49, 52, 'TS5', 35, 'TERMINALE', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', 'M. BUISSON PHILIPPE', 'TERM TOURNADRE', 'Standard', '', '', '', 'Langues étrangères et régionales (Lycée),Langages mathématiques, scientifiques et informatiques (Lycée),COMPETENCES TRANSVERSALES (Lycée)'),
(50, 87, 'UPE2A', 13, 'Non désigné', 'Trimestrielle', 'LYCEE BLAISE PASCAL LYCEE BLAISE PASCAL', '', 'Sans Notes', 'Standard', '', '', '', '');

-- --------------------------------------------------------

--
-- Structure de la table `filieres`
--

DROP TABLE IF EXISTS `filieres`;
CREATE TABLE IF NOT EXISTS `filieres` (
  `nom` varchar(50) NOT NULL,
  PRIMARY KEY (`nom`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `filieres`
--

INSERT INTO `filieres` (`nom`) VALUES
('CPGE ECE'),
('CPGE ECS'),
('CPGE HK'),
('CPGE KH'),
('CPGE MP'),
('CPGE MP*'),
('CPGE MPSI'),
('CPGE PC'),
('CPGE PC*'),
('CPGE PCSI'),
('CPGE PSI'),
('Première ES'),
('Première L'),
('Première S'),
('Seconde'),
('Terminale ES'),
('Terminale L'),
('Terminale S');

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

DROP TABLE IF EXISTS `matieres`;
CREATE TABLE IF NOT EXISTS `matieres` (
  `NUMERO` int(3) DEFAULT NULL,
  `CODE` varchar(18) DEFAULT NULL,
  `LIBELLE` varchar(27) DEFAULT NULL,
  `LIBLONG` varchar(10) DEFAULT NULL,
  `EQUIVALENCE` varchar(27) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `matieres`
--

INSERT INTO `matieres` (`NUMERO`, `CODE`, `LIBELLE`, `LIBLONG`, `EQUIVALENCE`) VALUES
(1, 'ACC. P', 'Acc. Pers. Français', '', 'Acc. Pers. Français'),
(2, 'ACC. P', 'Acc. Pers. HG', '', 'Acc. Pers. HG'),
(3, 'ACC. P', 'Acc. Pers. LV1', '', 'LV1'),
(4, 'ACC. P', 'Acc. Pers. Maths', '', 'Acc. Pers. Maths'),
(5, 'ACC. P', 'Acc. Pers. PC', '', 'Acc. Pers. PC'),
(6, 'ACC. P', 'Acc. Pers. SES', '', 'Acc. Pers. SES'),
(7, 'ACC. P', 'Acc. Pers. SI', '', 'Acc. Pers. SI'),
(8, 'ACC. P', 'Acc. Pers. SVT', '', 'Acc. Pers. SVT'),
(9, 'ACC.PE', 'Acc.Pers. LITT', '', 'Acc.Pers. LITT'),
(10, 'ACC.PE', 'Acc.Pers. Philo', '', 'Acc.Pers. Philo'),
(11, 'AGL4', 'AGL LV RENFORCÉE', '', 'OPTION'),
(12, 'AGL1-2', 'AGL LV1-LV2', '', 'LV2'),
(13, 'AGL LV', 'AGL LVA', '', 'AGL LVA'),
(14, 'AGL LV', 'AGL LVB', '', 'AGL LVB'),
(15, 'ALL1-2', 'ALL LV1-LV2', '', 'LV2'),
(16, 'ALL4', 'ALLD LV RENFORCÉE', '', 'OPTION'),
(17, 'ALLEMA', 'ALLEMAND  ASS.', '', 'Allemand ASS.'),
(18, 'ALL2', 'ALLEMAND 2', '', 'LV2'),
(19, 'ALLEMA', 'ALLEMAND EURO', '', 'ALLEMAND EURO'),
(20, 'ALLEMA', 'ALLEMAND LV A', '', 'ALLEMAND LV A'),
(21, 'ALLEMA', 'ALLEMAND LV B', '', 'ALLEMAND LV B'),
(22, 'ALL1', 'ALLEMAND LV1', '', 'LV1'),
(23, 'ALL2', 'ALLEMAND LV2', '', 'LV2'),
(24, 'ALLEMA', 'ALLEMAND LV2 CNED', '', 'LV2'),
(25, 'E-HSC', 'AN.ECO.HIS.SOC.CONT.', '', 'AN.ECO.HIS.SOC.CONT.'),
(26, 'ANG  C', 'ANG  conc. autres ENS', '', 'ANG  conc. autres ENS'),
(27, 'ANG LV', 'ANG LV1-LV2 COURS COMMUN', '', 'LV2'),
(28, 'ANG PR', 'ANG PREPA LSH', '', 'ANG PREPA LSH'),
(29, 'AGL€', 'ANGLAIS €', '', 'ANGALIS €'),
(30, 'AGL EU', 'ANGLAIS EURO 1', '', 'LV1'),
(31, 'AGL EURO', 'ANGLAIS EURO 1', '', 'LV1'),
(32, 'AGL4', 'ANGLAIS LV APPROFONDIE', '', 'ANGLAIS LV APPROFONDIE'),
(33, 'AGL1', 'ANGLAIS LV1', '', 'LV1'),
(34, 'AGL1-2', 'ANGLAIS LV1-LV2', '', 'LV2'),
(35, 'AGL2', 'ANGLAIS LV2', '', 'LV2'),
(36, 'AGLOPT', 'ANGLAIS OPT', '', 'ANGLAIS OPT'),
(37, 'AGLOPT', 'ANGLAIS OPTION', '', 'ANGLAIS OPT'),
(38, 'ARABE CNED', 'ARABE CNED', '', 'ARABE CNED'),
(39, 'ARABE LV1', 'ARABE LV1', '', 'LV1'),
(40, 'ARA2C', 'ARABE LV2 CORRESP.', '', 'LV2'),
(41, 'ARA3C', 'ARABE LV3 CORRESP.', '', 'LV3'),
(42, 'A-PLA', 'ARTS PLASTIQUES', '', 'ARTS PLASTIQUES'),
(43, 'A-PLA', 'ARTS PLASTIQUES FAC', '', 'ARTS PLASTIQUES'),
(44, 'A-VIS', 'ARTS VISUELS', '', 'ARTS VISUELS'),
(45, 'ASSIST', 'ASSISTANT LV', '', 'ASSISTANT LV'),
(46, 'THEAT', 'ATELIER THEATRE', '', 'ATELIER THEATRE'),
(47, 'ATHLE', 'ATHLETISME', '', 'OPTION EPS'),
(48, 'BIA', 'BIA', '', 'BIA'),
(49, 'BIOLO', 'BIOLOGIE', '', 'BIOLOGIE'),
(50, 'BIOLTP', 'BIOLOGIE TP', '', 'BIOLOGIE TP'),
(51, 'C.D.I.', 'C.D.I.', '', 'C.D.I.'),
(52, 'CHIMI', 'CHIMIE', '', 'PHYSIQUE-CHIMIE'),
(53, 'CHI-2', 'CHIMIE (2E PER.PSI)', '', 'PHYSIQUE-CHIMIE'),
(54, 'CHI-4', 'CHIMIE (4 HEUR.PCSI)', '', 'PHYSIQUE-CHIMIE'),
(55, 'CHI-SI', 'CHIMIE OPT SI', '', 'PHYSIQUE-CHIMIE'),
(56, 'CHIMTD', 'CHIMIE TD', '', 'PHYSIQUE-CHIMIE'),
(57, 'CHIMTP', 'CHIMIE TP', '', 'PHYSIQUE-CHIMIE'),
(58, 'CHI1C', 'CHINOIS LV1 CORRESP.', '', 'LV1'),
(59, 'CHI2', 'CHINOIS LV2', '', 'LV2'),
(60, 'CHI2C', 'CHINOIS LV2 CORRESP.', '', 'LV2'),
(61, 'CHINOIS LV3 CNED', 'CHINOIS LV3 CNED', '', 'CHINOIS LV3 CNED'),
(62, 'CHI3C', 'CHINOIS LV3 CORRESP.', '', 'LV3'),
(63, 'CHORCL', 'CHORALE', '', 'CHORALE  CLG'),
(64, 'CHORAL', 'CHORALE CLG', '', 'CHORALE CLG'),
(65, 'CIAV5', 'CINEMA-AUDIOVIS. 5H', '', 'CINEMA-AUDIOVIS. 5H'),
(66, 'CAV-F', 'CINEMA-AUDIOVIS. FAC', '', 'CINEMA-AUDIOVIS. FAC'),
(67, 'CI-AV', 'CINEMA-AUDIOVISUEL', '', 'CINÉMA-AUDIOVISUEL'),
(68, 'CI-AV', 'CINEMA-AUDIOVISUEL FAC', '', 'OPTION'),
(69, 'CLUB', 'CLUB  DE  MATH', '', 'CLUB  DE  MATH'),
(70, 'COLLE', 'COLLE', '', 'COLLE'),
(71, 'COLLE', 'COLLE ALLLEMAND', '', 'COLLE ALLLEMAND'),
(72, 'COLLE', 'COLLE ANGLAIS', '', 'COLLE ANGLAIS'),
(73, 'AP MA/PC', 'COLLE AP MATHS/PC MPSI1', '', 'AP M/P MPSI1'),
(74, 'COLLE', 'COLLE CULTURE GE', '', 'COLLE CULTURE GE'),
(75, 'COLLE', 'COLLE ECO-SOC-HIST', '', 'COLLE ECO-SOC-HIST'),
(76, 'COLLE', 'COLLE ESPAGNOL', '', 'COLLE ESPAGNOL'),
(77, 'COLLE', 'COLLE GEO', '', 'COLLE GEO'),
(78, 'COLLE', 'COLLE HISTOIRE', '', 'COLLE HISTOIRE'),
(79, 'COLLE', 'COLLE ITALIEN', '', 'COLLE IT'),
(80, 'COLLE', 'COLLE LANGUES ANCIENNES', '', 'COLLE LETTRES ANCIENNES'),
(81, 'COLLE', 'COLLE LETTRES', '', 'COLLE LETTRES'),
(82, 'COLLE', 'COLLE MATHS', '', 'COLLE MATHS'),
(83, 'COLLE', 'COLLE PHILO', '', 'COLLE PHILO'),
(84, 'COLLE', 'COLLE SCIENCES', '', 'COLLE SCIENCES'),
(85, 'COLLE', 'COLLE SI', '', 'COLLE SI'),
(86, 'COLMA', 'COLLE TD MAPLE', '', 'COLLE TD MAPLE'),
(87, 'BP CLG', 'COLLEGE B P', '', 'COLLEGE B P'),
(88, 'COLLEG', 'COLLEGE CHATEL', '', 'COLLEGE CHATEL'),
(89, 'COLLEG', 'COLLEGE L. MICHEL', '', 'COLLEGE L. MICHEL'),
(90, 'COLLEG', 'COLLEGE MDH', '', 'COLLEGE MDH'),
(91, 'CONCOU', 'CONCOURS BLANCS', '', 'CONCOURS BLANCS'),
(92, 'CONCOU', 'CONCOURS DES GRANDES ECOLES', '', 'CONCOURS DES GRANDES ECOLES'),
(93, 'COURS', 'COURS LANGUES ANCIENNES', '', 'COURS LANGUES ANCIENNES'),
(94, 'COURS', 'COURS SECOURISME', '', 'COURS SECOURISME'),
(95, 'ANTIQU', 'CULTURE ANTIQUE', '', 'CULTURE ANTIQUE'),
(96, 'CULGE', 'CULTURE GENE', '', 'CULTURE GENE'),
(97, 'CULGE', 'CULTURE GENERALE', '', 'CULTURE GENERALE'),
(98, 'DECP3', 'DECOUV .PROFESS. 3H', '', 'DÉCOUV. PROFESSION. 3H'),
(99, 'DETGED', 'DetGEDMC', '', 'DetGEDMC'),
(100, 'DEVOIR', 'DEVOIRS SURVEILLES', '', 'DEVOIRS SURVEILLES'),
(101, 'DNL HG', 'DNL HG', '', 'HI-GEO EURO'),
(102, 'DGEMC', 'DRT&ENJX.MDE CONTEMP', '', 'DRT&ENJX.MDE CONTEMP'),
(103, 'ESHMC', 'ECON.SOC.& HIST. MC', '', 'ECON.SOC.& HIST. MC'),
(104, 'E-ONO', 'ECONOMIE', '', 'ECONOMIE'),
(105, 'SES', 'ECONOMIE', '', 'SC. ECONO.&'),
(106, 'ECOAP', 'ECONOMIE APPROFONDIE', '', 'ÉCONOMIE APPROFONDIE'),
(107, 'ECONOM', 'ECONOMIE APPROFONDIE', '', 'ÉCONOMIE APPROFONDIE'),
(108, 'ECJS', 'ED.CIVIQ.JURIDIQ.SOC', '', 'ED.CIVIQ.JURIDIQ.SOC'),
(109, 'EPS', 'ED.PHYSIQUE & SPORT.', '', 'ED.PHYSIQUE & SPORT.'),
(110, 'EDE AAV', 'EDE Arts Vis', '', 'EDE Arts Vis'),
(111, 'EDE AR', 'EDE Arts Vis', '', 'EDE Arts Vis'),
(112, 'EDE LI', 'EDE Litt & Soc', '', 'EDE Litt & Soc'),
(113, 'EDE LIT', 'EDE Litt & Soc', '', 'EDE Litt & Soc'),
(114, 'EDE MP', 'EDE MPS', '', 'EDE MPS'),
(115, 'EDE PF', 'EDE PFEG', '', 'EDE PFEG'),
(116, 'EDE S-', 'EDE S-I', '', 'EDE S-I'),
(117, 'EDCIV', 'EDUCATION CIVIQUE', '', 'ÉDUCATION CIVIQUE'),
(118, 'EDMUS', 'EDUCATION MUSICALE', '', 'ÉDUCATION MUSICALE'),
(119, 'EMC', 'ENS. MORAL & CIVIQUE', '', 'ENS. MORAL & CIVIQUE'),
(120, 'ENSPHY', 'ENS_SC_PHYS', '', 'ENS_SC_PHYS'),
(121, 'ENSSVT', 'ENS_SC_SVT', '', 'ENS_SC_SVT'),
(122, 'ENTRET', 'ENTRETIEN', '', 'ENTRETIEN'),
(123, 'ESP A', 'ESP LV A', '', 'ESP LV A'),
(124, 'ESP B', 'ESP LV B', '', 'ESP LV B'),
(125, 'ESP LV RENFORCEE', 'ESP LV RENFORCEE', '', 'ESP LV RENFORCEE'),
(126, 'ESP1-2', 'ESP LV1-LV2', '', 'LV2'),
(127, 'ESP1', 'ESPAGNOL LV1', '', 'LV1'),
(128, 'ESP2', 'ESPAGNOL LV2', '', 'LV2'),
(129, 'ET CPG', 'ETUDE CPGE', '', 'ETUDE CPGE'),
(130, 'ET ECO', 'ETUDE CPGE ECO', '', 'Etudes CPGE ECO'),
(131, 'EXAMEN', 'EXAMEN', '', 'Examen'),
(132, 'FLE', 'FLE', '', 'FLE'),
(133, 'FORUM', 'FORUM DES GRANDES ECOLES', '', 'Forum des grandes écoles'),
(134, 'FRANC', 'FRANCAIS', '', 'FRANÇAIS'),
(135, 'FRANCAIS OPTION', 'FRANCAIS OPTION', '', 'FRANÇAIS'),
(136, 'FR-PH', 'FRANCAIS PHI', '', 'FRANÇAIS'),
(137, 'FR-PH', 'FRANCAIS PHILO', '', 'FRANÇAIS'),
(138, 'FR-PH', 'FRANCAIS PHILOSOPHIE', '', 'FRANÇAIS'),
(139, 'GEO-OP', 'GEO OPTION', '', 'GEO OPTION'),
(140, 'GEO-OP', 'GEO OPTION LSH', '', 'GEO OPTION'),
(141, 'GEOTP', 'GEO TP', '', 'GEO TP'),
(142, 'GEOGF', 'GEOGRAPHIE', '', 'GEOGRAPHIE'),
(143, 'GEOGRA', 'GEOGRAPHIE LSH', '', 'GEOGRAPHIE LSH'),
(144, 'GEOGRA', 'GEOGRAPHIE OBL LSH', '', 'GEOGRAPHIE LSH'),
(145, 'GREC', 'GREC ANCIEN', '', 'GREC ANCIEN'),
(146, 'GREC I', 'GREC INITIAT', '', 'GREC INITIAT'),
(147, 'GRESP', 'GREC SPECIALITE', '', 'GREC SPECIALITE'),
(148, 'HIG-EU', 'HI-GEO EURO', '', 'DNL'),
(149, 'HICTX', 'HIST.-COMMENT.TEXTES', '', 'HIST.-COMMENT.TEXTES'),
(150, 'HGGMC', 'HIST.GEO.GEOPOL.M.C.', '', 'HIST.GEO.GEOPOL.M.C.'),
(151, 'HMEMO', 'HIST.MEDIEV.& MODERN', '', 'HIST.MEDIEV.& MODERN'),
(152, 'HISTO', 'HISTOIRE', '', 'HISTOIRE'),
(153, 'HIGEO', 'HISTOIRE & G', '', 'HISTOIRE & G'),
(154, 'HIGEO', 'HISTOIRE & GEOGRAPH.', '', 'HISTOIRE & GEOGRAPH.'),
(155, 'HIANC', 'HISTOIRE ANC', '', 'HISTOIRE ANC'),
(156, 'HIANC', 'HISTOIRE ANCIENNE', '', 'HISTOIRE ANCIENNE'),
(157, 'HIDA', 'HISTOIRE DES ARTS', '', 'HISTOIRE DES ARTS'),
(158, 'HISOPT', 'HISTOIRE OPT', '', 'HISTOIRE OPT'),
(159, 'HI-GE', 'HISTOIRE-GEOGRAPHIE', '', 'HISTOIRE-GÉOGRAPHIE'),
(160, 'HIGEO', 'HISTOIRE-GEOGRAPHIE', '', 'HISTOIRE & GEOGRAPH.'),
(161, 'HI-GE', 'HISTOIRE-GÉOGRAPHIE', '', 'HISTOIRE-GÉOGRAPHIE'),
(162, 'INFOCO', 'INFO - COURS', '', 'INFO - COURS'),
(163, 'INFORM', 'INFO COMMUNE COURS', '', 'INFORMATIQUE'),
(164, 'INFOTD', 'INFO COMMUNE TD', '', 'INFORM P Tous TD'),
(165, 'I P T', 'INFORM  Pour Tous Cours', '', 'INFORM  Pour Tous Cours'),
(166, 'INFOTD', 'INFORM P Tous TD', '', 'INFORM P Tous TD'),
(167, 'INFOTD', 'INFORM TD', '', 'INFORM TD'),
(168, 'ISCNU', 'INFORMATIQ.SC.NUMERI', '', 'INFORMATIQ.SC.NUMERI'),
(169, 'IFTIQ', 'INFORMATIQUE', '', 'INFORMATIQUE'),
(170, 'INFORM', 'INFORMATIQUE', '', 'INFORMATIQUE'),
(171, 'IFTIQ', 'INFORMATIQUE OPTION', '', 'INFORMATIQUE OPTION'),
(172, 'IEP', 'INSTITUT ETU.POLITI.', '', 'INSTITUT ETU.POLITI.'),
(173, 'ISL2', 'ISLANDAIS LV2', '', 'LV2'),
(174, 'ISN', 'ISN', '', 'ISN'),
(175, 'ITA2', 'ITALIEN 2', '', 'LV2'),
(176, 'ITALIE', 'ITALIEN KH-HK', '', 'ITALIEN KH-HK'),
(177, 'ITA4', 'ITALIEN LV RENFORCE', '', 'ITALIEN LV RENFORCE'),
(178, 'ITA1', 'ITALIEN LV1', '', 'LV1'),
(179, 'ITA2', 'ITALIEN LV2', '', 'LV2'),
(180, 'ITALIE', 'ITALIEN LVI-LV2', '', 'LV2'),
(181, 'JAPONA', 'JAPONAIS 2 CNED', '', 'JAPONAIS 2 CNED'),
(182, 'JAP LV3 CNE', 'JAPONAIS LV3 CNED', '', 'LV3'),
(183, 'LATIN', 'LATIN', '', 'LATIN'),
(184, 'LCALA', 'LATIN', '', 'LATIN'),
(185, 'LATIN CNED', 'LATIN CNED', '', 'LATIN CNED'),
(186, 'LATSP', 'LATIN SPECIALITE', '', 'LATIN SPECIALITE'),
(187, 'LCAGR', 'LCA GREC', '', 'LCA GREC'),
(188, 'LITT L', 'LITT LVE AGL', '', 'LITT LVE AGL'),
(189, 'AGL-8', 'LITT. ANGLAIS', '', 'LITT. ANGLAIS'),
(190, 'LITCI', 'LITTER.CIVILIS.ETRG.', '', 'LITTER.CIVILIS.ETRG.'),
(191, 'AGL-8', 'LITTER.ETRANG.EN LVE', '', 'LITTER.ETRANG.EN LVE'),
(192, 'LILVE', 'LITTER.ETRANG.EN LVE', '', 'LITTER.ETRANG.EN LVE'),
(193, 'LITTE', 'LITTERATURE', '', 'LITTÉRATURE'),
(194, 'LITSO', 'LITTÉRATURE  SOCIETE', '', 'LITTÉRATURE  SOCIETE'),
(195, 'LYCEE', 'LYCEE JEANNE D\'ARC', '', 'LYCEE JEANNE D\'ARC'),
(196, 'LYCEE', 'LYCEE LAFAYETTE', '', 'LYCEE LAFAYETTE'),
(197, 'LYCÉE', 'Lycée MARIE CURIE', '', 'Lycée Marie Curie'),
(198, 'LYCEE', 'LYCEE PJB', '', 'LYCEE PJB'),
(199, 'LYCEE', 'LYCEE ROGER CLAUSTRES', '', 'LYCEE ROGER CLAUSTRES'),
(200, 'LYCÉEE', 'LYCEE SIDOINE', '', 'Lycéee Sidoine'),
(201, 'LYCEEV', 'LYCEE VIRLOGEUX', '', 'LYCEE VIRLOGEUX'),
(202, 'MATH E', 'MATH EURO', '', 'MATHÉMATIQUES'),
(203, 'MATH-S', 'MATH SOUTIEN', '', 'MATHÉMATIQUES'),
(204, 'MA-SP', 'MATH. SPE', '', 'MATHÉMATIQUES'),
(205, 'MA-SP', 'MATH. SPECIA', '', 'MATHÉMATIQUES'),
(206, 'MATHS', 'MATHEMATIQUE', '', 'MATHÉMATIQUES'),
(207, 'MATHS', 'MATHEMATIQUES', '', 'MATHÉMATIQUES'),
(208, 'DNL MA', 'MATHS (DNL)', '', 'DNL MATHS'),
(209, 'DNL MATH', 'MATHS (DNL)', '', 'DNL MATHS'),
(210, 'MATH E', 'MATHS (DNL)', '', 'MATHÉMATIQUES'),
(211, 'MA-SP', 'MATHS (SPE)', '', 'MATHÉMATIQUES'),
(212, 'MATHS', 'MATHS APPLIQUEES', '', 'MATHS APPLIQUEES'),
(213, 'MATHS', 'MATHS COURS-TD', '', 'MATHÉMATIQUES'),
(214, 'MA-IF', 'MATHS INFO ECO', '', 'MATHÉMATIQUES'),
(215, 'MA-IF', 'MATHS INFORMATIQUE', '', 'MATHÉMATIQUES'),
(216, 'MATHS', 'MATHS SPE ES', '', 'MATHÉMATIQUES'),
(217, 'MATHTD', 'MATHS TD', '', 'MATHÉMATIQUES'),
(218, 'MATHTP', 'MATHS TP', '', 'MATHÉMATIQUES'),
(219, 'MATIÈR', 'Matière non désignée', '', 'Non désignée'),
(220, 'MP-SC', 'METHOD.PRAT.SCIENTIF', '', 'METHOD.PRAT.SCIENTIF'),
(221, 'MUSIQ', 'MUSIQUE', '', 'MUSIQUE'),
(222, 'MUSIQ', 'MUSIQUE FAC', '', 'ARTS'),
(223, 'ORAUX', 'ORAUX ENTRAINEMENT', '', 'ORAUX ENTRAINEMENT'),
(224, 'ORIENT', 'ORIENTATION', '', 'ORIENTATION'),
(225, 'PPRE F', 'P.P.R.E. FRANCAIS', '', 'P.P.R.E. FRANCAIS'),
(226, 'PPRE M', 'P.P.R.E. MATHS', '', 'P.P.R.E. MATHS'),
(227, 'PHIOPT', 'PHILO OPTION', '', 'PHILO OPTION'),
(228, 'PHILO', 'PHILOSOPHIE', '', 'PHILOSOPHIE'),
(229, 'PHY-CH', 'PHYS (SPE)', '', 'PHYS SPECIA'),
(230, 'PHYSC', 'PHYS COURS', '', 'PHYS COURS'),
(231, 'PHY-SP', 'PHYS SPECIA', '', 'PHYS SPECIA'),
(232, 'PHY-SP', 'PHYS SPECIALITE', '', 'PHYS SPECIA'),
(233, 'PHYSI', 'PHYSIQUE', '', 'PHYSIQUE'),
(234, 'PHYSIQ', 'PHYSIQUE (DNL)', '', 'PHYSIQUE EURO'),
(235, 'PHYSIQ', 'PHYSIQUE EURO', '', 'PHYSIQUE EURO'),
(236, 'PHYSIQ', 'PHYSIQUE Soutien', '', 'PHYSIQUE Soutien'),
(237, 'PHYSTD', 'PHYSIQUE TD', '', 'PHYSIQUE TD'),
(238, 'PHYSTP', 'PHYSIQUE TP', '', 'PHYSIQUE TP'),
(239, 'PH-CH', 'PHYSIQUE-CHIMIE', '', 'PHYSIQUE-CHIMIE'),
(240, 'PHY-CH', 'PHYSIQUE-CHIMIE', '', 'PHYSIQUE'),
(241, 'PORTUGAIS LV2 CNED', 'PORTUGAIS LV2 CNED', '', 'LV2'),
(242, 'POR2C', 'PORTUGAIS LV2 CORR.', '', 'LV2'),
(243, 'PREPAR', 'PREPARATION IEP', '', 'PREPARATION IEP'),
(244, 'PREPAR', 'PREPARATION IEP HK/KH/ EC', '', 'PREPARATION IEP HK/KH'),
(245, 'PFEG', 'PRINC.FOND. ECO.GEST', '', 'PRINC.FOND. ECO.GEST'),
(246, 'RÉSERV', 'Réservation de salle', '', 'Non désignée'),
(247, 'RÉUNIO', 'Réunion Parents Prof', '', 'Réunion Parents Prof'),
(248, 'RUS2C', 'RUSSE LV2 CNED', '', 'LV2'),
(249, 'RUS2C', 'RUSSE LV2 CORRESP.', '', 'LV2'),
(250, 'RUS3', 'RUSSE LV3', '', 'LV3'),
(251, 'S.I.C', 'S.I. COURS', '', 'S.I. COURS'),
(252, 'S.I.TD', 'S.I. TD', '', 'S.I. TD'),
(253, 'SI1P', 'S.I. TD 1P', '', 'S.I. TD 1P'),
(254, 'S.I.TP', 'S.I. TP', '', 'S.I. TP'),
(255, 'SES', 'SC. ECONO.&', '', 'SC. ECONO.&'),
(256, 'SES', 'SC. ECONO.& SOCIALES', '', 'SC. ECONO.&'),
(257, 'SC. SO', 'SC. SOCIALES ET POLITIQUE', '', 'SC. SOCIALES ET POLITIQUE'),
(258, 'SSPOL', 'SC.SOC. & POLITIQUES', '', 'SC.SOC. & POLITIQUES'),
(259, 'S-BT', 'SCI.BIOLOGI.ET TERRE', '', 'SCI.BIOLOGI.ET TERRE'),
(260, 'S-IN4', 'SCI.INDUS.4H 2E PER.', '', 'SCI.INDUS.4H 2E PER.'),
(261, 'S-IN2', 'SCI.INDUST. 2H MPSI', '', 'SCI.INDUST. 2H MPSI'),
(262, 'SCIEN', 'SCIENCES', '', 'SCIENCES'),
(263, 'SCIENCES', 'SCIENCES', '', 'SCIENCES'),
(264, 'DNL SCIENCES', 'SCIENCES (DNL)', '', 'SCIENCES (DNL)'),
(265, 'S-IND', 'SCIENCES IND', '', 'SCIENCES IND'),
(266, 'S-IND', 'SCIENCES INDUSTRIEL.', '', 'SCIENCES INDUSTRIEL.'),
(267, 'SCIENCES INDUSTR', 'SCIENCES INDUSTRIELLES', '', 'SCIENCES INDUSTRIEL.'),
(268, 'SC-ING', 'SCIENCES ING', '', 'SCIENCES ING'),
(269, 'SC-IG', 'SCIENCES INGENIEUR', '', 'SCIENCES INGENIEUR'),
(270, 'SVT', 'SCIENCES VIE', '', 'SCIENCES VIE'),
(271, 'SVT', 'SCIENCES VIE & TERRE', '', 'SCIENCES VIE & TERRE'),
(272, 'ALL9S', 'SECTION ALLEMAND', '', 'SECTION ALLEMAND'),
(273, 'AGL9S', 'SECTION ANGLAIS', '', 'SECTION ANGLAIS'),
(274, 'ITA9S', 'SECTION ITALIEN', '', 'SECTION ITALIEN'),
(275, 'SESOP', 'SES ( SPE)', '', 'SES Spécialité'),
(276, 'SI COU', 'SI COURS 2ème p.', '', 'SI COURS 2ème p.'),
(277, 'SI COU', 'SI OPTION COURS 2ème p.', '', 'SI COURS 2ème p.'),
(278, 'SI TD', 'SI OPTION TD 2ème p.', '', 'SI TD 2ème p.'),
(279, 'SI TP', 'SI OPTION TP 2ème p.', '', 'SI TP 2ème p.'),
(280, 'SI-TD', 'SI-TD', '', 'SI-TD'),
(281, 'SOUTIE', 'SOUTIEN', '', 'SOUTIEN'),
(282, 'SOUTIE', 'SOUTIEN ANGLAIS', '', 'SOUTIEN ANGLAIS'),
(283, 'SOUTIE', 'SOUTIEN FRANCAIS', '', 'SOUTIEN FRANCAIS'),
(284, 'SOUTIE', 'SOUTIEN MATHS', '', 'SOUTIEN MATK£HS'),
(285, 'S PHYS', 'SOUTIEN PHYSIQUE', '', 'SOUTIEN PHYSIQUE'),
(286, 'SOUTIE', 'SOUTIEN TICE', '', 'SOUTIEN TICE'),
(287, 'SVT-EU', 'SVT (DNL)', '', 'SVT EURO'),
(288, 'SVT-EU', 'SVT (DNL)2', '', 'SVT EURO'),
(289, 'SVT-SP', 'SVT (SPE)', '', 'SVT SPECIA'),
(290, 'SVT-EU', 'SVT EURO', '', 'SVT EURO'),
(291, 'SVT-SP', 'SVT SPE', '', 'SVT SPECIA'),
(292, 'SVT-SP', 'SVT SPECIA', '', 'SVT SPECIA'),
(293, 'SVT-TP', 'SVT TP', '', 'SVT TP'),
(294, 'TIPESI', 'T.I.P.E. S.I', '', 'T.I.P.E. S.I'),
(295, 'TD MAP', 'TD MAPLE', '', 'TD MAPLE'),
(296, 'TECHN', 'TECHNOLOGIE', '', 'TECHNOLOGIE'),
(297, 'TIPEBI', 'TIPE BIO', '', 'TIPE BIO'),
(298, 'TIPECH', 'TIPE CHIMIE', '', 'PHYSIQUE-CHIMIE'),
(299, 'TIPEMA', 'TIPE MATHS', '', 'TIPE MATHS'),
(300, 'TIPEPH', 'TIPE PHYS', '', 'TIPE PHYS'),
(301, 'TIPE P', 'TIPE Phys.Chimie', '', 'TIPE Phys.Chimie'),
(302, 'TP SI', 'TP SI', '', 'TP SI'),
(303, 'TPE', 'TRAVX PERSO.ENCADRES', '', 'TRAVX PERSO.ENCADRES'),
(304, 'TURC', 'TURC', '', 'LV2'),
(305, 'TURQUE', 'TURQUE', '', 'TURQUE'),
(306, 'TUTORA', 'TUTORAT', '', 'TUTORAT'),
(307, 'TX-IP', 'TX.INIT.PERS', '', 'TX.INIT.PERS'),
(308, 'TX-IP', 'TX.INIT.PERSO.ENCAD.', '', 'TX.INIT.PERSO.ENCAD.'),
(309, 'VICLA', 'VIE DE CLASSE', '', 'VIE DE CLASSE'),
(310, 'VIE CL', 'VIE DE CLASSE', '', 'VIE SCOLAIRE');

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `offres`
--

INSERT INTO `offres` (`id`, `auteur`, `filiere`, `matiere`, `date_time`, `participant`, `participant2`, `disponible`, `debut_j0`, `fin_j0`, `debut_j1`, `fin_j1`, `debut_j2`, `fin_j2`, `debut_j3`, `fin_j3`, `debut_j4`, `fin_j4`, `debut_j5`, `fin_j5`) VALUES
(1, 'Marco Desmoulins', 'Terminale S', 'MATHEMATIQUES', '2018-02-22 00:00:00', NULL, NULL, 1, '08:00:00', '09:00:00', '16:00:00', '17:00:00', '14:00:00', '16:00:00', NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Tao Blancheton', 'Terminale S', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, '15:00:00', '16:00:00', NULL, NULL, NULL, NULL, '09:00:00', '10:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(3, 'Antoine Labarussias', 'Terminale S', 'S.I. COURS', '2018-02-22 00:00:00', NULL, NULL, 1, '13:00:00', '14:00:00', '17:00:00', '18:00:00', NULL, NULL, '14:00:00', '15:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(4, 'Jean Kévin', 'Seconde', 'FRANCAIS', '2018-02-22 00:00:00', NULL, NULL, 1, '08:00:00', '10:00:00', '11:00:00', '13:00:00', NULL, NULL, '15:00:00', '16:00:00', NULL, NULL, '08:00:00', '09:00:00'),
(5, 'Alexis Ducont', 'Terminale S', 'ISN', '2018-02-19 14:15:41', NULL, NULL, 1, '10:00:00', '11:00:00', NULL, NULL, NULL, NULL, '08:00:00', '09:00:00', NULL, NULL, NULL, NULL),
(6, 'Lola Blachard', 'Première S', 'S.I. COURS', '2018-02-22 00:00:00', NULL, NULL, 1, '15:00:00', '16:00:00', NULL, NULL, '17:00:00', '18:00:00', '10:00:00', '11:00:00', NULL, NULL, '09:00:00', '10:00:00');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `nom` varchar(50) NOT NULL DEFAULT '',
  `mdp` varchar(15) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `classe` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  `ban` tinyint(1) NOT NULL DEFAULT '0',
  `css` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`nom`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`nom`, `mdp`, `mail`, `classe`, `admin`, `ban`, `css`) VALUES
('Antoine Labarussias', 'antoine', 'antoinelabarussias@orange.fr', 'TS5', 1, 0, 0),
('Marco Desmoulins', 'marco', 'markopelo@gmail.com', 'TS5', 1, 0, 0),
('Tao Blancheton', 'tao', 'taotom63@gmail.com', 'TS5', 1, 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
