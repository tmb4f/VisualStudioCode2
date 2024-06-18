CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Vivian', 15);
INSERT INTO Ages (name, age) VALUES ('Jaimee', 27);
INSERT INTO Ages (name, age) VALUES ('Taylor', 32);
INSERT INTO Ages (name, age) VALUES ('Bentley', 40);

SELECT hex(name || age) AS X FROM Ages ORDER BY X