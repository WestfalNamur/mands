export interface Todo {
  id: number
  user_id: number
  content_text: string
  done: boolean
}

export function isTodo(todo: Todo): boolean {
  if (typeof todo.id !== "number") {
    return false
  }
  if (typeof todo.user_id !== "number") {
    return false
  }
  if (typeof todo.content_text !== "string") {
    return false
  }
  if (typeof todo.done !== "boolean") {
    return false
  }
  return true
}
