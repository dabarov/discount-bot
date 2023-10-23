CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    external_id VARCHAR(100) NOT NULL,
    uri VARCHAR(100) NOT NULL,
    source VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    UNIQUE (external_id, source)
);
CREATE INDEX external_id_idx ON items(external_id);
CREATE TABLE prices (
    id INTEGER PRIMARY KEY,
    item_id INT NOT NULL,
    price int,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(id)
);
CREATE INDEX item_id_idx ON prices(item_id);