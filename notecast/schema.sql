DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS cast;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE cast (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    script TEXT NOT NULL,
    location TEXT NOT NULL,
    image TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
);
