package api

import (
	"database/sql"
	"net/http"
	"net/http/httptest"
	"os"
	db "server/db/sqlc"
	"server/util"
	"testing"

	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/require"

	_ "github.com/lib/pq" // We do not use any of its function directly.
)

func newTestServer(t *testing.T) *Server {
	config, err := util.LoadConfig("../")
	require.NoError(t, err)

	conn, err := sql.Open(config.DBDriver, config.DBSource)
	require.NoError(t, err)

	store := db.NewStore(conn)
	server := NewServer(store)

	return server
}

func TestMain(m *testing.M) {
	gin.SetMode(gin.TestMode)

	os.Exit(m.Run())
}

func TestPing(t *testing.T) {
	server := newTestServer(t)

	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/ping", nil)
	server.router.ServeHTTP(w, req)

	require.Equal(t, 200, w.Code)
	require.Equal(t, "pong", w.Body.String())
}
