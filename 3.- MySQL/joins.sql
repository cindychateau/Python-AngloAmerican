SELECT * FROM usuarios;

SELECT * FROM usuarios
JOIN direcciones ON direcciones.id = usuarios.direccion_id;

SELECT nombre, edad, calle
FROM usuarios
JOIN direcciones ON direcciones.id = usuarios.direccion_id;

SELECT *
FROM pedidos
JOIN usuarios ON usuarios.id = pedidos.usuario_id;


SELECT *
FROM pedidos
JOIN usuarios ON usuarios.id = pedidos.usuario_id
WHERE total > 500;

SELECT usuarios.id, nombre, actividad
FROM usuarios
JOIN usuarios_has_hobbies ON usuarios_has_hobbies.usuario_id = usuarios.id
JOIN hobbies ON hobbies.id = usuarios_has_hobbies.hobbie_id
WHERE usuarios.id = 1
ORDER BY actividad ASC; 


