-- Guardamos un nuevo registro
-- INSERT INTO tabla (columna1, columna2) VALUES ('valor1', 'valor2');
INSERT INTO usuarios (nombre, edad, dojo_id) VALUES ('Juana', 30, 4);

SELECT * FROM usuarios;

-- Eliminamos el registro
DELETE FROM usuarios WHERE id = 9; -- WHERE id >= 9 AND id <= 40

-- Actualizar
UPDATE usuarios SET nombre = 'Juanita', edad = 31 WHERE id = 8;

