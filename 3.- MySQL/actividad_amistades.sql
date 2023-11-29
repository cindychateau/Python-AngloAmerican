INSERT INTO users (first_name, last_name) VALUES 
("Juana", "De Arco"),
("Pablo", "Picasso"),
("Pedro", "Páramo"),
("Gabriel", "García Márquez"),
("Stephen", "King");

INSERT INTO friendships (user_id, friend_id) VALUES 
(1, 2),
(1, 4),
(1, 6);

INSERT INTO friendships (user_id, friend_id) VALUES
(2, 1),
(2, 3),
(2, 5);

INSERT INTO friendships (user_id, friend_id) VALUES
(3, 2),
(3, 5);

INSERT INTO friendships (user_id, friend_id) VALUES (4, 3);

INSERT INTO friendships (user_id, friend_id) VALUES 
(5, 1),
(5, 6);

INSERT INTO friendships (user_id, friend_id) VALUES 
(6, 2),
(6, 3);

SELECT users.first_name, users.last_name, amigos.first_name as friend_first_name, amigos.last_name as friend_last_name
FROM users
JOIN friendships ON friendships.user_id = users.id
JOIN users as amigos ON friendships.friend_id = amigos.id;

SELECT users.first_name, users.last_name, amigos.first_name as friend_first_name, amigos.last_name as friend_last_name
FROM users
JOIN friendships ON friendships.user_id = users.id
JOIN users as amigos ON friendships.friend_id = amigos.id
WHERE users.id = 1;

SELECT COUNT(*) FROM friendships;
