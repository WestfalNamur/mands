import {Avatar, Divider, List} from "antd";

export interface Props {
  done: boolean
  content_text: string
  user_id: number
}

export default function ListTodosItem({done, content_text}: Props) {
  return (
    <>
      <Divider/>
      <List.Item>
        <List.Item.Meta
          avatar={<Avatar src="https://joeschmoe.io/api/v1/random"/>}
          description={content_text}
        />
      </List.Item>
    </>
  )
}
