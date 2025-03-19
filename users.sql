-- Table: users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    CONSTRAINT users_email_un UNIQUE KEY (email)
);

-- Table: status
DROP TABLE IF EXISTS status;
CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    CONSTRAINT status_name_un UNIQUE KEY (email)
);

-- Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
