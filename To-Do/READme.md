# 📝 To-Do CLI App in Python

A simple, lightweight command-line To-Do List application built with Python. This app lets you manage your daily tasks right from the terminal. You can add tasks, view them, mark them as done, and delete them — all stored locally in a JSON file.

## 🚀 Features

- ✅ Add new tasks to your to-do list  
- 📋 View all your tasks with status (Pending/Done)  
- ✔️ Mark tasks as completed  
- 🗑️ Delete tasks from the list  
- 💾 Persistent data storage using JSON  

## 🛠️ Installation

1. **Clone the repository or download the `todo.py` file**
   ```bash
   git clone https://github.com/yourusername/todo-cli-app.git
   cd todo-cli-app
   ```
## ✅ Ensure Python is installed (Python 3.6 or above)  
```bash  
python --version  
```

## ▶️ Run the application  
```bash
python todo.py
```

## 🧠 How It Works  
Tasks are stored as dictionaries in a list (e.g., `{"task": "Buy groceries", "done": false}`). This list is saved to a file named `todos.json`. Every action (add, delete, update) updates this file in real time.

## 🎮 Usage  
On running the script, you will be presented with the following menu:  
```pgsql
To-Do CLI App  
1. View To-Dos  
2. Add To-Do  
3. Mark To-Do as Done  
4. Delete To-Do  
5. Exit  
```
## ➕ Add a Task 
Select option 2  
Enter your task description  

## 👀 View Tasks  
Select option 1 to see all your tasks and their statuses  

## ✅ Mark as Done  
Select option 3  
Enter the task number you want to mark as done  

## ❌ Delete a Task  
Select option 4  
Enter the task number you want to remove  

## 🔚 Exit  
Select option 5 to quit the app  

## 🧩 Future Enhancements  
⏰ Add task deadlines  
📅 Sort tasks by due date or priority  
✏️ Edit existing tasks  
📌 Tagging system for better organization  

## 📜 License  
This project is open-source and free to use under the MIT License.  
👨‍💻 Developed with ❤️ in Python  
