package api

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	db "server/db/sqlc"
	"server/util"
	"strconv"
	"testing"

	"github.com/stretchr/testify/require"
)

func postUser(t *testing.T, server *Server) db.UserDatum {
	// Create struct and encode // https://gosamples.dev/struct-to-io-reader/
	// We create a struct called arg of type createUserRequest. Then we create
	// a buffer and write arg into it as JSON.
	arg := createUserRequest{
		UserName:     util.RandomString(10),
		UserPassword: util.RandomString(10),
	}
	var buf bytes.Buffer
	err := json.NewEncoder(&buf).Encode(arg)
	require.NoError(t, err)

	// Creat a ResponseRecorder that we write the response into. Then we create
	// a new request. Finally we server the request via ServeHTTP methode and
	// write the response into w.
	w := httptest.NewRecorder()
	req, err := http.NewRequest("POST", "/users", &buf)
	require.NoError(t, err)
	server.router.ServeHTTP(w, req)

	// Check status code and if we can unmarshal the response into a user struct.
	// Then we know that we have the right response type.
	require.Equal(t, 200, w.Code)
	var user db.UserDatum
	err = json.Unmarshal(w.Body.Bytes(), &user)
	require.NoError(t, err)
	require.Equal(t, arg.UserName, user.UserName)
	require.Equal(t, arg.UserPassword, user.UserPassword)
	require.NotEmpty(t, user.ID)

	return user
}

func getUser(t *testing.T, server *Server, user db.UserDatum) error {
	w := httptest.NewRecorder()
	s := "/users/" + strconv.Itoa(int(user.ID))
	req, err := http.NewRequest("GET", s, nil)
	if err != nil {
		return err
	}
	require.NoError(t, err)
	server.router.ServeHTTP(w, req)

	require.Equal(t, 200, w.Code)
	var userRes db.UserDatum
	err = json.Unmarshal(w.Body.Bytes(), &userRes)
	if err != nil {
		return err
	}
	require.NoError(t, err)
	require.Equal(t, user.UserName, userRes.UserName)
	require.Equal(t, user.UserPassword, userRes.UserPassword)
	require.Equal(t, user.UserPassword, userRes.UserPassword)

	return nil
}

func deleteUser(t *testing.T, server *Server, user db.UserDatum, shouldFail bool) {
	w := httptest.NewRecorder()
	s := "/users/" + strconv.Itoa(int(user.ID))
	req, err := http.NewRequest("DELETE", s, nil)
	server.router.ServeHTTP(w, req)
	require.NoError(t, err)
	if shouldFail == true {
		require.Equal(t, 404, w.Code)
	} else {
		require.Equal(t, 200, w.Code)
	}
}

func TestPostUser(t *testing.T) {
	server := newTestServer(t)
	postUser(t, server)
}

func TestGetUser(t *testing.T) {
	server := newTestServer(t)
	user := postUser(t, server)
	err := getUser(t, server, user)
	require.NoError(t, err)
}

func TestDeleteUser(t *testing.T) {
	server := newTestServer(t)
	user := postUser(t, server)
	getUser(t, server, user)
	deleteUser(t, server, user, false)
	deleteUser(t, server, user, true)
}
