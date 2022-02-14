package api

import (
	"net/http"
	db "server/db/sqlc"

	"github.com/gin-gonic/gin"
)

type Server struct {
	store  *db.Store
	router *gin.Engine
}

func NewServer(store *db.Store) *Server {
	server := &Server{store: store}
	router := gin.Default()

	// Ping test
	router.GET("/ping", func(c *gin.Context) {
		c.String(http.StatusOK, "pong")
	})

	server.router = router
	return server
}

// Start server. server.router.Run is private, thats why we wrap it.
func (server *Server) Start(address string) error {
	return server.router.Run(address)
}

// Often used error response
func errorResponse(err error) gin.H {
	return gin.H{"error": err.Error()}
}
