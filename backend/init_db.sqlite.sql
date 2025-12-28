-- SQLite schema for customer purchase data
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER REFERENCES customers(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    total REAL NOT NULL,
    purchased_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (name, email) VALUES
('Alice Smith', 'alice@example.com'),
('Bob Jones', 'bob@example.com'),
('Carol Lee', 'carol@example.com');

INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Phone', 800.00),
('Headphones', 150.00);

INSERT INTO purchases (customer_id, product_id, quantity, total) VALUES
(1, 1, 1, 1200.00),
(1, 3, 2, 300.00),
(2, 2, 1, 800.00),
(3, 1, 1, 1200.00),
(3, 2, 2, 1600.00);
