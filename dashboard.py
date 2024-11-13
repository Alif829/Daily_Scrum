import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Task Time Analysis Dashboard")
uploaded_file = st.file_uploader("Upload your Excel file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    df['Task ID'] = df['Task ID'].fillna(method='ffill')
    df['Name'] = df['Name'].fillna(method='ffill')

    task_summary = df.groupby(['Name', 'Task ID'])['Spent Time(Hr)'].sum().reset_index()

    task_summary_pivot = task_summary.pivot(index='Task ID', columns='Name', values='Spent Time(Hr)').fillna(0)
    st.subheader("Total Hours per Task ID by Each Individual")
    fig, ax = plt.subplots()
    task_summary_pivot.plot(kind='bar', stacked=True, ax=ax, figsize=(10, 6))
    plt.xlabel('Task ID')
    plt.ylabel('Total Hours Spent')
    plt.title('Total Hours Spent per Task ID by Each Individual')
    plt.xticks(rotation=45)
    st.pyplot(fig)
