import {useState} from "react";
import {Divider} from "antd";

export default function AddTodo() {
  const [text, setText] = useState("")

  return (<>
    <Divider>Add Todo</Divider>
    <input value={text} onChange={e => setText(e.target.value)}/>
  </>)
}

