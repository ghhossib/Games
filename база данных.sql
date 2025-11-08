-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Ноя 08 2025 г., 13:05
-- Версия сервера: 8.0.13
-- Версия PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `StaN1234_game_bd`
--

-- --------------------------------------------------------

--
-- Структура таблицы `game`
--

CREATE TABLE `game` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `developer` varchar(100) NOT NULL,
  `releaseYear` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `game`
--

INSERT INTO `game` (`id`, `title`, `developer`, `releaseYear`) VALUES
(1, 'The Witcher 3: Wild Hunt', 'CD Projekt Red', '2015'),
(2, 'Cyberpunk 2077', 'CD Projekt Red', '2020'),
(3, 'Half-Life 2', 'Valve', '2004'),
(4, 'Counter-Strike: Global Offensive', 'Valve', '2012'),
(5, 'StarCraft II', 'Blizzard Entertainment', '2010'),
(6, 'World of Warcraft', 'Blizzard Entertainment', '2004'),
(7, 'The Legend of Zelda: Breath of the Wild', 'Nintendo', '2017'),
(8, 'FIFA 23', 'EA Sports', '2022'),
(9, 'title123123', '23213', '2023'),
(10, 'title123123', '23213', '2023'),
(11, '44', '1', '2'),
(12, '44', '1', '2'),
(13, 'title123123', '23213', '2023'),
(14, 'title123123', '23213', '2023'),
(15, 'title123123', '23213', '2023'),
(16, 'DDD', 'DDD', 'DD'),
(17, 'title1234123', '232413', '20243');

-- --------------------------------------------------------

--
-- Структура таблицы `game_genre`
--

CREATE TABLE `game_genre` (
  `id` int(11) NOT NULL,
  `game_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `game_genre`
--

INSERT INTO `game_genre` (`id`, `game_id`, `genre_id`, `created_at`) VALUES
(1, 1, 2, '2025-11-08 12:49:38'),
(2, 3, 4, '2025-11-08 12:53:15'),
(3, 4, 2, '2025-11-08 12:56:04');

-- --------------------------------------------------------

--
-- Структура таблицы `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `genre`
--

INSERT INTO `genre` (`id`, `name`) VALUES
(4, 'Приключение'),
(3, 'Стратегия'),
(2, 'Шутер'),
(1, 'RPG'),
(5, 'Спорт'),
(6, 'Стандофчик');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `game`
--
ALTER TABLE `game`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `game_genre`
--
ALTER TABLE `game_genre`
  ADD PRIMARY KEY (`id`),
  ADD KEY `gamegenre_game_id` (`game_id`),
  ADD KEY `gamegenre_genre_id` (`genre_id`);

--
-- Индексы таблицы `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `game`
--
ALTER TABLE `game`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT для таблицы `game_genre`
--
ALTER TABLE `game_genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
