package db

import (
	"context"
	"server/util"
	"testing"

	"github.com/stretchr/testify/require"
)

func createRandomUser(t *testing.T, ctx context.Context) (UserDatum, error) {
	arg := AddUserDataParams{
		UserName:     util.RandomString(12),
		UserPassword: util.RandomString(12),
	}
	user, err := testQueries.AddUserData(ctx, arg)

	require.NoError(t, err)
	require.NotEmpty(t, user)

	return user, err
}

func TestAddUser(t *testing.T) {
	ctx := context.Background()

	createRandomUser(t, ctx)
}

func TestDeleteUser(t *testing.T) {
	ctx := context.Background()

	user, _ := createRandomUser(t, ctx)

	err := testQueries.DeleteUserData(ctx, user.ID)
	require.NoError(t, err)
}

func TestAddAndDeleteMultipleUserData(t *testing.T) {
	ctx := context.Background()

	n := 5

	errs := make(chan error)
	users := make(chan UserDatum)

	// Create a few user
	for i := 0; i < n; i++ {
		go func() {
			user, err := createRandomUser(t, ctx)
			errs <- err
			users <- user
		}()
	}

	// Check errors
	for i := 0; i < n; i++ {
		err := <-errs
		require.NoError(t, err)
	}

	// Delete user data
	for i := 0; i < n; i++ {
		user := <-users
		err := testQueries.DeleteUserData(ctx, user.ID)
		require.NoError(t, err)
	}
}
