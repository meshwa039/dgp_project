-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 11, 2025 at 10:34 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `digital_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_tb`
--

DROP TABLE IF EXISTS `admin_tb`;
CREATE TABLE IF NOT EXISTS `admin_tb` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `a_username` varchar(20) NOT NULL,
  `a_password` varchar(20) NOT NULL,
  `a_image` varchar(100) NOT NULL,
  `a_lastseen` datetime NOT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_tb`
--

INSERT INTO `admin_tb` (`a_id`, `a_username`, `a_password`, `a_image`, `a_lastseen`) VALUES
(1, 'Meshwa', '1234', 'avatar-7.jpg', '2025-03-10 16:14:20'),
(2, 'Shivani', '1234', 'user-img.jpg', '2025-03-10 14:47:31'),
(3, 'Kashish', '1234', 'avatar-3.jpg', '2024-12-13 12:48:04');

-- --------------------------------------------------------

--
-- Table structure for table `birth_tb`
--

DROP TABLE IF EXISTS `birth_tb`;
CREATE TABLE IF NOT EXISTS `birth_tb` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `city_dname` varchar(50) NOT NULL,
  `city_tname` varchar(50) NOT NULL,
  `city_vname` varchar(50) NOT NULL,
  `b_name` varchar(50) NOT NULL,
  `b_gender` enum('Male','Female','Other') NOT NULL,
  `b_dob` date NOT NULL,
  `b_place` varchar(50) NOT NULL,
  `b_mother` varchar(20) NOT NULL,
  `b_father` varchar(20) NOT NULL,
  `b_address` text NOT NULL,
  `b_peraddress` text NOT NULL,
  `b_relation_name` varchar(20) NOT NULL,
  `b_time` varchar(20) NOT NULL,
  `b_regdate` date NOT NULL,
  `b_remarkdetail` text,
  `e_id` int(11) NOT NULL,
  `g_status` enum('Active','Deactive') NOT NULL,
  `e_status` enum('Active','Deactive') NOT NULL,
  `b_cdate` datetime NOT NULL,
  `b_udate` datetime NOT NULL,
  `b_idproof` varchar(100) NOT NULL,
  `b_hospitalletter` varchar(100) NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `birth_tb`
--

INSERT INTO `birth_tb` (`b_id`, `u_id`, `city_dname`, `city_tname`, `city_vname`, `b_name`, `b_gender`, `b_dob`, `b_place`, `b_mother`, `b_father`, `b_address`, `b_peraddress`, `b_relation_name`, `b_time`, `b_regdate`, `b_remarkdetail`, `e_id`, `g_status`, `e_status`, `b_cdate`, `b_udate`, `b_idproof`, `b_hospitalletter`) VALUES
(1, 2, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'meshwa patel', 'Female', '2005-09-03', 'SMVS hospital,Mansa,Gandhinagar', 'bhavnaben d patel', 'Daxeshbhai k patel', 'Mansa,Gandhinagar', '27 Sparsh Palace,PDPU Road,Raysan,Gandhinagar', 'Self', '19:32', '2025-02-19', NULL, 1, 'Active', 'Active', '2025-02-19 14:34:10', '2025-02-19 14:56:33', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_2o9rbBE.jpg'),
(2, 1, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'Meshwa D Patel', 'Female', '2005-09-03', 'SMVS hospital,Mansa,Gandhinagar', 'bhavnaben d patel', 'Daxeshbhai k patel', 'Mansa,Gandhinagar', '27 Sparsh Palace,PDPU Road,Raysan,Gandhinagar', 'Self', '19:19', '2025-02-18', 'None', 3, 'Active', 'Deactive', '2025-02-19 15:21:30', '2025-03-10 12:19:01', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_2o9rbBE.jpg'),
(3, 1, 'Gandhinagar', 'Kalol', 'Bhadol', 'Nandani R patel', 'Female', '2005-05-23', 'gayatri sergical hospial,Kalol,Gandhinagar', 'Komalben R patel', 'Rajeshbhai Patel', 'gayatri sergical hospial,Kalol,Gandhinagar', 'mukhiwadi fali,near by dairy,bayad,arvali', 'Self', '20:30', '2025-02-19', 'None', 3, 'Active', 'Active', '2025-02-19 15:34:35', '2025-02-19 15:36:01', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_2o9rbBE.jpg'),
(4, 3, 'Gandhinagar', 'Dehgam', 'Halisa', 'disha j patel', 'Female', '2003-06-10', 'maa surgical hospital,dehgam,gandhinagar', 'kailashben j patel', 'jigneshbhai patel', 'maa surgical hospital,dehgam,gandhinagar', 'c302,swaminarayan society,dahegam, gandhinagar', 'Self', '04:43', '2025-02-19', 'None', 1, 'Active', 'Active', '2025-02-19 15:45:58', '2025-02-19 16:06:30', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_2o9rbBE.jpg'),
(5, 1, 'Gandhinagar', 'Mansa', 'Mansa', 'khevna kevadiya', 'Female', '2005-09-24', 'arpan multispecialist hospital,mansa,gandhinagar', 'toralben k kevadiya', 'ketanbhai kevadiya', 'arpan multispecialist hospital,mansa,gandhinagar', '12 kumkumnagar mansa,gandhinagar', 'Self', '10:01', '2025-02-19', 'None', 1, 'Active', 'Active', '2025-02-19 16:05:04', '2025-02-19 16:06:17', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_2o9rbBE.jpg'),
(6, 2, 'Gandhinagar', 'Mansa', 'Ajol', 'derft', 'Female', '2025-02-11', 'fghyu', 'aaweftyu', 'dghjk', 'swdefrgthyu', 'efrgtyh', 'Self', '10:34', '2025-02-11', 'approve d both fjk', 2, 'Active', 'Active', '2025-02-20 10:33:19', '2025-02-25 15:35:59', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_2o9rbBE.jpg'),
(8, 2, 'Gandhinagar', 'Dehgam', 'Dehgam', 'foram', 'Female', '2025-02-22', 'gchvjhvk', 'jvjhvbjhbjh', 'jhjhgjbk', 'chgcghjvjhb', 'gfcjhvhvhvj', 'Father', '14:22', '2025-02-22', NULL, 0, 'Deactive', 'Deactive', '2025-02-22 22:22:46', '2025-02-22 22:22:46', 'blog_single_client2_2o9rbBE.jpg', 'blog_single_client2_zQdXqjj.jpg'),
(9, 2, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'foram', 'Female', '2024-12-11', 'sfsddg', 'test', 'test', 'sadsdasd', 'sadsdasdasd', 'Mother', '16:17', '2025-02-25', 'None', 2, 'Deactive', 'Deactive', '2025-02-25 15:18:08', '2025-03-11 14:28:25', 'shivani_xao5AVP.jpg', 'mygov_165674019251307401_vj2QXQp.jpg'),
(10, 2, 'Gandhinagar', 'Dehgam', 'Dehgam', 'rvdfecfhe', 'Male', '2025-03-04', 'SMVS hospital,Gandhinagar', 'edcdc', 'decdec', 'dcedc', 'dcedc', 'Father', '16:11', '2025-03-11', NULL, 0, 'Deactive', 'Deactive', '2025-03-11 13:11:51', '2025-03-11 13:11:51', 'shivani2.pdf', 'll application.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `cast_tb`
--

DROP TABLE IF EXISTS `cast_tb`;
CREATE TABLE IF NOT EXISTS `cast_tb` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `city_dname` varchar(50) NOT NULL,
  `city_tname` varchar(50) NOT NULL,
  `city_vname` varchar(50) NOT NULL,
  `c_name` varchar(50) NOT NULL,
  `c_gender` enum('Male','Female','Other') NOT NULL,
  `c_year` int(11) NOT NULL,
  `c_address` text NOT NULL,
  `c_peraddress` text NOT NULL,
  `c_father` varchar(50) NOT NULL,
  `c_regdate` date NOT NULL,
  `c_blood_relation` enum('Yes','No') NOT NULL,
  `c_religion` varchar(20) NOT NULL,
  `c_cast_type` varchar(20) NOT NULL,
  `c_applyfor` varchar(20) NOT NULL,
  `c_cdate` datetime NOT NULL,
  `c_udate` datetime NOT NULL,
  `c_issuedate` date DEFAULT NULL,
  `e_id` int(11) NOT NULL,
  `e_status` enum('Active','Deactive') NOT NULL,
  `g_status` enum('Active','Deactive') NOT NULL,
  `c_status` enum('Approve','Reject') NOT NULL,
  `c_dob` date NOT NULL,
  `c_remarkdetail` text,
  `c_idproof` varchar(100) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cast_tb`
