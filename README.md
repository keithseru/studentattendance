# Django Assessment: Student Attendance System

This project is a simple Django application designed to manage student attendance records. It demonstrates core Django concepts including virtual environments, project/app structure, models, views, templates, and CRUD operations.

---

## Project Requirements

### 1. Virtual Environment
- Set up a dedicated Python virtual environment for the project to manage dependencies cleanly.

### 2. Django Project & App
- Create a new Django project.
- Inside it, build a single Django application to handle attendance logic.

### 3. Data Model
Define a single model to represent a student attendance record with the following fields:

| Field       | Type         | Description                              |
|-------------|--------------|------------------------------------------|
| `name`      | CharField    | Student's full name                      |
| `student_id`| CharField    | Unique student ID                        |
| `is_present`| BooleanField | Attendance status for the day            |
| `date`      | DateField    | Date of the attendance record            |

---

## CRUD Functionality

### Create (Record Attendance)
- A form to add a new student attendance record.
- Collects name, student ID, and presence status.

### Read (View Records)
- **List View**: Homepage displaying all attendance records in a table.
- **Detail View**: Individual page showing full details of a single record.

### Update (Edit Record)
- A form pre-filled with existing data to modify a student’s attendance.

### Delete (Remove Record)
- A confirmation page or button to delete a specific record.

---

## URLs, Views & Templates

- Define distinct URLs for each CRUD operation:
  - `/` — List view
  - `/create/` — Add new record
  - `/view/<int:pk>/` — Detail view
  - `/update/<int:pk>/` — Edit record
  - `/delete/<int:pk>/` — Delete record

- Create corresponding Django views to handle logic and render templates.
- Build separate HTML templates for each page using Bootstrap for styling.

---

## Submission Instructions

1. **GitHub Repository**
   - Publish the complete Django project to a public GitHub repository.

2. **Submit Link**
   - Share the link to your GitHub repository as your final submission.

---

**Good luck, and happy coding!**
