import NavBar from "../features/layout/navBar";
import Index from "../features/listTodos";

export default function Todos() {
  return (
    <>
      <NavBar/>
      <div className={"grid place-items-center"}>
        <Index/>
      </div>
    </>
  )
}