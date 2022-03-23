import { useState } from "react";
import { Button, Divider, Input, List } from "antd";
import { NewTodo } from "./types";
import { useMutation } from "react-query";
import styles from "./ListTodos.module.css";
import { queryClient } from "../../pages/_app";

export default function AddTodo() {
  const [text, setText] = useState("");

  function postNewTodo(newTodo: NewTodo) {
    return fetch("http://localhost:8000/todos", {
      method: "POST",
      body: JSON.stringify(newTodo),
      headers: {
        "Content-type": "application/json",
      },
    });
  }

  const mutation = useMutation(postNewTodo, {
    onSuccess: (data, newTodo) => {
      queryClient.setQueriesData(["todo", newTodo], data);
    },
  });

  function handleClick() {
    const newTodo: NewTodo = {
      user_id: 1,
      content_text: text,
      done: false,
    };
    mutation.mutate(newTodo, {
      // If successfully we invalidate all queries cached under key 'todos'.
      onSuccess: () => {
        queryClient.invalidateQueries("todos");
      },
    });
    setText("");
  }

  return (
    <>
      <Divider>Add Todo</Divider>
      <List.Item>
        <Input
          size="large"
          placeholder="large size"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </List.Item>
      <div className={styles.postTodoButton}>
        <Button type="primary" onClick={handleClick} disabled={text == ""}>
          Post Todo
        </Button>
      </div>
    </>
  );
}
