import { useState } from "react";
import { Button, Divider, Input, List } from "antd";
import { NewTodo } from "./types";

export default function AddTodo() {
  const [text, setText] = useState("");

  function handleClick() {
    const newTodo: NewTodo = {
      user_id: 0,
      content_text: text,
      done: false,
    };
    console.log(newTodo);
    setText("");
  }

  const btn: JSX.Element =
    text == "" ? (
      <Button type="primary" onClick={handleClick} disabled={true}>
        Post Todo
      </Button>
    ) : (
      <Button type="primary" onClick={handleClick} disabled={false}>
        Post Todo
      </Button>
    );

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
      <div className="grid place-items-center">{btn}</div>
    </>
  );
}
