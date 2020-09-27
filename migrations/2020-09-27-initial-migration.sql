CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS unsplash;

DROP TABLE IF EXISTS animals;

CREATE TABLE animals (
    id uuid DEFAULT uuid_generate_v4 (),
    species VARCHAR NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE unsplash (
    id uuid DEFAULT uuid_generate_v4 (),
    unsplash_id VARCHAR NOT NULL UNIQUE,
    animal_id uuid,
    PRIMARY KEY (id),
    CONSTRAINT fk_animal FOREIGN KEY (animal_id) REFERENCES animals(id) ON DELETE CASCADE
);
