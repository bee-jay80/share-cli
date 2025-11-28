# ShareCLI – Secure Temporary Room-Based File Sharing (CLI + FastAPI)

ShareCLI is a lightweight, fast, and secure tool that allows users to create **temporary rooms** to share files or folders between team members.  
Rooms are protected with a password, automatically expire, and files are compressed for fast transfer.

This repository contains:

- **CLI application (Typer + Python)** — Used by users to create/join rooms.
- **Backend server (FastAPI + Redis)** — Manages temporary rooms and file storage.

---

## 🚀 Features

### ✔ Temporary room creation  
Users can create a room with:
- auto-generated room ID  
- password protection  
- automatic expiration

### ✔ Folder compression & fast transfer  
All folders/files are zipped before upload.  
Client extracts automatically when downloading.

### ✔ Secure password validation  
Backend stores only **hashed passwords** using bcrypt.

### ✔ Redis-backed temporary storage  
Rooms expire automatically using Redis TTL.

### ✔ Lightweight & fast  
No database migrations needed.  
Uses local file storage for uploaded ZIPs.

---

