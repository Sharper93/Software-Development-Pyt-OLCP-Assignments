BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "books" (
	"title"	TEXT,
	"author"	TEXT,
	"year"	INTEGER
);
INSERT INTO "books" ("title","author","year") VALUES ('The Weirdstone of Brisingamen','Alan Garner',1960),
 ('Perdido Street Station','China Miéville',2000),
 ('Thud!','Terry Pratchett',2005),
 ('The Spellman Files','Lisa Lutz',2007),
 ('Small Gods','Terry Pratchett',1992);
CREATE VIEW "books-data" AS SELECT * FROM "main"."books";
CREATE VIEW "books-view" AS SELECT * FROM books
order by title;
COMMIT;
