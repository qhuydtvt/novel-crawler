BEGIN TRANSACTION;
CREATE TABLE "tbl_word" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`origin`	TEXT NOT NULL,
	`explanation`	TEXT NOT NULL,
	`type`	TEXT NOT NULL,
	`pronunciation`	TEXT,
	`image_url`	TEXT NOT NULL,
	`example`	TEXT NOT NULL,
	`example_translation`	TEXT,
	`topic_id`	INTEGER NOT NULL,
	FOREIGN KEY(`topic_id`) REFERENCES `tbl_topic`(`id`)
);
CREATE TABLE "tbl_topic" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`no`	INTEGER NOT NULL,
	`image_url`	TEXT NOT NULL
);
COMMIT;
