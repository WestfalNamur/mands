-- name: AddTodo :one
INSERT INTO todo (
    user_id,
    content_text,
    done
) VALUES (
    $1, $2, $3
) RETURNING *;

-- name: GetAllTodo :many
SELECT * FROM todo;

-- name: GetTodo :one
SELECT * FROM todo
WHERE id = $1;

-- name: UpdateTodo :one
UPDATE todo
SET user_id = $2,
    content_text = $3,
    done = $4
WHERE id = $1 
RETURNING *;

-- name: DeleteTodo :exec
DELETE FROM todo
WHERE id = $1;