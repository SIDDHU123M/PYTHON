**GUI Programming**

1. **Creating a Simple GUI Application with Tkinter**
   - Use the `tkinter` library to create GUI applications.
   - Create a main application window using `tk.Tk()`.

2. **Adding Buttons and Handling Events**
   - Use `tk.Button()` to add buttons to the GUI.
   - Specify a function to be called when the button is clicked using the `command` parameter.

3. **Creating Forms with Entry Widgets**
   - Use `tk.Entry()` to create input fields.
   - Capture input data and process it.

4. **Designing Layouts with Grid and Pack**
   - Use the `grid()` and `pack()` methods to design layouts.
   - Arrange widgets using rows and columns with the grid layout.

**Notes and Tips:**
- GUI programming involves creating graphical interfaces for users.
- The `tkinter` library is commonly used for GUI development in Python.
- Widgets are elements like buttons, labels, input fields, etc.
- Handling events allows you to respond to user actions.
- Designing layouts involves arranging widgets visually.

**Instructions:**
- Learn about different GUI libraries available in Python (e.g., Tkinter, PyQt, wxPython).
- Understand the basic structure of GUI applications (main window, widgets, events).
- Explore widget documentation to understand available options.
- Design user-friendly interfaces with appropriate labels, buttons, and input fields.
- Handle events to make your GUI interactive.
- Experiment with different layout managers to arrange widgets.
- Practice creating various types of GUI applications.

---
**Code:**

```python
# Creating a Simple GUI Application with Tkinter
import tkinter as tk

root = tk.Tk()
root.title("Simple GUI Application")

label = tk.Label(root, text="Hello, GUI!")
label.pack()

root.mainloop()

# Adding Buttons and Handling Events
def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("GUI with Button")

label = tk.Label(root, text="Press the button:")
label.pack()

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()

# Creating Forms with Entry Widgets
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    result_label.config(text=f"Name: {name}, Age: {age}")

root = tk.Tk()
root.title("User Form")

entry_name = tk.Entry(root)
entry_name.pack()

entry_age = tk.Entry(root)
entry_age.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

# Designing Layouts with Grid and Pack
root = tk.Tk()
root.title("Layout Example")

label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1)

button1 = tk.Button(root, text="Button 1")
button1.pack(side=tk.LEFT)

button2 = tk.Button(root, text="Button 2")
button2.pack(side=tk.LEFT)

root.mainloop()
```

