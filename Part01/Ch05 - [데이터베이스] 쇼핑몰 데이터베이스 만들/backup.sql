BEGIN TRANSACTION;
CREATE TABLE test (id integer primary key, product_name text, price integer);
INSERT INTO "test" VALUES(1,'상품명1',10000);
INSERT INTO "test" VALUES(2,'상품명2',20000);
INSERT INTO "test" VALUES(3,'상품명3',30000);
CREATE TABLE test2 (id integer primary key, product_name text, price integer);
INSERT INTO "test2" VALUES(1,'모자',10000);
INSERT INTO "test2" VALUES(2,'가방',12000);
INSERT INTO "test2" VALUES(3,'가방',120001);
INSERT INTO "test2" VALUES(4,'가방',120002);
INSERT INTO "test2" VALUES(5,'가방',120003);
INSERT INTO "test2" VALUES(6,'바지',20000);
COMMIT;
