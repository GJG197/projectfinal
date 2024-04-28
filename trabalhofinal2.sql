-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-04-2024 a las 12:52:28
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `trabalhofinal2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `hardware_tickets`
--

CREATE TABLE `hardware_tickets` (
  `id` int(11) NOT NULL,
  `numero_sequencial` int(11) NOT NULL,
  `data_hora` datetime NOT NULL,
  `codigo_colaborador` varchar(50) NOT NULL,
  `equipamento` varchar(100) NOT NULL,
  `avaria` text NOT NULL,
  `descricao_reparacao` text NOT NULL,
  `estado_hardware` enum('Avariado','Reparado','Não Reparado','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `hardware_tickets`
--

INSERT INTO `hardware_tickets` (`id`, `numero_sequencial`, `data_hora`, `codigo_colaborador`, `equipamento`, `avaria`, `descricao_reparacao`, `estado_hardware`) VALUES
(1, 1, '2024-04-28 11:28:12', '23', 'motherboard trocada', 'nenhuma', 'software actualizacao', 'Reparado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `software_tickets`
--

CREATE TABLE `software_tickets` (
  `id` int(11) NOT NULL,
  `numero_sequencial` int(11) NOT NULL,
  `data_hora` datetime NOT NULL,
  `codigo_colaborador` varchar(50) NOT NULL,
  `software` varchar(100) NOT NULL,
  `descricao_necessidade` text NOT NULL,
  `estado_software` enum('Necessita atualização','Atualizado','Não atualizado','') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `software_tickets`
--

INSERT INTO `software_tickets` (`id`, `numero_sequencial`, `data_hora`, `codigo_colaborador`, `software`, `descricao_necessidade`, `estado_software`) VALUES
(1, 0, '2024-04-27 17:34:31', '2', 'atualizado', 'feito', 'Não atualizado'),
(2, 12345, '2024-04-27 17:44:31', '23', 'avaria', '', '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `hardware_tickets`
--
ALTER TABLE `hardware_tickets`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `software_tickets`
--
ALTER TABLE `software_tickets`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `hardware_tickets`
--
ALTER TABLE `hardware_tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `software_tickets`
--
ALTER TABLE `software_tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
