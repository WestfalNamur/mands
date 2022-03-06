import {Divider} from "antd";

export interface Props {
  done: boolean
  content_text: string
}

export default function ListTodosItem({done, content_text}: Props) {
  return (
    <>
      <Divider>{done ? "Done" : "Todo"}</Divider>
      <p>{content_text}</p>
    </>
  )
}