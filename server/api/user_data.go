package api

import (
	"net/http"
	db "server/db/sqlc"

	"github.com/gin-gonic/gin"
)

// Will be validated by Gin internally via validator
type createUserRequest struct {
	UserName     string `json:"user_name" binding:"required"`
	UserPassword string `json:"user_password" binding:"required"`
}

func (server *Server) createUser(ctx *gin.Context) {
	var req createUserRequest
	if err := ctx.ShouldBindJSON(&req); err != nil {
		ctx.JSON(http.StatusBadRequest, errorResponse(err))
		return
	}

	arg := db.AddUserDataParams{
		UserName:     req.UserName,
		UserPassword: req.UserPassword,
	}

	user, err := server.store.AddUserData(ctx, arg)
	if err != nil {
		ctx.JSON(http.StatusInternalServerError, errorResponse(err))
		return
	}

	ctx.JSON(http.StatusOK, user)
}
