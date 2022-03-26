-- This file will be used to create the sql database and tables.
USE `certify`;
CREATE TABLE IF NOT EXISTS `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL, -- Corresponds to the user's wikipedia username
    `email` varchar(255) NOT NULL, -- Corresponds to the user's email address
    `password` varchar(255) NOT NULL-- Corresponds to the user's password
)