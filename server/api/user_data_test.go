package api

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	db "server/db/sqlc"
	"server/util"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestPostUser(t *testing.T) {
	server := newTestServer(t)

	// Create struct and encode // https://gosamples.dev/struct-to-io-reader/
	// We create a struct called arg of type createUserRequest. Then we create
	// a buffer and write arg into it as JSON.
	arg := createUserRequest{
		UserName:     util.RandomString(10),
		UserPassword: util.RandomString(10),
	}
	var buf bytes.Buffer
	json.NewEncoder(&buf).Encode(arg)

	// Creat a ResponseRecorder that we write the response into. Then we create
	// a new request. Finally we server the request via ServeHTTP methode and
	// write the response into w.
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("POST", "/users", &buf)
	server.router.ServeHTTP(w, req)

	// Check status code and if we can unmarshal the response into a user struct.
	// Then we know that we have the right response type.
	require.Equal(t, 200, w.Code)
	var user db.UserDatum
	err := json.Unmarshal(w.Body.Bytes(), &user)
	require.NoError(t, err)
}
