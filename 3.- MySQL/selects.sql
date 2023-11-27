-- Comentario
-- SELECT -> Consulta sobre una tabla

-- SELECT * FROM tabla (Selecciona todas las columnas de la tabla de usuarios)
SELECT * FROM usuarios;

-- SELECT columna1, columna2 FROM tabla (Despliega las columnas nombre y edad de la tabla de usuarios)
SELECT nombre, edad FROM usuarios;

-- SELECT columna1, columna2 FROM tabla WHERE id = idbusqueda 
-- (Despliega las columnas nombre y edad de la tabla de usuarios donde el id = 2)
SELECT nombre, edad FROM usuarios WHERE id = 2;

-- Despliega todas las columnas de la tabla de usuarios donde nombre es "Martina"
SELECT * FROM usuarios WHERE nombre LIKE "Martina";

-- Depliega todas las columnas de la tabla de usuarios donde nombre comience con "Al"
-- % = comodin (no me importa que más haya en ese espacio)
SELECT * FROM usuarios WHERE nombre LIKE "Al%";

SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o";

SELECT nombre, edad FROM usuarios WHERE nombre LIKE "a%o";

SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%n%";

SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o" AND edad > 23;

SELECT * FROM usuarios WHERE edad > 20 AND nombre LIKE "A%" AND id > 3;

-- SELECT columnas FROM tabla ORDER BY columna ASC/DESC
SELECT * FROM usuarios ORDER BY edad DESC;

SELECT * FROM usuarios ORDER BY nombre ASC; -- ASC 1-10 o A-Z.       DESC 10-1 o Z-A 

SELECT nombre, edad FROM usuarios WHERE nombre LIKE "%o" ORDER BY edad DESC;

-- SELECT columna1, columna2 FROM tabla WHERE columna = valor.... ORDER BY columna ASC/DESC;

-- Desplegar las columnas de id, nombre y edad de la tabla de usuarios siempre y cuando su nombre comience con la E
-- y se vean ordenados en base a su edad de más chico a más grande
SELECT id, nombre, edad FROM usuarios WHERE nombre LIKE "E%" ORDER BY edad ASC;
