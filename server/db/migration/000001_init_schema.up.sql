CREATE TABLE "user_data" (
  "id" bigserial PRIMARY KEY,
  "user_name" varchar UNIQUE NOT NULL,
  "user_password" varchar UNIQUE NOT NULL
);

CREATE TABLE "todo" (
  "id" bigserial PRIMARY KEY,
  "user_id" bigserial NOT NULL,
  "content_text" TEXT NOT NULL,
  "done" boolean NOT NULL
);

ALTER TABLE "todo" ADD FOREIGN KEY ("user_id") REFERENCES "user_data" ("id");
