import {useState} from "react";
import {Divider, Input, List} from "antd";

export default function AddTodo() {
  const [text, setText] = useState("")

  return (
    <>
      <Divider>Add Todo</Divider>
      <List.Item>
        <Input
          size="large"
          placeholder="large size"
          value={text}
          onChange={e => setText(e.target.value)}
        />
      </List.Item>
    </>
  )
}

