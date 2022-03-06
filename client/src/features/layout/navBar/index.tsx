import NavBarTab from "./NavBarTab";

export default function NavBar() {
  return (
    <ul className="flex border-b">
      <NavBarTab href="/" text="Home"/>
      <NavBarTab href="/todos" text="Todos"/>
    </ul>
  );
}
