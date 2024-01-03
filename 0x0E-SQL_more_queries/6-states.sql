-- creates the table id_not_null on your MySQL server.
-- * id_not_null description:
-- * id INT with the default value 1 and must be unique
-- * name VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null (id INT unique default 1, name VARCHAR(256));
