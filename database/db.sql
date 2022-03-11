CREATE TABLE IF NOT EXISTS products (
    code INT(4) UNSIGNED ZEROFILL NOT NULL,
    name CHAR(50),
    stock INT NOT NULL,
    value FLOAT,
    category_id tinyint NULL,
    PRIMARY KEY(code)
);

CREATE TABLE IF NOT EXISTS categories(
    id tinyint NOT NULL,
    name CHAR(50) NOT NULL,
    description VARCHAR(200),
    PRIMARY KEY(id)
);

ALTER TABLE products ADD FOREIGN KEY(category_id) REFERENCES categories(id)