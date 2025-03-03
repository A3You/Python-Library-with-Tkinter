CREATE TABLE IF NOT EXISTS autores
(
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    fecha_fallecimiento DATE
);

CREATE TABLE IF NOT EXISTS editoriales
(
    id_editorial INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    fundacion DATE,
    website VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS libros
(
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    fecha_publicacion DATE,
    precio DECIMAL(10, 2),
    id_editorial INT,
    FOREIGN KEY (id_editorial) REFERENCES editoriales(id_editorial)
);

CREATE TABLE IF NOT EXISTS libros_autores
(
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro),
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

CREATE TABLE IF NOT EXISTS roles
(
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios
(
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    id_rol INT,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

