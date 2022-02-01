CREATE TABLE "user" (
  "id" bigserial PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "password" varchar UNIQUE NOT NULL
);

CREATE TABLE "todo" (
  "id" bigserial PRIMARY KEY,
  "user_id" bigserial,
  "name" varchar UNIQUE NOT NULL,
  "text" TEXT NOT NULL,
  "done" boolean NOT NULL
);

ALTER TABLE "todo" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");
