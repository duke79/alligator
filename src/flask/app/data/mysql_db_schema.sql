-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: yojaka
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `yojaka`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `yojaka` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

USE `yojaka`;

--
-- Table structure for table `issues`
--

DROP TABLE IF EXISTS `issues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `issues` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `project` int(10) unsigned DEFAULT NULL COMMENT 'in future, owner can be project instead of a user?',
  `count` int(10) unsigned NOT NULL DEFAULT '1',
  `title` varchar(500) DEFAULT NULL,
  `state` varchar(50) NOT NULL DEFAULT 'open' COMMENT 'allow ''open'' & ''closed''',
  `created_by_id` int(10) unsigned DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_by_id` int(10) unsigned DEFAULT NULL,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `description` text,
  `closed_at` datetime DEFAULT NULL,
  `closed_by_id` int(10) unsigned DEFAULT NULL,
  `discussion_locked` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_count` (`project`,`count`),
  KEY `FK_issue_created_by` (`created_by_id`),
  KEY `FK_issue_closed_by` (`closed_by_id`),
  KEY `FK_issues_user` (`updated_by_id`),
  CONSTRAINT `FK_issue_closed_by` FOREIGN KEY (`closed_by_id`) REFERENCES `user` (`id`) ON DELETE SET NULL,
  CONSTRAINT `FK_issue_created_by` FOREIGN KEY (`created_by_id`) REFERENCES `user` (`id`) ON DELETE SET NULL,
  CONSTRAINT `FK_issues_project` FOREIGN KEY (`project`) REFERENCES `project` (`id`) ON DELETE SET NULL,
  CONSTRAINT `FK_issues_user` FOREIGN KEY (`updated_by_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `permissions` (
  `user_id` int(11) unsigned NOT NULL,
  `permission_bit` int(11) unsigned NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY `FK_permissions_user` (`user_id`),
  KEY `FK_permissions_permissions_schema` (`permission_bit`),
  CONSTRAINT `FK_permissions_permissions_schema` FOREIGN KEY (`permission_bit`) REFERENCES `permissions_schema` (`bit`),
  CONSTRAINT `FK_permissions_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `permissions_schema`
--

DROP TABLE IF EXISTS `permissions_schema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `permissions_schema` (
  `bit` int(11) unsigned NOT NULL COMMENT 'must increment exponentially (power of 2)',
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`bit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `project` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `owner` int(10) unsigned DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `issue_counter` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_project_user` (`owner`),
  CONSTRAINT `FK_project_user` FOREIGN KEY (`owner`) REFERENCES `user` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `photo_url` varchar(2013) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `email` varchar(200) DEFAULT NULL,
  `firebase_uid` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-10 18:43:18
