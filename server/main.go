package main

import (
	"database/sql"
	"log"
	"server/api"
	db "server/db/sqlc"

	_ "github.com/lib/pq" // We do not use any of its function directly.
)

const (
	dbDriver      = "postgres"
	dbSource      = "postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"
	serverAddress = "0.0.0.0:8080"
)

func main() {
	conn, err := sql.Open(dbDriver, dbSource)
	if err != nil {
		log.Fatal("cannot connect to db:", err)
	}

	store := db.NewStore(conn)
	server := api.NewServer(store)

	err = server.Start(serverAddress)
	if err != nil {
		log.Fatal("cannot start server: ", err)
	}
}
