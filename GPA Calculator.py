# GPA CALCULATOR WITH INTERFACE
import tkinter as tk

# Create a new window
window = tk.Tk()
window.title("GPA Calculator")
window.configure(bg="#FFB6C1")

# GPA Calculator Form
header_label = tk.Label(window, text="GPA Calculator", font=("Arial", 40, "bold"), fg="black", bg="#FFB6C1")
header_label.grid(row=0, column=2, columnspan=2, sticky="n")

# Course Details
course_label = tk.Label(window, text="Course Details", font=("Arial", 15, "bold"), fg="black", bg="#FFB6C1")
course_label.grid(row=2, column=0, columnspan=2)


# loop
def add_course_fields():
    global i, course_entries, credit_entries, grade_entries
    i += 1
    course_code_label = tk.Label(window, text="Course code " + str(i) + ": ", font=("Arial", 12, "bold"), fg="black", bg="#FFB6C1")
    course_code_label.grid(row=i + 2, column=0)
    course_code_entry = tk.Entry(window)
    course_code_entry.grid(row=i + 2, column=1)
    course_entries.append(course_code_entry)
    credit_label = tk.Label(window, text="Credit Hours for course " + str(i) + ": ", font=("Arial", 12, "bold"), fg="black", bg="#FFB6C1")
    credit_label.grid(row=i+2, column=2)
    credit_entry = tk.Entry(window)
    credit_entry.grid(row=i+2, column=3)
    credit_entries.append(credit_entry)
    grade_label = tk.Label(window, text="Grade for course " + str(i) + ": ", font=("Arial", 12, "bold"), fg="black", bg="#FFB6C1")
    grade_label.grid(row=i+2, column=4)
    grade_entry = tk.Entry(window)
    grade_entry.grid(row=i+2, column=5)
    grade_entries.append(grade_entry)


def remove_course_fields():
    global i, credit_entries, grade_entries, course_entries
    if i > 0:
        course_entries[-1].destroy()
        course_entries.pop()
        credit_entries[-1].destroy()
        credit_entries.pop()
        grade_entries[-1].destroy()
        grade_entries.pop()
        i -= 1


i = 0
course_entries = []
credit_entries = []
grade_entries = []
add_course_fields()

add_course_button = tk.Button(window, text="Add Course", command=add_course_fields, bg="#f5f5f5", font=("Arial", 10))
add_course_button.config(height=1, width=13)
add_course_button.grid(row=2, column=2)

remove_course_button = tk.Button(window, text="Remove Course", command=remove_course_fields, bg="#f5f5f5", font=("Arial", 10))
remove_course_button.config(height=1, width=13)
remove_course_button.grid(row=2, column=3)

# GPA Calculation
gpa_label = tk.Label(window, text="GPA Calculation", font=("Arial", 15, "bold"), fg="black", bg="#FFB6C1")
gpa_label.grid(row=i+18, column=2, columnspan=2)


output_label = tk.Label(window, text="Your GPA:", bg="#FFB6C1", fg="black")
output_label.grid(row=i+20, column=2, columnspan=2)


# Bind Events
def calculate_gpa():
    no_of_sub = i
    summ = 0
    sum_credit = 0
    for j in range(no_of_sub):
        credit_point = int(credit_entries[j].get())
        grade = grade_entries[j].get().upper()
        if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            grade = 5 - ord(grade) + ord('A')
        else:
            output_label.configure(text="Invalid grade(s) entered.")
            return
        total = grade * credit_point
        summ += total
        sum_credit += credit_point
    gpa = summ / sum_credit
    output_label.configure(text=f"Your GPA: {gpa:.2f}", bg="#FFB6C1", fg="black")


calculate_button = tk.Button(window, text="Calculate", command=calculate_gpa, bg="#f5f5f5", font=("Arial", 10))
calculate_button.config(height=1, width=13)
calculate_button.grid(row=i+19, column=2, columnspan=2)

# Run the Application
window.mainloop()
