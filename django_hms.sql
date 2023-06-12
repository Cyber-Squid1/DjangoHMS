-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 12, 2023 at 09:22 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `django_hms`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add feedback', 7, 'add_feedback'),
(26, 'Can change feedback', 7, 'change_feedback'),
(27, 'Can delete feedback', 7, 'delete_feedback'),
(28, 'Can view feedback', 7, 'view_feedback'),
(29, 'Can add patient', 8, 'add_patient'),
(30, 'Can change patient', 8, 'change_patient'),
(31, 'Can delete patient', 8, 'delete_patient'),
(32, 'Can view patient', 8, 'view_patient'),
(33, 'Can add specialization', 9, 'add_specialization'),
(34, 'Can change specialization', 9, 'change_specialization'),
(35, 'Can delete specialization', 9, 'delete_specialization'),
(36, 'Can view specialization', 9, 'view_specialization'),
(37, 'Can add doctor', 10, 'add_doctor'),
(38, 'Can change doctor', 10, 'change_doctor'),
(39, 'Can delete doctor', 10, 'delete_doctor'),
(40, 'Can view doctor', 10, 'view_doctor'),
(41, 'Can add appointment', 11, 'add_appointment'),
(42, 'Can change appointment', 11, 'change_appointment'),
(43, 'Can delete appointment', 11, 'delete_appointment'),
(44, 'Can view appointment', 11, 'view_appointment'),
(45, 'Can add admitted patient details', 12, 'add_admittedpatientdetails'),
(46, 'Can change admitted patient details', 12, 'change_admittedpatientdetails'),
(47, 'Can delete admitted patient details', 12, 'delete_admittedpatientdetails'),
(48, 'Can view admitted patient details', 12, 'view_admittedpatientdetails');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$GAUCGTviqb3xmADMgk59CZ$w9AG79Ylih+iXULG9/LQhUfXbtBDCoXf0CQuqC+uesE=', '2023-06-12 13:35:06.294419', 1, 'ompatel', '', '', 'ompatel22072002@gmail.com', 1, 1, '2023-06-12 13:33:06.638465');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-06-12 13:45:42.615313', '2', 'Dr. ABC', 1, '[{\"added\": {}}]', 10, 1),
(2, '2023-06-12 13:46:13.420498', '3', 'Dr. XYZ', 1, '[{\"added\": {}}]', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(12, 'HMS', 'admittedpatientdetails'),
(11, 'HMS', 'appointment'),
(10, 'HMS', 'doctor'),
(7, 'HMS', 'feedback'),
(8, 'HMS', 'patient'),
(9, 'HMS', 'specialization'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'HMS', '0001_initial', '2023-06-12 13:31:48.412164'),
(2, 'HMS', '0002_remove_patient_assigneddoctorid_delete_doctor_and_more', '2023-06-12 13:31:53.445266'),
(3, 'HMS', '0003_initial', '2023-06-12 13:32:01.441293'),
(4, 'HMS', '0004_rename_assigneddoctorid_patient_currentlyassigneddoctorid_and_more', '2023-06-12 13:32:03.286293'),
(5, 'HMS', '0005_feedback', '2023-06-12 13:32:03.601316'),
(6, 'HMS', '0006_patient_patientusername', '2023-06-12 13:32:03.806431'),
(7, 'HMS', '0007_alter_patient_patientusername', '2023-06-12 13:32:03.840957'),
(8, 'HMS', '0008_alter_doctor_phone_alter_feedback_phonenumber_and_more', '2023-06-12 13:32:07.729510'),
(9, 'HMS', '0009_remove_patient_patientusername', '2023-06-12 13:32:07.916869'),
(10, 'HMS', '0010_alter_patient_patientprofileimg', '2023-06-12 13:32:07.974965'),
(11, 'HMS', '0011_alter_patient_patientmedicalreport_and_more', '2023-06-12 13:32:08.026676'),
(12, 'HMS', '0012_alter_patient_currentlyassigneddoctorid', '2023-06-12 13:32:09.464509'),
(13, 'HMS', '0013_doctor_availableon', '2023-06-12 13:32:09.640436'),
(14, 'HMS', '0014_specialization_alter_doctor_specialization', '2023-06-12 13:32:12.335782'),
(15, 'HMS', '0015_alter_specialization_specialization', '2023-06-12 13:32:12.666856'),
(16, 'HMS', '0016_remove_admittedpatientdetails_appointmentdetailsid_and_more', '2023-06-12 13:32:17.331124'),
(17, 'HMS', '0017_initial', '2023-06-12 13:32:25.562176'),
(18, 'contenttypes', '0001_initial', '2023-06-12 13:32:26.286449'),
(19, 'auth', '0001_initial', '2023-06-12 13:32:36.205295'),
(20, 'admin', '0001_initial', '2023-06-12 13:32:37.919035'),
(21, 'admin', '0002_logentry_remove_auto_add', '2023-06-12 13:32:37.988400'),
(22, 'admin', '0003_logentry_add_action_flag_choices', '2023-06-12 13:32:38.073771'),
(23, 'contenttypes', '0002_remove_content_type_name', '2023-06-12 13:32:38.898906'),
(24, 'auth', '0002_alter_permission_name_max_length', '2023-06-12 13:32:39.747431'),
(25, 'auth', '0003_alter_user_email_max_length', '2023-06-12 13:32:40.044020'),
(26, 'auth', '0004_alter_user_username_opts', '2023-06-12 13:32:40.163488'),
(27, 'auth', '0005_alter_user_last_login_null', '2023-06-12 13:32:40.711571'),
(28, 'auth', '0006_require_contenttypes_0002', '2023-06-12 13:32:40.913530'),
(29, 'auth', '0007_alter_validators_add_error_messages', '2023-06-12 13:32:40.968184'),
(30, 'auth', '0008_alter_user_username_max_length', '2023-06-12 13:32:41.397691'),
(31, 'auth', '0009_alter_user_last_name_max_length', '2023-06-12 13:32:41.797333'),
(32, 'auth', '0010_alter_group_name_max_length', '2023-06-12 13:32:41.994497'),
(33, 'auth', '0011_update_proxy_permissions', '2023-06-12 13:32:42.078081'),
(34, 'auth', '0012_alter_user_first_name_max_length', '2023-06-12 13:32:42.186948'),
(35, 'sessions', '0001_initial', '2023-06-12 13:32:42.752572'),
(36, 'HMS', '0018_alter_admittedpatientdetails_appointmentdetailsid_and_more', '2023-06-12 17:48:06.752423'),
(37, 'HMS', '0019_alter_admittedpatientdetails_appointmentdetailsid_and_more', '2023-06-12 17:48:37.148941'),
(38, 'HMS', '0020_appointment', '2023-06-12 17:48:54.020978'),
(39, 'HMS', '0021_alter_admittedpatientdetails_doctoridid_and_more', '2023-06-12 17:49:12.599055'),
(40, 'HMS', '0022_rename_doctoridid_admittedpatientdetails_doctorid_and_more', '2023-06-12 17:50:05.454035');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zfcvbdhhgd3t740954vaom2ple5tcsir', '.eJxVjssOgjAQRf-FtWn6BlwZo0u_gUzbqaBAsZSV8d8tCQtYTXLPuTfzLRpYUtssM8amc8W5YMVpnxmwbxxX4F4wPgOxYUyxM2RVyEZn8ggO--vmHgZamNvcVobWlGmtUct8vEDGuAdRubpmikmvJBdYUVVpkF6D0t44JUpLmZLKYR7FAbo-T4VhgoQ957TklPLLc83zX0N2bsGmEO-bOX3igboDBWN39PcH_1tWbw:1q8n4o:kSK3xYqIGFXS2XlesvHeTI8cQ0ASfXWpLSgsOa4tQqw', '2023-06-26 19:19:42.971343');

-- --------------------------------------------------------

--
-- Table structure for table `hms_admittedpatientdetails`
--

CREATE TABLE `hms_admittedpatientdetails` (
  `id` bigint(20) NOT NULL,
  `admittedOn` date NOT NULL,
  `dischargeDate` date NOT NULL,
  `roomCharges` int(11) NOT NULL,
  `MedicineCost` int(11) NOT NULL,
  `doctorFees` int(11) NOT NULL,
  `otherCharges` int(11) NOT NULL,
  `totalCost` int(11) NOT NULL,
  `appointmentDetailsId` varchar(10) NOT NULL,
  `doctorId` varchar(10) NOT NULL,
  `patientId` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `hms_appointment`
--

CREATE TABLE `hms_appointment` (
  `id` bigint(20) NOT NULL,
  `patientId` varchar(10) NOT NULL,
  `doctorId` varchar(10) NOT NULL,
  `appointmentDate` date NOT NULL,
  `description` longtext NOT NULL,
  `medicinePrescribed` varchar(1000) NOT NULL,
  `appointmentCost` int(11) NOT NULL,
  `wasAdmitted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hms_appointment`
--

INSERT INTO `hms_appointment` (`id`, `patientId`, `doctorId`, `appointmentDate`, `description`, `medicinePrescribed`, `appointmentCost`, `wasAdmitted`) VALUES
(7, '1', '2', '2023-06-13', '', '', 800, 0);

-- --------------------------------------------------------

--
-- Table structure for table `hms_doctor`
--

CREATE TABLE `hms_doctor` (
  `id` bigint(20) NOT NULL,
  `doctorName` varchar(200) NOT NULL,
  `doctorEmail` varchar(254) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  `address` varchar(300) NOT NULL,
  `doctorProfileImg` varchar(100) NOT NULL,
  `availableOn` varchar(10) NOT NULL,
  `specialization_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hms_doctor`
--

INSERT INTO `hms_doctor` (`id`, `doctorName`, `doctorEmail`, `phone`, `password`, `address`, `doctorProfileImg`, `availableOn`, `specialization_id`) VALUES
(1, 'Dr. PQR', 'pqr@gmail.com', 3030303030, '159753', 'Rajkot', 'doctorProfileImg/basketball_s1qFwoD.jpg', '3', 2),
(2, 'Dr. ABC', 'abc@gmail.com', 1010101010, '123456', 'Jamnagar', 'doctorProfileImg/basketball_djXHU4U.jpg', '1', 3),
(3, 'Dr. XYZ', 'xyz@gmail.com', 2020202020, '987654', 'Mumbai', 'doctorProfileImg/basketball_s1qFwoD.jpg', '2', 3);

-- --------------------------------------------------------

--
-- Table structure for table `hms_feedback`
--

CREATE TABLE `hms_feedback` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phonenumber` bigint(20) NOT NULL,
  `message` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `hms_patient`
--

CREATE TABLE `hms_patient` (
  `id` bigint(20) NOT NULL,
  `patientName` varchar(200) NOT NULL,
  `patientEmail` varchar(254) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `password` varchar(200) NOT NULL,
  `address` varchar(300) NOT NULL,
  `patientProfileImg` varchar(100) NOT NULL,
  `symptoms` varchar(1000) NOT NULL,
  `currentlyAssignedDoctorId` varchar(8) NOT NULL,
  `patientMedicalReport` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hms_patient`
--

INSERT INTO `hms_patient` (`id`, `patientName`, `patientEmail`, `phone`, `password`, `address`, `patientProfileImg`, `symptoms`, `currentlyAssignedDoctorId`, `patientMedicalReport`) VALUES
(1, 'Om Patel', 'ompatel22072002@gmail.com', 7016104220, '123456', 'Jamnagar', '', '', '2', '');

-- --------------------------------------------------------

--
-- Table structure for table `hms_specialization`
--

CREATE TABLE `hms_specialization` (
  `id` bigint(20) NOT NULL,
  `specialization` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hms_specialization`
--

INSERT INTO `hms_specialization` (`id`, `specialization`) VALUES
(3, 'Dentist'),
(1, 'General Doctor'),
(4, 'Neurologist'),
(2, 'Physician');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `hms_admittedpatientdetails`
--
ALTER TABLE `hms_admittedpatientdetails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hms_appointment`
--
ALTER TABLE `hms_appointment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hms_doctor`
--
ALTER TABLE `hms_doctor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `HMS_doctor_specialization_id_3a336175_fk_HMS_specialization_id` (`specialization_id`);

--
-- Indexes for table `hms_feedback`
--
ALTER TABLE `hms_feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hms_patient`
--
ALTER TABLE `hms_patient`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hms_specialization`
--
ALTER TABLE `hms_specialization`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `specialization` (`specialization`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `hms_admittedpatientdetails`
--
ALTER TABLE `hms_admittedpatientdetails`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hms_appointment`
--
ALTER TABLE `hms_appointment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `hms_doctor`
--
ALTER TABLE `hms_doctor`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `hms_feedback`
--
ALTER TABLE `hms_feedback`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hms_patient`
--
ALTER TABLE `hms_patient`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `hms_specialization`
--
ALTER TABLE `hms_specialization`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `hms_doctor`
--
ALTER TABLE `hms_doctor`
  ADD CONSTRAINT `HMS_doctor_specialization_id_3a336175_fk_HMS_specialization_id` FOREIGN KEY (`specialization_id`) REFERENCES `hms_specialization` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;