--

INSERT INTO `cast_tb` (`c_id`, `u_id`, `city_dname`, `city_tname`, `city_vname`, `c_name`, `c_gender`, `c_year`, `c_address`, `c_peraddress`, `c_father`, `c_regdate`, `c_blood_relation`, `c_religion`, `c_cast_type`, `c_applyfor`, `c_cdate`, `c_udate`, `c_issuedate`, `e_id`, `e_status`, `g_status`, `c_status`, `c_dob`, `c_remarkdetail`, `c_idproof`) VALUES
(1, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'Karangiya Shivani', 'Female', 2024, '95 Sidhivinayak Park,sargasan,gandhinagar', '95 Sidhivinayak Park,sargasan,gandhinagar', 'ranshibhai karangiya', '2025-02-19', 'Yes', 'HINDU', 'AHIR', 'ST', '2025-02-19 14:51:58', '2025-02-19 14:57:00', '2025-02-25', 3, 'Active', 'Active', 'Approve', '2005-04-05', 'None', ''),
(2, 2, 'Gandhinagar', 'Dehgam', 'Halisa', 'Kashish H Talwadi', 'Female', 2024, '22 Plot,sector 22,halisa,Dehgam,Gandhinagar', '22 Plot,sector 22,halisa,Dehgam,Gandhinagar', 'Harsadbhai Talwadi', '2025-02-17', 'Yes', 'HINDU', 'Talwadi', 'SC', '2025-02-19 15:29:01', '2025-02-19 15:36:54', NULL, 2, 'Active', 'Active', 'Reject', '2004-12-26', 'None', ''),
(3, 3, 'Gandhinagar', 'Kalol', 'Balva', 'dhruvisha boghara', 'Female', 2025, '22,tower chock,kalol,gandhinagar', '22,tower chock,kalol,gandhinagar', 'batukbhai boghara', '2025-02-19', 'Yes', 'HINDU', 'boghraa', 'ST', '2025-02-19 15:54:08', '2025-02-20 14:59:25', '2025-02-20', 3, 'Active', 'Active', 'Approve', '2005-03-07', 'None', ''),
(4, 3, 'Gandhinagar', 'Dehgam', 'Badpur', 'sakshi chaudhary', 'Female', 2025, '207 shreeji charan,dahegam,gandhinagar', '207 shreeji charan,dahegam,gandhinagar', 'bharatbhai chaudhary', '2025-02-19', 'Yes', 'HINDU', 'chaudhary', 'oBC', '2025-02-19 15:57:22', '2025-02-20 14:59:33', '2025-02-20', 3, 'Active', 'Active', 'Approve', '2005-12-08', 'None', ''),
(6, 2, 'Gandhinagar', 'Dehgam', 'Halisa', 'hvjhvjhbj', 'Female', 2022, 'vmvvhvbjhj', 'hbjkbkbkjbjk', 'vhjvbjhbj', '2025-02-22', 'Yes', 'gkjbkj', 'jkkjhkj', 'vjhvjh', '2025-02-22 22:21:31', '2025-02-25 15:30:06', NULL, 2, 'Deactive', 'Active', 'Reject', '2025-02-22', 'None', ''),
(8, 2, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'foram', 'Male', 2025, 'test', 'test', 'test', '2025-02-25', 'Yes', 'hindu', 'hindu1', 'test', '2025-02-25 15:21:04', '2025-03-10 16:20:26', '2025-02-28', 2, 'Deactive', 'Deactive', 'Reject', '2025-02-11', 'Done', 'user_Qtk8g7F.png'),
(9, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'test', 'Male', 2025, 'yhfhgfhv', 'fsdfsdfsdfs', 'test', '2025-03-10', 'Yes', 'HINDU', 'sc', 'ST', '2025-03-10 16:30:13', '2025-03-10 16:30:32', NULL, 0, 'Deactive', 'Deactive', 'Reject', '2025-03-10', NULL, 'shivani lc_szGcZUP.jpg'),
(10, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'wdwd', 'Female', 2025, 'ew', 'ergrt', 'wd', '2025-03-11', 'Yes', 'HINDU', 'AHIR', 'wed', '2025-03-11 11:30:45', '2025-03-11 11:30:59', NULL, 0, 'Deactive', 'Deactive', 'Reject', '2025-03-11', NULL, 'dummy_NGt6JRd.pdf'),
(11, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'cvcv', 'Female', 2025, 'cvxcvx', 'cxvxcvxcv', 'cvxcv', '2025-03-11', 'Yes', 'xcvxcv', 'vcxcv', 'xcv', '2025-03-11 14:45:41', '2025-03-11 15:03:38', NULL, 0, 'Deactive', 'Deactive', 'Reject', '2025-03-11', NULL, 'shivani2_XjMWZqw.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `category_tb`
--

DROP TABLE IF EXISTS `category_tb`;
CREATE TABLE IF NOT EXISTS `category_tb` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(50) NOT NULL,
  `cat_image` varchar(100) NOT NULL,
  `cat_status` enum('Active','Deactive') NOT NULL,
  `cat_cdate` datetime NOT NULL,
  `cat_udate` datetime NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category_tb`
--

INSERT INTO `category_tb` (`cat_id`, `cat_name`, `cat_image`, `cat_status`, `cat_cdate`, `cat_udate`) VALUES
(3, 'Birth Certificate', 'birth-certificate.png', 'Active', '2025-01-08 14:30:48', '2025-01-08 14:30:48'),
(4, 'Death Certificate', 'death-certificate.png', 'Active', '2025-01-08 14:31:09', '2025-01-08 14:31:09'),
(5, 'Cast Certificate', 'certificate (1).png', 'Active', '2025-01-08 14:31:33', '2025-01-08 14:31:33'),
(6, 'Income Certificate', 'contract.png', 'Active', '2025-01-08 14:31:53', '2025-01-08 14:31:53'),
(7, 'Tax Certificate', 'certificate.png', 'Active', '2025-01-08 14:32:07', '2025-01-08 14:32:07');

-- --------------------------------------------------------

--
-- Table structure for table `death_tb`
--

DROP TABLE IF EXISTS `death_tb`;
CREATE TABLE IF NOT EXISTS `death_tb` (
  `dth_id` int(11) NOT NULL AUTO_INCREMENT,
  `e_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `city_dname` varchar(50) NOT NULL,
  `city_tname` varchar(50) NOT NULL,
  `city_vname` varchar(50) NOT NULL,
  `dth_name` varchar(50) NOT NULL,
  `dth_gender` enum('Male','Female','Other') NOT NULL,
  `dth_time` varchar(20) NOT NULL,
  `dth_place` varchar(50) NOT NULL,
  `dth_mother` varchar(50) NOT NULL,
  `dth_father` varchar(50) NOT NULL,
  `dth_nominy` varchar(50) NOT NULL,
  `dth_type` enum('Naturally','Accidentally') NOT NULL,
  `dth_Address` text NOT NULL,
  `dth_Peraddress` text NOT NULL,
  `dth_Deathdate` datetime NOT NULL,
  `dth_Relationname` varchar(50) NOT NULL,
  `dth_Regdate` date NOT NULL,
  `dth_issuedate` date DEFAULT NULL,
  `dth_Remarkdetail` text,
  `g_status` enum('Active','Deactive') NOT NULL,
  `e_status` enum('Active','Deactive') NOT NULL,
  `dth_cdate` datetime DEFAULT NULL,
  `dth_udate` datetime DEFAULT NULL,
  `dth_idproof` varchar(100) NOT NULL,
  `dth_hospitalletter` varchar(100) NOT NULL,
  PRIMARY KEY (`dth_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `death_tb`
--

INSERT INTO `death_tb` (`dth_id`, `e_id`, `u_id`, `city_dname`, `city_tname`, `city_vname`, `dth_name`, `dth_gender`, `dth_time`, `dth_place`, `dth_mother`, `dth_father`, `dth_nominy`, `dth_type`, `dth_Address`, `dth_Peraddress`, `dth_Deathdate`, `dth_Relationname`, `dth_Regdate`, `dth_issuedate`, `dth_Remarkdetail`, `g_status`, `e_status`, `dth_cdate`, `dth_udate`, `dth_idproof`, `dth_hospitalletter`) VALUES
(2, 2, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'priyanshi s bapodariya', 'Female', '16:45', 'chaudhary collage,sector 7,Gandhinagar', 'Joshnaben bapodariya', 'Sureshbhai bapodariya', 'Janki patel', 'Naturally', 'sector 7 , gandhinagar', '22 rivanta, sargasan,gandhinagar', '2024-11-12 00:00:00', 'Daughter', '2025-02-12', '2025-02-19', 'None', 'Active', 'Active', '2025-02-19 14:47:00', '2025-02-19 14:59:19', '', ''),
(3, 2, 2, 'Gandhinagar', 'Kalol', 'Balva', 'Drashti K Patel', 'Female', '04:12', 'Gh 5 , Kalol,Gandhinagar', 'Kinjalben patel', 'Kishorbhai patel', 'Priyanshi S patel', 'Accidentally', 'Gh 5 , Kalol,Gandhinagar', '22 Radhe-Green,Kalol,gandhinagar', '2025-01-28 00:00:00', 'Daughter', '2025-02-12', NULL, 'None', 'Active', 'Active', '2025-02-19 15:15:20', '2025-02-19 18:04:27', '', ''),
(4, 1, 1, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'Mansi Zalavdiya', 'Female', '20:23', 'Orbit Mall,Kalol,Gandhinagar', 'Kantaben n patel', 'Nirbhaybhai J Patel', 'Janki patel', 'Accidentally', 'Orbit Mall,Kalol,Gandhinagar', '22 radhe,Alua,Kalol,Gandhinagar', '2025-02-01 00:00:00', 'Daughter', '2025-02-19', NULL, 'None', 'Deactive', 'Deactive', '2025-02-19 15:27:15', '2025-02-21 11:25:00', '', ''),
(5, 2, 3, 'Gandhinagar', 'Mansa', 'Charada', 'ranchodbhai k chaudhary', 'Male', '17:47', 'sector 25,gyan shakti road,mansa,gandhinagar', 'Lilaben k chaudhary ', 'Kanhabhai chaudhary', 'haridada', 'Accidentally', 'sector 25,gyan shakti road,mansa,gandhinagar', 'shreenagar society, mansa,gandhinagar', '2025-03-06 00:00:00', 'Brother', '2025-02-19', NULL, 'None', 'Active', 'Active', '2025-02-19 15:50:52', '2025-02-20 14:57:49', '', ''),
(6, 0, 1, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'htfh', 'Female', '00:19', 'fhfhf', 'ffbhdferetwtw', 'dxxfs', 'tfhfchh', 'Accidentally', 'rdhfth', 'dfhfgjhfjgg', '2025-02-21 00:00:00', 'Self', '2025-02-20', NULL, NULL, 'Deactive', 'Deactive', '2025-02-21 11:20:13', '2025-02-21 11:20:13', '', ''),
(7, 0, 1, 'Gandhinagar', 'Dehgam', 'Dehgam', 'ffgdf', 'Female', '11:22', 'vnvcncnv', 'cvbvnv', 'cvnbcvn', 'vnnv', 'Accidentally', 'cnbvncn', 'cnvnvncvn', '2025-02-21 00:00:00', 'Self', '2025-02-13', NULL, NULL, 'Deactive', 'Deactive', '2025-02-21 11:21:20', '2025-02-21 11:21:20', '', ''),
(9, 2, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'sfdgsdg', 'Female', '20:57', 'sgdg', 'asfasfsaf', 'dsfsdfa', 'sdgsgds', 'Naturally', 'asfasf', 'fasfasf', '2025-02-13 00:00:00', 'Father', '2025-02-10', '2025-02-25', 'done', 'Active', 'Active', '2025-02-22 21:07:32', '2025-02-25 15:37:33', 'blog_single_client2_QCuUVU3.jpg', 'blog_single_client2_m0zRCHw.jpg'),
(10, 2, 2, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'test', 'Female', '16:19', 'Home', 'test', 'test', 'test', 'Accidentally', 'test', 'test', '2025-02-25 00:00:00', 'Other', '2025-02-25', '2025-02-25', 'Done', 'Deactive', 'Deactive', '2025-02-25 15:19:37', '2025-03-10 17:55:01', 'certificate_a1PDI7k.png', 'certificate_L4gJysc.png'),
(11, 0, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'test', 'Female', '03:18', 'dxds', 'efce', 'dfc', 'fce', 'Accidentally', 'ecded', 'ececec', '2025-03-11 00:00:00', 'Father', '2025-03-11', NULL, NULL, 'Deactive', 'Deactive', '2025-03-11 11:21:11', '2025-03-11 11:22:06', 'dummy_fcuOyrR.pdf', 'dummy_fcuOyrR.pdf'),
(12, 0, 2, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'trgrdg', 'Male', '15:16', 'trhrthrth', 'rthrthh', 'rgtrth', 'trhrhrh', 'Accidentally', 'trhrthrh', 'hhtyrthh', '2025-03-04 00:00:00', 'Mother', '2025-03-11', NULL, NULL, 'Deactive', 'Deactive', '2025-03-11 15:12:36', '2025-03-11 15:16:18', 'shivani_DsJ4bhx.jpg', 'shivani1_M5DLWB2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `employee_tb`
--

DROP TABLE IF EXISTS `employee_tb`;
CREATE TABLE IF NOT EXISTS `employee_tb` (
  `e_id` int(11) NOT NULL AUTO_INCREMENT,
  `e_name` varchar(50) NOT NULL,
  `e_image` varchar(100) NOT NULL,
  `e_contact` bigint(20) NOT NULL,
  `e_post` varchar(50) NOT NULL,
  `e_email` varchar(50) NOT NULL,
  `e_password` varchar(20) NOT NULL,
  `e_status` enum('Active','Deactive') NOT NULL,
  `e_cdate` datetime NOT NULL,
  `e_udate` datetime NOT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_tb`
--

INSERT INTO `employee_tb` (`e_id`, `e_name`, `e_image`, `e_contact`, `e_post`, `e_email`, `e_password`, `e_status`, `e_cdate`, `e_udate`) VALUES
(1, 'Meshwa Patel', 'meshwa_rh3vfN0.jpg', 9537620224, 'Talati', 'meshwa123@gmail.com', '1234', 'Active', '2025-01-28 15:09:49', '2025-03-10 14:48:30'),
(2, 'Shivani Ahir', 'shivani_rbkGyzy.jpg', 8264711111, 'Talati', 'shivani044@gmail.com', '1234', 'Active', '2025-01-28 15:10:54', '2025-03-10 16:10:43'),
(3, 'Kashish Talwadi', 'kashish_YWDCLms.jpg', 9727550483, 'Talati', 'kashish12@gmail.com', '1234', 'Active', '2025-01-28 15:11:28', '2025-02-20 14:59:40');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_tb`
--

DROP TABLE IF EXISTS `feedback_tb`;
CREATE TABLE IF NOT EXISTS `feedback_tb` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(50) NOT NULL,
  `f_contact` bigint(20) NOT NULL,
  `f_message` text NOT NULL,
  `f_status` enum('Active','Deactive') NOT NULL,
  `f_cdate` datetime NOT NULL,
  `f_udate` datetime NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_tb`
--

INSERT INTO `feedback_tb` (`f_id`, `f_name`, `f_contact`, `f_message`, `f_status`, `f_cdate`, `f_udate`) VALUES
(1, 'Shivani Ahir', 8264711111, 'To be honest it is the first government app which is fast and smooth.\r\n', 'Active', '2025-01-28 15:16:20', '2025-01-28 15:16:20'),
(2, 'Meshwa Patel', 9537620224, 'A review is an evaluation of a publication, product, service, or company or a critical take on current affairs in literature, politics or culture. ', 'Active', '2025-01-28 15:18:54', '2025-01-28 15:18:54'),
(3, 'Kashish Talawdi', 9727550483, '“I think you did a great job when you… ...', 'Active', '2025-01-28 15:20:11', '2025-01-28 15:20:11');

-- --------------------------------------------------------

--
-- Table structure for table `income_tb`
--

DROP TABLE IF EXISTS `income_tb`;
CREATE TABLE IF NOT EXISTS `income_tb` (
  `i_id` int(11) NOT NULL AUTO_INCREMENT,
  `e_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `city_dname` varchar(50) NOT NULL,
  `city_tname` varchar(50) NOT NULL,
  `city_vname` varchar(50) NOT NULL,
  `i_name` varchar(20) NOT NULL,
  `i_gender` enum('Male','Female','Other') NOT NULL,
  `i_address` text NOT NULL,
  `i_peraddress` text NOT NULL,
  `i_amount` varchar(50) NOT NULL,
  `i_year` varchar(20) NOT NULL,
  `i_issuedate` date DEFAULT NULL,
  `i_status` enum('Approve','Reject') NOT NULL,
  `g_status` enum('Active','Deactive') NOT NULL,
  `e_status` enum('Active','Deactive') NOT NULL,
  `i_remarkdetail` text,
  `i_cdate` datetime NOT NULL,
  `i_udate` datetime NOT NULL,
  `i_pancard` varchar(100) NOT NULL,
  PRIMARY KEY (`i_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `income_tb`
--

INSERT INTO `income_tb` (`i_id`, `e_id`, `u_id`, `city_dname`, `city_tname`, `city_vname`, `i_name`, `i_gender`, `i_address`, `i_peraddress`, `i_amount`, `i_year`, `i_issuedate`, `i_status`, `g_status`, `e_status`, `i_remarkdetail`, `i_cdate`, `i_udate`, `i_pancard`) VALUES
(1, 2, 3, 'Gandhinagar', 'Dehgam', 'Halisa', 'Kashish Talwadi', 'Female', 'Sectior-6/B,Halisa,Gandhinagar', 'Sectior-6/B,Halisa,Gandhinagar', '50000', '2025-01-17', NULL, 'Reject', 'Active', 'Active', 'None', '2025-01-30 12:37:12', '2025-02-19 16:07:43', ''),
(2, 2, 2, 'Gandhinagar', 'Kalol', 'Aluva', 'Ramsibhai Ahir', 'Male', '27,Siddhivinayak,Aluva,Gandhinagar', '27,Siddhivinayak,Aluva,Gandhinagar', '50000', '2025-01-15', '2025-02-19', 'Approve', 'Active', 'Active', 'None', '2025-01-30 13:00:19', '2025-02-19 16:07:53', ''),
(3, 2, 1, 'Gandhinagar', 'Mansa', 'Mansa', 'Meshwa Patel', 'Female', 'Sector 6/B,Mansa,Gandhinagar', 'Sector 6/B,Mansa,Gandhinagar', '50000', '2025-01-16', '2025-02-12', 'Approve', 'Active', 'Active', 'Approved And Approved By Employee', '2025-01-31 12:12:47', '2025-02-12 15:24:21', ''),
(4, 2, 3, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'parth karangiya', 'Male', '95 Sidhivinayak Park,sargasan,gandhinagar', '95 Sidhivinayak Park,sargasan,gandhinagar', '700000', '2025-02-19', NULL, 'Reject', 'Active', 'Active', 'None', '2025-02-19 15:59:02', '2025-02-19 16:07:33', ''),
(5, 0, 1, 'Gandhinagar', 'Dehgam', 'Dehgam', 'sdsc', 'Male', 'sdsdc', 'sdddd', '50000', '2000', NULL, 'Reject', 'Deactive', 'Deactive', NULL, '2025-02-21 11:44:05', '2025-02-21 11:44:29', ''),
(7, 2, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'sefsdfasf', 'Female', 'dfdfsdf', 'sdgdsdgs', '23123', '2002', '2025-02-25', 'Approve', 'Active', 'Active', 'Done', '2025-02-22 22:17:54', '2025-02-25 15:37:01', ''),
(8, 2, 2, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'test', 'Female', 'test', 'test', '50000', '2025', '2025-02-27', 'Approve', 'Active', 'Active', 'Done', '2025-02-25 15:21:31', '2025-02-25 15:42:28', ''),
(9, 0, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'test', 'Female', 'testttttt', 'testtttt', '1322222', '2025', NULL, 'Reject', 'Deactive', 'Deactive', NULL, '2025-03-10 16:24:58', '2025-03-10 16:25:20', 'income_WDvjvLy.jpg'),
(10, 0, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'ds', 'Male', 'csdc', 'dcv', '1234', '2025', NULL, 'Reject', 'Deactive', 'Deactive', NULL, '2025-03-11 11:33:29', '2025-03-11 11:33:29', 'certificate_gBMhJUy.png'),
(11, 0, 2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'rdfdfd', 'Male', 'fgdgd', 'dfsdgd', '50000', '2025', NULL, 'Reject', 'Deactive', 'Deactive', NULL, '2025-03-11 15:20:12', '2025-03-11 15:23:30', 'shop_tmVUftu.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tax_tb`
--

DROP TABLE IF EXISTS `tax_tb`;
CREATE TABLE IF NOT EXISTS `tax_tb` (
  `tx_id` int(11) NOT NULL AUTO_INCREMENT,
  `e_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `city_dname` varchar(50) NOT NULL,
  `city_tname` varchar(50) NOT NULL,
  `city_vname` varchar(50) NOT NULL,
  `tx_name` varchar(50) NOT NULL,
  `tx_gender` enum('Male','Female') NOT NULL,
  `tx_address` text NOT NULL,
  `tx_peraddress` text NOT NULL,
  `tx_home` varchar(50) NOT NULL,
  `tx_sqrt` varchar(20) NOT NULL,
  `tx_amount` int(11) NOT NULL,
  `tx_year` varchar(20) NOT NULL,
  `tx_outstanding` double NOT NULL,
  `tx_total` int(11) NOT NULL,
  `tx_issue` date NOT NULL,
  `tx_status` enum('Approve','Reject') NOT NULL,
  `e_status` enum('Active','Deactive') NOT NULL,
  `g_status` enum('Active','Deactive') NOT NULL,
  `tx_remarkdetail` text NOT NULL,
  `tx_cdate` datetime NOT NULL,
  `tx_udate` datetime NOT NULL,
  PRIMARY KEY (`tx_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tax_tb`
--

INSERT INTO `tax_tb` (`tx_id`, `e_id`, `u_id`, `city_dname`, `city_tname`, `city_vname`, `tx_name`, `tx_gender`, `tx_address`, `tx_peraddress`, `tx_home`, `tx_sqrt`, `tx_amount`, `tx_year`, `tx_outstanding`, `tx_total`, `tx_issue`, `tx_status`, `e_status`, `g_status`, `tx_remarkdetail`, `tx_cdate`, `tx_udate`) VALUES
(1, 2, 2, 'Gandhinagar', 'Mansa', 'Ajol', 'Komal Patel', 'Male', '302, 3rd Floor Shrinath Complex, Nr. GH-5, Sector-22, Gandhinagar', '302, 3rd Floor Shrinath Complex, Nr. GH-5, Sector-22, Gandhinagar', '292/3', '550', 1100, '2025', 10, 1110, '2025-02-08', 'Approve', 'Active', 'Active', '2025 Financial Year Tax', '2025-02-07 14:24:39', '2025-02-12 15:58:54');

-- --------------------------------------------------------

--
-- Table structure for table `user_tb`
--

DROP TABLE IF EXISTS `user_tb`;
CREATE TABLE IF NOT EXISTS `user_tb` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `u_image` varchar(100) NOT NULL,
  `u_idproof` varchar(100) NOT NULL,
  `u_contact` bigint(20) NOT NULL,
  `u_aadharnumber` varchar(50) NOT NULL,
  `u_password` varchar(20) NOT NULL,
  `u_status` enum('Active','Deactive') NOT NULL,
  `u_cdate` datetime NOT NULL,
  `u_udate` datetime NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_tb`
--

INSERT INTO `user_tb` (`u_id`, `u_name`, `u_image`, `u_idproof`, `u_contact`, `u_aadharnumber`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES
(1, 'Meshwa Patel', 'meshwa_RGhMaTs.jpg', 'id.jpg', 9537620224, '342541346714', '1234', 'Active', '2025-01-28 14:58:57', '2025-02-21 11:44:58'),
(2, 'Shivani Ahir', 'certificate_sGD2pWE.png', 'dummy_C9Dz7je.pdf', 8264711111, '342541346714', '1234', 'Active', '2025-01-28 15:05:46', '2025-03-11 15:52:09'),
(3, 'Kashish Talwadi', 'kashish_BY5NuEB.jpg', 'id.jpg', 9727550483, '342541346714', '1234', 'Active', '2025-01-28 15:07:08', '2025-02-21 10:09:52'),
(4, 'dscsd', 'blog_single_client3.jpg', 'blog_single_client2.jpg', 2312131232, '213123123312', '21312', 'Active', '2025-02-21 11:46:30', '2025-02-21 11:46:30'),
(5, 'foram', 'death-certificate_kAuJ1ug.png', 'dummy_A3TfPH1.pdf', 7016664771, '145879632444', '12345', 'Active', '2025-03-11 13:00:28', '2025-03-11 13:00:28');

-- --------------------------------------------------------

--
-- Table structure for table `village_tb`
--

DROP TABLE IF EXISTS `village_tb`;
CREATE TABLE IF NOT EXISTS `village_tb` (
  `v_id` int(11) NOT NULL AUTO_INCREMENT,
  `v_dname` varchar(50) NOT NULL,
  `v_tname` varchar(50) NOT NULL,
  `v_vname` varchar(50) NOT NULL,
  `v_status` enum('Active','Deactive') NOT NULL,
  `v_cdate` datetime NOT NULL,
  `v_udate` datetime NOT NULL,
  PRIMARY KEY (`v_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `village_tb`
--

INSERT INTO `village_tb` (`v_id`, `v_dname`, `v_tname`, `v_vname`, `v_status`, `v_cdate`, `v_udate`) VALUES
(1, 'Gandhinagar', 'Gandhinagar', 'Raysan', 'Active', '2025-01-08 15:32:52', '2025-01-08 15:32:52'),
(2, 'Gandhinagar', 'Gandhinagar', 'Sargasan', 'Active', '2025-01-08 15:34:16', '2025-01-08 15:34:16'),
(3, 'Gandhinagar', 'Gandhinagar', 'Kudasan', 'Active', '2025-01-08 15:34:35', '2025-01-08 15:34:35'),
(4, 'Gandhinagar', 'Gandhinagar', 'Pethapur', 'Active', '2025-01-08 15:34:53', '2025-01-08 15:34:53'),
(5, 'Gandhinagar', 'Dehgam', 'Babra', 'Active', '2025-01-08 15:35:39', '2025-01-08 15:35:39'),
(9, 'Gandhinagar', 'Dehgam', 'Dehgam', 'Active', '2025-01-08 15:41:20', '2025-01-08 15:41:20'),
(8, 'Gandhinagar', 'Dehgam', 'Halisa', 'Active', '2025-01-08 15:36:34', '2025-01-08 15:36:34'),
(17, 'Gandhinagar', 'Mansa', 'Ajol', 'Active', '2025-01-08 15:46:28', '2025-01-08 15:46:28'),
(18, 'Gandhinagar', 'Mansa', 'Charada', 'Active', '2025-01-08 15:46:37', '2025-01-08 15:46:37'),
(16, 'Gandhinagar', 'Mansa', 'Mansa', 'Active', '2025-01-08 15:46:20', '2025-01-08 15:46:20'),
(15, 'Gandhinagar', 'Dehgam', 'Badpur', 'Active', '2025-01-08 15:46:00', '2025-01-08 15:46:00'),
(19, 'Gandhinagar', 'Mansa', 'Amarapur', 'Active', '2025-01-08 15:47:31', '2025-01-08 15:47:31'),
(20, 'Gandhinagar', 'Kalol', 'Kalol', 'Active', '2025-01-08 15:48:14', '2025-01-08 15:48:14'),
(21, 'Gandhinagar', 'Kalol', 'Aluva', 'Active', '2025-01-08 15:48:41', '2025-01-08 15:48:41'),
(22, 'Gandhinagar', 'Kalol', 'Balva', 'Active', '2025-01-08 15:48:52', '2025-01-08 15:48:52'),
(23, 'Gandhinagar', 'Kalol', 'Bhadol', 'Active', '2025-01-08 15:49:03', '2025-01-08 15:49:03');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
