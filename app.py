
#
#
# python3 -m venv  ~/Documents/repos/streamlit/streamlit-venv
#
# source ~/Documents/repos/streamlit/streamlit-venv/bin/activate
#
# pip install streamlit
# pip install pandas numpy seaborn matplotlib altair plotly
# pip install docx2txt
# pip install textract
#
# pip install PyPDF2 pdfplumber
#
# # To upgrade:
# pip3 install streamlit -U
#
# streamlit run app.py

# [browser]
# gatherUsageStats = false
#
# You can now view your Streamlit app in your browser.

# source /Users/avasb2/Documents/Staging/Projects/streamlit/repos/streamlit-venv/bin/activate

# streamlit run app.py

#
# Local
# URL: http://localhost:8501
# Network
# URL: http://192.168.1.162:8501
#
# For better performance, install the Watchdog module:

# $ xcode-select --install
# $ pip install watchdog

# Chapter 73 next

# Core Pkgs
import pandas as pd
import streamlit as st
import plotly.express as px

# DB fxns
from db_fxns import create_table, add_data, view_all_data, view_unique_tasks, get_task, \
	edit_task_data, delete_data



def main():
	st.title("ToDo App with Streamlit")


	menu = ["Create","Read","Update","Delete","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	create_table()
	if choice == "Create":
		st.subheader("Add Items")

		col1, col2 = st.columns(2)

		with col1:
			task = st.text_area("Task To Do")

		with col2:
			task_status = st.selectbox("Status",["ToDo","Doing","Done"])
			task_due_date = st.date_input("Due Date")

		if st.button("Add Task"):
			add_data(task, task_status, task_due_date)
			st.success("Successfully Added Data: {}".format(task))

	elif choice == "Read":
		st.subheader("View Items")
		result = view_all_data()
		st.write(result)
		df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
		with st.expander("View All Data"):
			st.dataframe(df)

		with st.expander("Task Status"):
			task_df = df['Status'].value_counts().to_frame()
			task_df = task_df.reset_index()
			st.dataframe(task_df)

			p1 = px.pie(task_df, names='index',values='Status')
			st.plotly_chart(p1)

	elif choice == "Update":
		st.subheader("Edit/Update Items")
		result = view_all_data()
		df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
		with st.expander("Current Data"):
			st.dataframe(df)

		# st.write(view_unique_tasks())
		list_of_task = [i[0] for i in view_unique_tasks()]
		# st.write(list_of_task)
		selected_task = st.selectbox("Task To Edit", list_of_task)

		selected_result = get_task(selected_task)
		st.write(selected_result)

		if selected_result:
			task = selected_result[0][0]
			task_status = selected_result[0][1]
			task_due_date = selected_result[0][2]

			# layout
			col1, col2 = st.columns(2)

			with col1:
				new_task = st.text_area("Task To Do", task)

			with col2:
				new_task_status = st.selectbox(task_status, ["ToDo", "Doing", "Done"])
				new_task_due_date = st.date_input(task_due_date)

			if st.button("Update Task"):
				edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
				st.success("Successfully Updated:: {} To ::{}".format(task,new_task))

		result2 = view_all_data()
		df2 = pd.DataFrame(result2, columns=['Task', 'Status', 'Due Date'])
		with st.expander("Updated Data"):
			st.dataframe(df2)

	elif choice == "Delete":
		st.subheader("Delete Item")
		result = view_all_data()
		df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
		with st.expander("Current Data"):
			st.dataframe(df)

		list_of_task = [i[0] for i in view_unique_tasks()]
		selected_task = st.selectbox("Task To Delete", list_of_task)
		st.warning("Do You Want to Delete {} task?".format(selected_task))
		if st.button("Delete Task"):
			delete_data(selected_task)
			st.success("Task has been Successfully Deleted")

		result2 = view_all_data()
		df2 = pd.DataFrame(result2, columns=['Task', 'Status', 'Due Date'])
		with st.expander("Updated Data"):
			st.dataframe(df2)

	else:
		st.subheader("About")


if __name__ == '__main__':
	main()

