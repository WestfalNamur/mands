package db

import (
	"context"
	"server/util"
	"testing"

	"github.com/stretchr/testify/require"
)

func createRandomTodo(t *testing.T, ctx context.Context, user UserDatum) (Todo, error) {
	arg := AddTodoParams{
		UserID:      user.ID,
		ContentText: util.RandomText(8),
		Done:        false,
	}

	todo, err := testQueries.AddTodo(ctx, arg)

	require.NoError(t, err)
	require.NotEmpty(t, todo)

	return todo, err
}

func TestAddTodo(t *testing.T) {
	ctx := context.Background()

	user, _ := createRandomUser(t, ctx)
	createRandomTodo(t, ctx, user)
}

func TestDeleteTodo(t *testing.T) {
	ctx := context.Background()

	user, _ := createRandomUser(t, ctx)
	todo, _ := createRandomTodo(t, ctx, user)

	err := testQueries.DeleteTodo(ctx, todo.ID)
	require.NoError(t, err)

	err = testQueries.DeleteUserData(ctx, user.ID)
	require.NoError(t, err)
}

func TestUpdateTodo(t *testing.T) {
	ctx := context.Background()

	// Create
	user, _ := createRandomUser(t, ctx)
	todo, _ := createRandomTodo(t, ctx, user) // Created Todos "Done" is false
	require.Equal(t, todo.Done, false)

	// Update
	arg := UpdateTodoParams{
		ID:          todo.ID,
		UserID:      todo.UserID,
		ContentText: todo.ContentText,
		Done:        true,
	}
	_, err := testQueries.UpdateTodo(ctx, arg)
	require.NoError(t, err)

	// Check
	todo, err = testQueries.GetTodo(ctx, todo.ID)
	require.NoError(t, err)
	require.Equal(t, todo.Done, true)

	// Delete
	err = testQueries.DeleteTodo(ctx, todo.ID)
	require.NoError(t, err)
	err = testQueries.DeleteUserData(ctx, user.ID)
	require.NoError(t, err)
}

func TestRmUsrFailsWhenUsrHasTodo(t *testing.T) {
	ctx := context.Background()

	user, _ := createRandomUser(t, ctx)
	todo, _ := createRandomTodo(t, ctx, user)

	// Removing user when they still have a Todo depending on it should fail.
	err := testQueries.DeleteUserData(ctx, user.ID)
	require.Error(t, err)
	err = testQueries.DeleteTodo(ctx, todo.ID)
	require.NoError(t, err)
	err = testQueries.DeleteUserData(ctx, user.ID)
	require.NoError(t, err)
}

func TestMultipleTodos(t *testing.T) {
	ctx := context.Background()

	n := 5

	errs := make(chan error)
	todos := make(chan Todo)

	// Create
	user, _ := createRandomUser(t, ctx)
	for i := 0; i < n; i++ {
		go func() {
			todo, err := createRandomTodo(t, ctx, user)
			errs <- err
			todos <- todo
		}()
	}

	// Check
	for i := 0; i < n; i++ {
		err := <-errs
		require.NoError(t, err)
	}

	// Delete
	for i := 0; i < n; i++ {
		todo := <-todos
		err := testQueries.DeleteTodo(ctx, todo.ID)
		require.NoError(t, err)
	}
}
