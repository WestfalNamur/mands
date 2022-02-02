package db

import (
	"context"
	"server/util"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestAddUser(t *testing.T) {
	ctx := context.Background()

	// Add
	arg := AddUserParams{
		UserName:     util.RandomString(12),
		UserPassword: util.RandomString(12),
	}
	user, err := testQueries.AddUser(ctx, arg)
	require.NoError(t, err)
	require.NotEmpty(t, user)

	// Delete
	err = testQueries.DeleteTodo(ctx, user.ID)
	require.NoError(t, err)
}
