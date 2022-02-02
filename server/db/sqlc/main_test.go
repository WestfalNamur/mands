package db

import (
	"database/sql"
	"log"
	"os"
	"testing"

	_ "github.com/lib/pq" // We do not use any of its function directly.
)

const (
	dbDriver = "postgres"
	dbSource = "postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"
)

// Used extensively thus defined as global
var testQueries *Queries
var testDB *sql.DB

// By convetion main entry point for all unit test within a specific Go package. Here for package db.
func TestMain(m *testing.M) {
	var err error
	// Create a connection to the db  // pass db driver and source string.
	testDB, err = sql.Open(dbDriver, dbSource)
	if err != nil {
		log.Fatal("Connot connect to db:", err)
	}
	// Use connection to create a new testQueirs object.
	// New() refers to "func New(db DBTX) *Queries" created by sqlc.
	testQueries = New(testDB)
	// Run unique test and report back to test-runner.
	os.Exit(m.Run())
}
