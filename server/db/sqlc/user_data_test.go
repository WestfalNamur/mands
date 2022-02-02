package db

import (
	"context"
	"server/util"
	"testing"

	"github.com/stretchr/testify/require"
)

// If we just use util.RandomString(12) Go will cache the result.
func createRandomName(t *testing.T) string {
	return util.RandomString(12)
}

func TestAddUser(t *testing.T) {
	ctx := context.Background()

	arg := AddUserDataParams{
		UserName:     createRandomName(t),
		UserPassword: createRandomName(t),
	}
	user, err := testQueries.AddUserData(ctx, arg)

	require.NoError(t, err)
	require.NotEmpty(t, user)
}

func TestDeleteUser(t *testing.T) {
	ctx := context.Background()

	// Add
	arg := AddUserDataParams{
		UserName:     createRandomName(t),
		UserPassword: createRandomName(t),
	}
	user, err := testQueries.AddUserData(ctx, arg)

	require.NoError(t, err)
	require.NotEmpty(t, user)

	// Delete
	err = testQueries.DeleteUserData(ctx, user.ID)

	require.NoError(t, err)
}

func TestAddAndDeleteMultipleUserData(t *testing.T) {
	ctx := context.Background()

	n := 7

	for i := 0; i < n; i++ {
		arg := AddUserDataParams{
			UserName:     createRandomName(t),
			UserPassword: createRandomName(t),
		}
		user, err := testQueries.AddUserData(ctx, arg)
		require.NoError(t, err)
		require.NotEmpty(t, user)
	}

}
