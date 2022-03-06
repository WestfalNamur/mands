import 'antd/dist/antd.css';
import {Divider} from "antd";
import useSWR from 'swr'
import {isTodo, Todo} from "./types"

const fetcher = async url => {
  const res = await fetch(url)

  // If the status code is not in the range 200-299, we still try to parse and throw it.
  if (!res.ok) {
    const error = new Error('An error occurred while fetching the data.')
    // Attach extra info to the error object.
    error.info = await res.json()
    error.status = res.status
    throw error
  }

  return res.json()
}


interface Props {
  done: boolean
  content_text: string
}


function TodoItem(props: Props) {
  const {done, content_text} = props
  return (
    <>
      <Divider>{done ? "Done" : "Todo"}</Divider>
      <p>{content_text}</p>
    </>
  )
}

export default function Index() {
  const {data, error} = useSWR('http://localhost:8000/todos/?limit=10&offset=0', fetcher)

  if (error) return <p>{error.status}</p>;
  if (!data) return <p>no data ...</p>;

  const todos: Todo[] = data.filter(todo => isTodo(todo))
  const items: JSX.Element[] = todos.map(todo => {
    return (
      <TodoItem
        key={todo.id}
        content_text={todo.content_text}
        done={todo.done}/>
    )
  })

  return (
    <>
      <div className={"w-1/3"}>
        {items}
      </div>
    </>
  )
}