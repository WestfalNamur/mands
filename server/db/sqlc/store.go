package db

import (
	"database/sql"
)

// store: provides all functions to execute db queries and transactions.
// extends: Queries object that contains queries methodes.
type Store struct {
	*Queries // Composition to extend Queries struct functionality.
	db       *sql.DB
}

// Take a pointer to sql-db as input and creates and returns a pointer to a new store obj.
func NewStore(db *sql.DB) *Store {
	return &Store{
		db:      db,
		Queries: New(db), // New() created by sqlc
	}
}
