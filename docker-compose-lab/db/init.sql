CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO users (name) 
VALUES 
    ('Alice'), 
    ('Bob'), 
    ('Charlie'), 
    ('David'), 
    ('Emma'), 
    ('Frank'), 
    ('Grace'), 
    ('Helen'), 
    ('Ivy'), 
    ('Jack'), 
    ('Karen'), 
    ('Leo'), 
    ('Mona'), 
    ('Nina'), 
    ('Oliver');
