-- name: AddUserData :one
INSERT INTO user_data (
    user_name,
    user_password
) VALUES (
    $1, $2
) RETURNING *;

-- name: GetAllUserData :many
SELECT * FROM user_data;

-- name: UpdateUserData :one
UPDATE user_data
SET user_name = $2,
    user_password = $3
WHERE id = $1 
RETURNING *;

-- name: DeleteUserData :exec
DELETE FROM user_data
WHERE id = $1;