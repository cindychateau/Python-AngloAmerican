-- ¿Qué consulta ejecutarías para obtener todos los clientes dentro de ciudad_id = 312? Tu consulta debe devolver el nombre, apellido, correo electrónico y dirección del cliente.
SELECT first_name, last_name, email, address, address2, postal_code 
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE city_id = 312;

-- ¿Qué consulta ejecutarías para obtener todas las películas de comedias? 
-- Tu consulta debe devolver el título de la película, la descripción, el año de lanzamiento, la clasificación, las características especiales y el género (categoría).
SELECT title, description, release_year, rating, special_features, name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- ¿Qué consulta ejecutarías para obtener todas las películas por actor_id=5? 
-- Tu consulta debe devolver el id del actor, el nombre del actor, el título de la película, la descripción y el año de lanzamiento.
SELECT actor.actor_id, first_name, last_name, title, description, release_year
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

-- ¿Qué consulta ejecutarías para obtener todos los clientes en store_id=1 y dentro de estas ciudades (1, 42, 312 y 459)?
-- Tu consulta debe devolver el nombre, apellido, correo electrónico y dirección del cliente.
SELECT first_name, last_name, email, address
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE store_id = 1
AND city_id IN (1, 42, 312, 459); -- AND (city_id = 1 OR city_id = 42 OR city_id = 312...)

-- ¿Qué consulta ejecutarías para obtener todas las películas con una "calificación = G" y una "característica especial = detrás de escena", unidas por actor_id = 15?  
-- Tu consulta debe devolver el título de la película, la descripción, el año de lanzamiento, la clasificación y la característica especial.
SELECT title, description, release_year, rating, special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
WHERE rating = "G"
AND special_features LIKE '%Behind the scenes%' -- AJSKASMlBehind the scenes.        Behind the scenesdaksj
AND actor_id = 15;

-- ¿Qué consulta ejecutarías para obtener todos los actores que se unieron al film_id = 369? 
-- Tu consulta debe devolver film_id, título, actor_id y actor_name.
SELECT film.film_id, title, actor.actor_id, first_name, last_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- ¿Qué consulta ejecutarías para obtener todas las películas de drama con una tarifa de arriendo de 2,99? 
-- Tu consulta debe devolver el título de la película, la descripción, el año de lanzamiento, la clasificación, las características especiales y el género (categoría).
SELECT title, description, release_year, special_features, name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE name = 'Drama'
AND rental_rate = 2.99;

-- ¿Qué consulta ejecutarías para obtener todas las películas de acción que estén unidas por SANDRA KILMER? 
-- Tu consulta debe devolver el título de la película, la descripción, el año de lanzamiento, 
-- la clasificación, las características especiales, el género (categoría) y 
-- el nombre y apellido del actor.
SELECT title, description, release_year, rating, special_features, name, first_name, last_name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = "Action"
AND actor.first_name = "Sandra"
AND actor.last_name = "Kilmer";
