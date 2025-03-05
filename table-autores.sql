DROP DATABASE IF EXISTS  bd_pylib ;
CREATE DATABASE  bd_pylib ;
USE  bd_pylib ;

CREATE TABLE IF NOT EXISTS autores
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    fecha_fallecimiento DATE
);

CREATE TABLE IF NOT EXISTS editoriales
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    fundacion DATE,
    website VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS libros
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    fecha_publicacion DATE,
    precio DECIMAL(10, 2),
    id_editorial INT,
    FOREIGN KEY (id_editorial) REFERENCES editoriales(id)
);

CREATE TABLE IF NOT EXISTS libros_autores
(
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES libros(id),
    FOREIGN KEY (id_autor) REFERENCES autores(id)
);

-- Inserción de datos en la tabla autores
INSERT INTO autores (nombre, apellidos, nacionalidad, fecha_nacimiento, fecha_fallecimiento)
VALUES 
('Gabriel', 'García Márquez', 'Colombiana', '1927-03-06', '2014-04-17'),
('Haruki', 'Murakami', 'Japonesa', '1949-01-12', NULL),
('Jane', 'Austen', 'Británica', '1775-12-16', '1817-07-18'),
('George', 'Orwell', 'Británica', '1903-06-25', '1950-01-21'),
('Isabel', 'Allende', 'Chilena', '1942-08-02', NULL),
('Franz', 'Kafka', 'Checa', '1883-07-03', '1924-06-03'),
('J.K.', 'Rowling', 'Británica', '1965-07-31', NULL),
('F. Scott', 'Fitzgerald', 'Estadounidense', '1896-09-24', '1940-12-21'),
('Miguel', 'de Cervantes', 'Española', '1547-09-29', '1616-04-23'),
('Leo', 'Tolstoy', 'Rusa', '1828-09-09', '1910-11-20');

-- Inserción de datos en la tabla editoriales
INSERT INTO editoriales (nombre, ciudad, pais, fundacion, website)
VALUES 
('Penguin Random House', 'Nueva York', 'EE.UU.', '1925-07-01', 'https://www.penguinrandomhouse.com'),
('HarperCollins', 'Nueva York', 'EE.UU.', '1989-08-01', 'https://www.harpercollins.com'),
('Simon & Schuster', 'Nueva York', 'EE.UU.', '1924-01-02', 'https://www.simonandschuster.com'),
('Macmillan', 'Londres', 'Reino Unido', '1843-01-01', 'https://us.macmillan.com'),
('Hachette Livre', 'París', 'Francia', '1826-01-01', 'https://www.hachette.com'),
('Planeta', 'Barcelona', 'España', '1949-10-02', 'https://www.planetadelibros.com'),
('Scholastic', 'Nueva York', 'EE.UU.', '1920-10-22', 'https://www.scholastic.com'),
('Alfaguara', 'Madrid', 'España', '1964-01-01', 'https://www.penguinlibros.com'),
('Gallimard', 'París', 'Francia', '1911-01-01', 'https://www.gallimard.fr'),
('Vintage', 'Nueva York', 'EE.UU.', '1954-01-01', 'https://www.penguinrandomhouse.com');

-- Inserción de datos en la tabla libros
INSERT INTO libros (titulo, fecha_publicacion, precio, id_editorial)
VALUES 
('Cien años de soledad', '1967-05-30', 19.99, 1),
('Kafka en la orilla', '2002-09-12', 14.99, 2),
('Orgullo y prejuicio', '1813-01-28', 9.99, 3),
('1984', '1949-06-08', 15.99, 4),
('La casa de los espíritus', '1982-01-01', 16.99, 5),
('La metamorfosis', '1915-01-01', 7.99, 6),
('Harry Potter y la piedra filosofal', '1997-06-26', 12.99, 7),
('El gran Gatsby', '1925-04-10', 10.99, 8),
('Don Quijote de la Mancha', '1605-01-16', 13.99, 9),
('Guerra y paz', '1869-01-01', 18.99, 10);

-- Inserción de datos en la tabla libros_autores
INSERT INTO libros_autores (id_libro, id_autor)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);
    
