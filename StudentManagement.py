import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Manager",
    layout="centered",
)

st.title("Student Management System")
st.caption("Simple Streamlit app using session_state")

# Initialize storage
if "students" not in st.session_state:
    st.session_state.students = []

st.divider()

# -------------------------
# 1. Add Student (FORM)
# -------------------------
st.subheader("1. Add Student")

with st.form("add_student_form", clear_on_submit=True):
    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    dept = st.text_input("Department (e.g., CSE)")
    submitted = st.form_submit_button("Add Student")

    if submitted:
        if name and roll and dept:
            st.session_state.students.append(
                {"Name": name, "Roll": roll, "Department": dept}
            )
            st.success("Student added successfully")
        else:
            st.warning("Please fill all fields")

st.divider()

# -------------------------
# 2. View Students
# -------------------------
st.subheader("2. Student List")

if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No students yet. Add one above.")

st.divider()

# -------------------------
# 3. Delete Student
# -------------------------
st.subheader("3. Delete Student")

if st.session_state.students:
    rolls = [s["Roll"] for s in st.session_state.students]
    roll_to_delete = st.selectbox("Select roll to delete", rolls)

    if st.button("Delete Student"):
        st.session_state.students = [
            s for s in st.session_state.students if s["Roll"] != roll_to_delete
        ]
        st.success(f"Student with roll {roll_to_delete} deleted")
else:
    st.caption("Add students before trying to delete.")
