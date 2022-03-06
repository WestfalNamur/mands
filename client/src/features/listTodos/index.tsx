import 'antd/dist/antd.css';
import useSWR from 'swr'
import {isTodo, Todo} from "./types"
import ListTodosItem from "./listTodosItem";
import styles from "./ListTodos.module.css"


const fetcher = async (url: string) => {
  const res = await fetch(url)
  return res.json()
}


export default function Index() {
  const {data, error} = useSWR('http://localhost:8000/todos/?limit=10&offset=0', fetcher)

  if (error) return <p>{error.status}</p>;
  if (!data) return <p>no data ...</p>;

  const todos: Todo[] = data.filter((todo: Todo) => isTodo(todo))
  const items: JSX.Element[] = todos.map(todo => {
    return (
      <ListTodosItem
        key={todo.id}
        content_text={todo.content_text}
        done={todo.done}/>
    )
  })

  return (
    <>
      <div className={styles.list}>
        {items}
      </div>
    </>
  )
}