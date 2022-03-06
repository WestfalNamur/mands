import NavBar from "../features/layout/navBar";
import Index from "../features/listTodos/ListTodos";
import styles from "../features/listTodos/ListTodos.module.css"

export default function Todos() {
  return (
    <>
      <NavBar/>
      <div className={styles.main}>
        <Index/>
      </div>
    </>
  )
}