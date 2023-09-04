BEGIN TRANSACTION;
DROP TABLE IF EXISTS "dbskeleton";
CREATE TABLE IF NOT EXISTS "dbskeleton" (
	"id"	INTEGER NOT NULL,
	"string"	VARCHAR NOT NULL,
	"date"	DATE,
	"isodatetime"	DATETIME,
	"isodate"	DATE,
	"integer"	INTEGER,
	"float"	FLOAT NOT NULL,
	"decimal"	DECIMAL(5, 2) NOT NULL,
	"numeric"	NUMERIC(5, 2) NOT NULL,
	"active"	INTEGER NOT NULL,
	"tags"	VARCHAR,
	"gruppe"	VARCHAR,
	"data"	JSON,
	PRIMARY KEY("id"),
	UNIQUE("id")
);
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (1,'one',NULL,NULL,NULL,1,0.0,0,0,1,'A,K','A','null');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (2,'two',NULL,NULL,NULL,2,0.0,0,0,0,'B,M','B','null');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (3,'three',NULL,NULL,NULL,3,0.0,0,0,1,'M,K,one','C','null');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (4,'four',NULL,NULL,NULL,4,0.0,0,0,0,'L,A K','C','null');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (5,'five',NULL,NULL,NULL,5,0.0,0,0,1,'A,K','B','null');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (6,'six',NULL,NULL,NULL,5,0.0,0,0,1,'B K A','A','null');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (7,'seven','2020-08-19','2020-08-19 14:37:00.000000','2020-08-19',6,0.333333333333333,1.2345,5.6789,1,NULL,'D','"{\"A\": 1}"');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (8,'eight','2020-08-19','2020-08-19 14:37:00.000000','2020-08-19',6,0.333333333333333,12345.3456,5.6789,1,NULL,'C','"{\"A\": 2}"');
INSERT INTO "dbskeleton" ("id","string","date","isodatetime","isodate","integer","float","decimal","numeric","active","tags","gruppe","data") VALUES (9,'sechs','2020-08-19','2020-08-19 14:37:00.000000','2020-08-19',6,0.333333333333333,1.2345,5.6789,1,NULL,NULL,'{"A": 1}');
COMMIT;
