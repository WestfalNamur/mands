package db

import (
	"database/sql"
	"log"
	"os"
	"testing"
	"server/util"

	_ "github.com/lib/pq" // We do not use any of its function directly.
)

// Used extensively thus defined as global
var testQueries *Queries
var testDB *sql.DB

// By convetion main entry point for all unit test within a specific Go package. Here for package db.
func TestMain(m *testing.M) {
	config, err := util.LoadConfig("../..")
	if err != nil {
		log.Fatal("cannot load config: ", err)
	}

	// Create a connection to the db  // pass db driver and source string.
	testDB, err = sql.Open(config.DBDriver, config.DBSource)
	if err != nil {
		log.Fatal("Connot connect to db:", err)
	}
	// Use connection to create a new testQueirs object.
	// New() refers to "func New(db DBTX) *Queries" created by sqlc.
	testQueries = New(testDB)
	// Run unique test and report back to test-runner.
	os.Exit(m.Run())
}
