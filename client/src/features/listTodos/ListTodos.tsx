import "antd/dist/antd.css";
import { isTodo, Todo } from "./types";
import ListTodosItem from "./ListTodosItem";
import AddTodo from "./ListTodoAdd";
import styles from "./ListTodos.module.css";
import { useQuery } from "react-query";

export default function Index() {
  const { isLoading, error, data } = useQuery<Todo[], Error>("todos", () =>
    fetch("http://localhost:8000/todos?limit=1000&offset=0").then((res) =>
      res.json()
    )
  );

  if (isLoading) return <p>...loading.</p>;
  if (error) return <p>{error}</p>;
  if (!data) return <p>no data ...</p>;

  const todos: Todo[] = data.filter((todo: Todo) => isTodo(todo));
  const items = todos.map((todo) => <ListTodosItem key={todo.id} {...todo} />);

  return (
    <>
      <div className={styles.list}>
        {items}
        <AddTodo />
      </div>
    </>
  );
}
