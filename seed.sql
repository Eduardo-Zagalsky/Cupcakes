DROP DATABASE IF EXISTS cupcake;

CREATE DATABASE cupcake;

\c cupcake
CREATE TABLE cupcakes (
    id serial PRIMARY KEY,
    flavor text NOT NULL,
    size text NOT NULL,
    rating float NOT NULL,
    img text DEFAULT 'https://tinyurl.com/demo-cupcake'
);

INSERT INTO cupcakes (flavor, size, rating, img)
    VALUES ('cherry', 'large', 5, DEFAULT), ('chocolate', 'small', 9, 'https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg');

