from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import markdown

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str
    tags: list[str]

def get_db():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/notes")
def create_note(note: Note):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)",
                (note.title, note.content, ",".join(note.tags)))
    conn.commit()
    conn.close()
    return {"status": "created"}

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT title, content, tags FROM notes WHERE id=?", (note_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return {"error": "not found"}
    html = markdown.markdown(row["content"])
    return {"title": row["title"], "html": html, "tags": row["tags"].split(",")}

@app.get("/search/{tag}")
def search_by_tag(tag: str):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM notes WHERE tags LIKE ?", (f"%{tag}%",))
    rows = cur.fetchall()
    conn.close()
    return [{"id": r["id"], "title": r["title"]} for r in rows]

