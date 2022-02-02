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
		UserName:     util.RandomString(10),
		UserPassword: util.RandomString(10),
	}
	user, err := testQueries.AddUser(ctx, arg)
	require.NoError(t, err)
	require.NotEmpty(t, user)
}
