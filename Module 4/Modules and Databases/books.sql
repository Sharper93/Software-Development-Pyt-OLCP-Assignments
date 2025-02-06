BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "books" (
	"title"	TEXT,
	"author"	TEXT,
	"year"	INTEGER
);
INSERT INTO "books" VALUES ('The Weirdstone of Brisingamen','Alan Garner',1960);
INSERT INTO "books" VALUES ('Perdido Street Station','China Miéville',2000);
INSERT INTO "books" VALUES ('Thud!','Terry Pratchett',2005);
INSERT INTO "books" VALUES ('The Spellman Files','Lisa Lutz',2007);
INSERT INTO "books" VALUES ('Small Gods','Terry Pratchett',1992);
CREATE VIEW "books-data" AS SELECT * FROM "main"."books";
CREATE VIEW "books-view" AS SELECT * FROM books
order by title;
COMMIT;
