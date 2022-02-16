package api

import (
	"database/sql"
	"log"
	"net/http"
	"net/http/httptest"
	db "server/db/sqlc"
	"server/util"
	"testing"

	"github.com/stretchr/testify/require"

	_ "github.com/lib/pq" // We do not use any of its function directly.
)

func TestServer(t *testing.T) {
	config, err := util.LoadConfig("../")
	if err != nil {
		log.Fatal("cannot load config: ", err)
	}

	conn, err := sql.Open(config.DBDriver, config.DBSource)
	if err != nil {
		log.Fatal("cannot connect to db:", err)
	}

	testStore := db.NewStore(conn)
	testServer := NewServer(testStore)

	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/ping", nil)
	testServer.router.ServeHTTP(w, req)

	require.Equal(t, 200, w.Code)
	require.Equal(t, "pong", w.Body.String())
}
