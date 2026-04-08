-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3307
-- Время создания: Апр 08 2026 г., 12:21
-- Версия сервера: 8.0.19
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `markets`
--

-- --------------------------------------------------------

--
-- Структура таблицы `authors`
--

CREATE TABLE `authors` (
  `idAuthor` int NOT NULL,
  `surname` varchar(50) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL DEFAULT 'Россия'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `authors`
--

INSERT INTO `authors` (`idAuthor`, `surname`, `firstname`, `country`) VALUES
(1, 'Пушкин', 'Александр', 'Россия'),
(2, 'Гоголь', 'Николай', 'Украина'),
(3, 'Достоевский', 'Федор', 'Россия'),
(5, 'супер толстый', 'Лев', 'Россия');

-- --------------------------------------------------------

--
-- Структура таблицы `books`
--

CREATE TABLE `books` (
  `idBook` int NOT NULL,
  `idAuthor` int NOT NULL,
  `title` varchar(50) NOT NULL,
  `genre` enum('проза','поэзия','другое') NOT NULL DEFAULT 'проза',
  `price` decimal(6,2) UNSIGNED NOT NULL DEFAULT '0.00',
  `weight` decimal(4,3) UNSIGNED NOT NULL DEFAULT '0.000',
  `pages` smallint NOT NULL DEFAULT '0',
  `yearRelease` smallint DEFAULT NULL,
  `count` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `books`
--

INSERT INTO `books` (`idBook`, `idAuthor`, `title`, `genre`, `price`, `weight`, `pages`, `yearRelease`, `count`) VALUES
(1, 1, 'Книга 1', 'другое', '2000.00', '2.000', 100, 2026, 50),
(2, 2, 'Книга 2', 'другое', '200.00', '4.000', 10, 2026, 30),
(3, 3, 'Книга 3', 'другое', '200.00', '5.000', 55, 2020, 50),
(4, 1, 'Книга', 'другое', '5000.00', '4.000', 11, 2026, 50),
(5, 1, '2', 'другое', '5000.00', '6.700', 67, 67, 67);

--
-- Триггеры `books`
--
DELIMITER $$
CREATE TRIGGER `BeforeBookInsert` BEFORE INSERT ON `books` FOR EACH ROW BEGIN
    IF NEW.price > 5000 THEN
        SET NEW.price = 5000;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `books_has_orders`
--

CREATE TABLE `books_has_orders` (
  `Books_idBook` int NOT NULL,
  `Orders_idOrder` int NOT NULL,
  `Count` tinyint NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Триггеры `books_has_orders`
--
DELIMITER $$
CREATE TRIGGER `BeforeOrderInsert` BEFORE INSERT ON `books_has_orders` FOR EACH ROW BEGIN
    UPDATE books 
    SET count = count - NEW.Count
    WHERE idBook = NEW.Books_idBook;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `customers`
--

CREATE TABLE `customers` (
  `idCustomer` int NOT NULL,
  `login` varchar(20) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `adress` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Триггеры `customers`
--
DELIMITER $$
CREATE TRIGGER `BeforeCustomerDelete` BEFORE DELETE ON `customers` FOR EACH ROW BEGIN
    DELETE FROM books_has_orders 
    WHERE Orders_idOrder IN (
        SELECT idOrder FROM orders 
        WHERE idCustomer = OLD.idCustomer
    );
    
    DELETE FROM orders 
    WHERE idCustomer = OLD.idCustomer;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `idOrder` int NOT NULL,
  `idCustomer` int NOT NULL,
  `dateTimeOrder` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Триггеры `orders`
--
DELIMITER $$
CREATE TRIGGER `BeforeOrdersInsert` BEFORE INSERT ON `orders` FOR EACH ROW BEGIN
	SET NEW.dateTimeOrder = NOW();
END
$$
DELIMITER ;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`idAuthor`);

--
-- Индексы таблицы `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`idBook`),
  ADD KEY `idAuthor_idx` (`idAuthor`);

--
-- Индексы таблицы `books_has_orders`
--
ALTER TABLE `books_has_orders`
  ADD PRIMARY KEY (`Books_idBook`,`Orders_idOrder`),
  ADD KEY `fk_Books_has_Orders_Orders1_idx` (`Orders_idOrder`),
  ADD KEY `fk_Books_has_Orders_Books1_idx` (`Books_idBook`);

--
-- Индексы таблицы `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`idCustomer`),
  ADD UNIQUE KEY `login_UNIQUE` (`login`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`idOrder`),
  ADD KEY `idCustomer_idx` (`idCustomer`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `authors`
--
ALTER TABLE `authors`
  MODIFY `idAuthor` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `books`
--
ALTER TABLE `books`
  MODIFY `idBook` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `customers`
--
ALTER TABLE `customers`
  MODIFY `idCustomer` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `orders`
--
ALTER TABLE `orders`
  MODIFY `idOrder` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `idAuthor` FOREIGN KEY (`idAuthor`) REFERENCES `authors` (`idAuthor`) ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `books_has_orders`
--
ALTER TABLE `books_has_orders`
  ADD CONSTRAINT `fk_Books_has_Orders_Books1` FOREIGN KEY (`Books_idBook`) REFERENCES `books` (`idBook`),
  ADD CONSTRAINT `fk_Books_has_Orders_Orders1` FOREIGN KEY (`Orders_idOrder`) REFERENCES `orders` (`idOrder`);

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `idCustomer` FOREIGN KEY (`idCustomer`) REFERENCES `customers` (`idCustomer`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
