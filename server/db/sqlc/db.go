// Code generated by sqlc. DO NOT EDIT.

package db

import (
	"context"
	"database/sql"
	"fmt"
)

type DBTX interface {
	ExecContext(context.Context, string, ...interface{}) (sql.Result, error)
	PrepareContext(context.Context, string) (*sql.Stmt, error)
	QueryContext(context.Context, string, ...interface{}) (*sql.Rows, error)
	QueryRowContext(context.Context, string, ...interface{}) *sql.Row
}

func New(db DBTX) *Queries {
	return &Queries{db: db}
}

func Prepare(ctx context.Context, db DBTX) (*Queries, error) {
	q := Queries{db: db}
	var err error
	if q.addUserStmt, err = db.PrepareContext(ctx, addUser); err != nil {
		return nil, fmt.Errorf("error preparing query AddUser: %w", err)
	}
	if q.createTodoStmt, err = db.PrepareContext(ctx, createTodo); err != nil {
		return nil, fmt.Errorf("error preparing query CreateTodo: %w", err)
	}
	if q.deleteTodoStmt, err = db.PrepareContext(ctx, deleteTodo); err != nil {
		return nil, fmt.Errorf("error preparing query DeleteTodo: %w", err)
	}
	if q.deleteUserDataStmt, err = db.PrepareContext(ctx, deleteUserData); err != nil {
		return nil, fmt.Errorf("error preparing query DeleteUserData: %w", err)
	}
	if q.getAllTodoStmt, err = db.PrepareContext(ctx, getAllTodo); err != nil {
		return nil, fmt.Errorf("error preparing query GetAllTodo: %w", err)
	}
	if q.getAllUserDataStmt, err = db.PrepareContext(ctx, getAllUserData); err != nil {
		return nil, fmt.Errorf("error preparing query GetAllUserData: %w", err)
	}
	if q.updateTodoStmt, err = db.PrepareContext(ctx, updateTodo); err != nil {
		return nil, fmt.Errorf("error preparing query UpdateTodo: %w", err)
	}
	if q.updateUserDataStmt, err = db.PrepareContext(ctx, updateUserData); err != nil {
		return nil, fmt.Errorf("error preparing query UpdateUserData: %w", err)
	}
	return &q, nil
}

func (q *Queries) Close() error {
	var err error
	if q.addUserStmt != nil {
		if cerr := q.addUserStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing addUserStmt: %w", cerr)
		}
	}
	if q.createTodoStmt != nil {
		if cerr := q.createTodoStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing createTodoStmt: %w", cerr)
		}
	}
	if q.deleteTodoStmt != nil {
		if cerr := q.deleteTodoStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing deleteTodoStmt: %w", cerr)
		}
	}
	if q.deleteUserDataStmt != nil {
		if cerr := q.deleteUserDataStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing deleteUserDataStmt: %w", cerr)
		}
	}
	if q.getAllTodoStmt != nil {
		if cerr := q.getAllTodoStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing getAllTodoStmt: %w", cerr)
		}
	}
	if q.getAllUserDataStmt != nil {
		if cerr := q.getAllUserDataStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing getAllUserDataStmt: %w", cerr)
		}
	}
	if q.updateTodoStmt != nil {
		if cerr := q.updateTodoStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing updateTodoStmt: %w", cerr)
		}
	}
	if q.updateUserDataStmt != nil {
		if cerr := q.updateUserDataStmt.Close(); cerr != nil {
			err = fmt.Errorf("error closing updateUserDataStmt: %w", cerr)
		}
	}
	return err
}

func (q *Queries) exec(ctx context.Context, stmt *sql.Stmt, query string, args ...interface{}) (sql.Result, error) {
	switch {
	case stmt != nil && q.tx != nil:
		return q.tx.StmtContext(ctx, stmt).ExecContext(ctx, args...)
	case stmt != nil:
		return stmt.ExecContext(ctx, args...)
	default:
		return q.db.ExecContext(ctx, query, args...)
	}
}

func (q *Queries) query(ctx context.Context, stmt *sql.Stmt, query string, args ...interface{}) (*sql.Rows, error) {
	switch {
	case stmt != nil && q.tx != nil:
		return q.tx.StmtContext(ctx, stmt).QueryContext(ctx, args...)
	case stmt != nil:
		return stmt.QueryContext(ctx, args...)
	default:
		return q.db.QueryContext(ctx, query, args...)
	}
}

func (q *Queries) queryRow(ctx context.Context, stmt *sql.Stmt, query string, args ...interface{}) *sql.Row {
	switch {
	case stmt != nil && q.tx != nil:
		return q.tx.StmtContext(ctx, stmt).QueryRowContext(ctx, args...)
	case stmt != nil:
		return stmt.QueryRowContext(ctx, args...)
	default:
		return q.db.QueryRowContext(ctx, query, args...)
	}
}

type Queries struct {
	db                 DBTX
	tx                 *sql.Tx
	addUserStmt        *sql.Stmt
	createTodoStmt     *sql.Stmt
	deleteTodoStmt     *sql.Stmt
	deleteUserDataStmt *sql.Stmt
	getAllTodoStmt     *sql.Stmt
	getAllUserDataStmt *sql.Stmt
	updateTodoStmt     *sql.Stmt
	updateUserDataStmt *sql.Stmt
}

func (q *Queries) WithTx(tx *sql.Tx) *Queries {
	return &Queries{
		db:                 tx,
		tx:                 tx,
		addUserStmt:        q.addUserStmt,
		createTodoStmt:     q.createTodoStmt,
		deleteTodoStmt:     q.deleteTodoStmt,
		deleteUserDataStmt: q.deleteUserDataStmt,
		getAllTodoStmt:     q.getAllTodoStmt,
		getAllUserDataStmt: q.getAllUserDataStmt,
		updateTodoStmt:     q.updateTodoStmt,
		updateUserDataStmt: q.updateUserDataStmt,
	}
}