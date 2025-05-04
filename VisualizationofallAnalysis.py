
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency
import scipy.stats as stats




def plot_attrition_rate(employee_data):
    plt.figure(figsize=(17,6))
    
    # Count attrition values
    attrition_rate = employee_data["Attrition"].value_counts()

    # Plotting the bar chart
    plt.subplot(1, 2, 1)
    sns.barplot(x=attrition_rate.index, y=attrition_rate.values, palette=["#1d7874", "#8B0000"])
    plt.title("Employee Attrition Counts", fontweight="black", size=20, pad=20)
    for i, v in enumerate(attrition_rate.values):
        plt.text(i, v, v, ha="center", fontweight='black', fontsize=18)

    # Plotting the pie chart
    plt.subplot(1, 2, 2)
    
    # Ensure the labels match the values of attrition_rate
    labels = attrition_rate.index.tolist()
    colors = ["#1d7874", "#AC1F29"][:len(labels)]  # Adjust colors to match the labels
    
    # Handle cases where attrition_rate might only contain one value (e.g., "No" or "Yes")
    if len(labels) == 1:
        labels.append("Other")  # If only one value exists, add a placeholder
    
    plt.pie(attrition_rate, labels=labels, autopct="%.2f%%", textprops={"fontweight": "black", "size": 15},
            colors=colors, explode=[0, 0.1] * (len(labels) // 2), startangle=90)

    # Add center circle for the donut chart effect
    center_circle = plt.Circle((0, 0), 0.3, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    plt.title("Employee Attrition Rate", fontweight="black", size=20, pad=10)
    st.pyplot(fig)











def plot_attrition_by_gender(employee_data):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    gender_attrition = employee_data["Gender"].value_counts()
    plt.title("Employees Distribution by Gender", fontweight="black", size=20)
    plt.pie(gender_attrition, autopct="%.0f%%", labels=gender_attrition.index, textprops={"fontweight": "black", "size": 20},
            explode=[0, 0.1], startangle=90, colors=["#ffb563", "#FFC0CB"])

    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_1 = employee_data["Gender"].value_counts()
    value_2 = new_df["Gender"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, palette=["#D4A1E7", "#E7A1A1"])
    plt.title("Employee Attrition Rate by Gender", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, str(value) + " (" + str(int(attrition_rate[index])) + "% )", ha="center", va="bottom",
                 size=15, fontweight="black")
    st.pyplot(plt.gcf())


def plot_attrition_by_age(employee_data):
    plt.figure(figsize=(13.5, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(x="Age", hue="Attrition", data=employee_data, kde=True, palette=["#11264e", "#6faea4"])
    plt.title("Employee Distribution by Age", fontweight="black", size=20, pad=10)

    plt.subplot(1, 2, 2)
    sns.boxplot(x="Attrition", y="Age", data=employee_data, palette=["#D4A1E7", "#6faea4"])
    plt.title("Employee Distribution by Age & Attrition", fontweight="black", size=20, pad=10)
    st.pyplot(plt.gcf())


def plot_attrition_by_business_travel(employee_data):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    value_1 = employee_data["BusinessTravel"].value_counts()
    plt.title("Employees by Business Travel", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#E84040', '#E96060', '#E88181'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["BusinessTravel"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B"])
    plt.title("Attrition Rate by Business Travel", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, str(value) + " (" + str(int(attrition_rate[index])) + "% )", ha="center", va="bottom",
                 size=15, fontweight="black")
    st.pyplot(plt.gcf())


def plot_attrition_by_department(employee_data):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    value_1 = employee_data["Department"].value_counts()
    sns.barplot(x=value_1.index, y=value_1.values, palette=["#FFA07A", "#D4A1E7", "#FFC0CB"])
    plt.title("Employees by Department", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_1.values):
        plt.text(index, value, value, ha="center", va="bottom", fontweight="black", size=15)

    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["Department"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B"])
    plt.title("Attrition Rate by Department", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, str(value) + " (" + str(attrition_rate[index]) + "% )", ha="center", va="bottom",
                 size=15, fontweight="black")
    st.pyplot(plt.gcf())



def plot_attrition_by_daily_rate(employee_data):
    # Define the bin edges for the groups
    bin_edges = [0, 500, 1000, 1500]
    bin_labels = ['Low DailyRate', 'Average DailyRate', 'High DailyRate']
    
    # Cut the DailyRate column into groups
    employee_data['DailyRateGroup'] = pd.cut(employee_data['DailyRate'], bins=bin_edges, labels=bin_labels)

    plt.figure(figsize=(14, 6))
    
    # Total employees by DailyRateGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["DailyRateGroup"].value_counts()
    plt.pie(value_1.values, labels=value_1.index, autopct="%.2f%%", textprops={"fontweight":"black","size":15},
            explode=[0, 0.1, 0.1], colors=['#FF8000', '#FF9933', '#FFB366'])
    plt.title("Employees by DailyRateGroup", fontweight="black", pad=15, size=18)
    
    # Attrition rate by DailyRateGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["DailyRateGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B"])
    plt.title("Employee Attrition Rate by DailyRateGroup", fontweight="black", pad=15, size=18)
    for index, value in enumerate(value_2.values):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", fontweight="black", size=15)
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_distance_from_home(employee_data):
    # Define the bin edges for the groups
    bin_edges = [0, 2, 5, 10, 30]
    bin_labels = ['0-2 kms', '3-5 kms', '6-10 kms', '10+ kms']
    
    # Cutting the DistanceFromHome column into groups
    employee_data['DistanceGroup'] = pd.cut(employee_data['DistanceFromHome'], bins=bin_edges, labels=bin_labels)
    
    plt.figure(figsize=(14, 6))
    
    # Total employees by DistanceGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["DistanceGroup"].value_counts()
    sns.barplot(x=value_1.index.tolist(), y=value_1.values, palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"])
    plt.title("Employees by Distance From Home", fontweight="black", pad=15, size=18)
    for index, value in enumerate(value_1.values):
        plt.text(index, value, value, ha="center", va="bottom", fontweight="black", size=15)
    
    # Attrition rate by DistanceGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["DistanceGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7"])
    plt.title("Attrition Rate by Distance From Home", fontweight="black", pad=15, size=18)
    for index, value in enumerate(value_2.values):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", fontweight="black", size=15)
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_education(employee_data):
    plt.figure(figsize=(13.5, 6))
    
    # Total employees by Education
    plt.subplot(1, 2, 1)
    value_1 = employee_data["Education"].value_counts()
    sns.barplot(x=value_1.index, y=value_1.values, order=value_1.index, palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"])
    plt.title("Employees Distribution by Education", fontweight="black", size=20, pad=15)
    for index, value in enumerate(value_1.values):
        plt.text(index, value, value, ha="center", va="bottom", fontweight="black", size=15)
    
    # Attrition rate by Education
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["Education"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7"])
    plt.title("Employee Attrition by Education", fontweight="black", size=18, pad=15)
    for index, value in enumerate(value_2.values):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", fontweight="black", size=13)
    
    plt.tight_layout()
    st.pyplot(plt.gcf())




def plot_attrition_by_education_field(employee_data):
    plt.figure(figsize=(13.5, 8))
    
    # Filter data to focus on employees with attrition (Attrition == 'Yes')
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    
    # Total employees by Education Field
    plt.subplot(1, 2, 1)
    value_1 = employee_data["EducationField"].value_counts()
    sns.barplot(x=value_1.index, y=value_1.values, order=value_1.index, palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"])
    plt.title("Employees by Education Field", fontweight="black", size=20, pad=15)
    for index, value in enumerate(value_1.values):
        plt.text(index, value, value, ha="center", va="bottom", fontweight="black", size=15)
    plt.xticks(rotation=90)
    
    # Attrition rate by Education Field
    plt.subplot(1, 2, 2)
    value_2 = new_df["EducationField"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7"])
    plt.title("Employee Attrition by Education Field", fontweight="black", size=18, pad=15)
    for index, value in enumerate(value_2.values):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", fontweight="black", size=13)
    plt.xticks(rotation=90)
    
    plt.tight_layout()
    st.pyplot(plt.gcf())





def plot_attrition_by_environment_satisfaction(employee_data):
    plt.figure(figsize=(14, 6))
    
    # Total Employees by Environment Satisfaction
    plt.subplot(1, 2, 1)
    value_1 = employee_data["EnvironmentSatisfaction"].value_counts()
    plt.title("Employees by Environment Satisfaction", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#E84040', '#E96060', '#E88181'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by Environment Satisfaction
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["EnvironmentSatisfaction"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Environment Satisfaction", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())




def plot_attrition_by_job_roles(employee_data):
    plt.figure(figsize=(13, 8))
    
    # Total Employees by Job Role
    plt.subplot(1, 2, 1)
    value_1 = employee_data["JobRole"].value_counts()
    sns.barplot(x=value_1.index.tolist(), y=value_1.values, palette=["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA"])
    plt.title("Employees by Job Role", fontweight="black", pad=15, size=18)
    plt.xticks(rotation=90)
    for index, value in enumerate(value_1.values):
        plt.text(index, value, value, ha="center", va="bottom", fontweight="black", size=15)
    
    # Attrition Rate by Job Role
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["JobRole"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Employee Attrition Rate by Job Role", fontweight="black", pad=15, size=18)
    plt.xticks(rotation=90)
    for index, value in enumerate(value_2.values):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", fontweight="black", size=10)
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_job_level(employee_data):
    plt.figure(figsize=(14, 6))
    
    # Total Employees by Job Level
    plt.subplot(1, 2, 1)
    value_1 = employee_data["JobLevel"].value_counts()
    plt.title("Employees by Job Level", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=['#FF6D8C', '#FF8C94', '#FFAC9B', '#FFCBA4', "#FFD8B1"], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
  
    # Attrition Rate by Job Level
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["JobLevel"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Job Level", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_job_satisfaction(employee_data):
    plt.figure(figsize=(14, 6))
    
    # Total Employees by Job Satisfaction
    plt.subplot(1, 2, 1)
    value_1 = employee_data["JobSatisfaction"].value_counts()
    plt.title("Employees by Job Satisfaction", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=['#FFB300', '#FFC300', '#FFD700', '#FFFF00'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
   
    # Attrition Rate by Job Satisfaction
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["JobSatisfaction"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Job Satisfaction", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())


def plot_attrition_by_marital_status(employee_data):
    plt.figure(figsize=(14, 6))
    
    # Total Employees by Marital Status
    plt.subplot(1, 2, 1)
    value_1 = employee_data["MaritalStatus"].value_counts()
    plt.title("Employees by Marital Status", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#E84040', '#E96060', '#E88181', '#E7A1A1'],
            textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by Marital Status
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["MaritalStatus"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index,
                palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Marital Status", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom",
                 size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())





def plot_attrition_by_monthly_income(employee_data):
    plt.figure(figsize=(13, 6))
    
    # Employee Distribution by Monthly Income
    plt.subplot(1, 2, 1)
    sns.histplot(x="MonthlyIncome", hue="Attrition", kde=True, data=employee_data, palette=["#11264e", "#6faea4"])
    plt.title("Employee Attrition by Monthly Income", fontweight="black", size=20, pad=15)
    
    # Employee Attrition by Monthly Income
    plt.subplot(1, 2, 2)
    sns.boxplot(x="Attrition", y="MonthlyIncome", data=employee_data, palette=["#D4A1E7", "#6faea4"])
    plt.title("Employee Attrition by Monthly Income", fontweight="black", size=20, pad=15)
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_work_experience(employee_data):
    # Bin the Number of Companies Worked
    bin_edges = [0, 1, 3, 5, 10]
    bin_labels = ['0-1 Companies', '2-3 companies', '4-5 companies', "5+ companies"]
    employee_data["NumCompaniesWorkedGroup"] = pd.cut(employee_data['NumCompaniesWorked'], bins=bin_edges, labels=bin_labels)
    
    plt.figure(figsize=(13, 6))
    
    # Total Employees by Companies Worked
    plt.subplot(1, 2, 1)
    value_1 = employee_data["NumCompaniesWorkedGroup"].value_counts()
    plt.title("Employees by Companies Worked", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=['#FF6D8C', '#FF8C94', '#FFAC9B', '#FFCBA4'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by Companies Worked
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["NumCompaniesWorkedGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Companies Worked", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({attrition_rate[index]}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())


def plot_attrition_by_overtime(employee_data):
    plt.figure(figsize=(15, 6))
    
    # Total Employees by Overtime
    plt.subplot(1, 2, 1)
    value_1 = employee_data["OverTime"].value_counts()
    plt.title("Employees by Overtime", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=["#ffb563", "#FFC0CB"], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by Overtime
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["OverTime"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Overtime", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())




def plot_attrition_by_salary_hike(employee_data):
    plt.figure(figsize=(16, 6))
    sns.countplot(x="PercentSalaryHike", hue="Attrition", data=employee_data, palette=["#1d7874", "#AC1F29"])
    plt.title("Employee Attrition By Percent Salary Hike", fontweight="black", size=20, pad=15)
    st.pyplot(plt.gcf())


def plot_attrition_by_performance_rating(employee_data):
    plt.figure(figsize=(14, 6))
    
    # Total Employees by Performance Rating
    plt.subplot(1, 2, 1)
    value_1 = employee_data["PerformanceRating"].value_counts()
    plt.title("Employees by Performance Rating", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=["#ffb563", "#FFC0CB"], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by Performance Rating
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["PerformanceRating"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Performance Rating", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_relationship_satisfaction(employee_data):
    plt.figure(figsize=(13, 6))
    
    # Total Employees by Relationship Satisfaction
    plt.subplot(1, 2, 1)
    value_1 = employee_data["RelationshipSatisfaction"].value_counts()
    plt.title("Employees by Relationship Satisfaction", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=['#6495ED', '#87CEEB', '#00BFFF', '#1E90FF'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by Relationship Satisfaction
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["RelationshipSatisfaction"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by Relationship Satisfaction", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_work_life_balance(employee_data):
    plt.figure(figsize=(13, 6))
    
    # Total Employees by WorkLifeBalance
    plt.subplot(1, 2, 1)
    value_1 = employee_data["WorkLifeBalance"].value_counts()
    plt.title("Employees by WorkLifeBalance", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=['#FF8000', '#FF9933', '#FFB366', '#FFCC99'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by WorkLifeBalance
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["WorkLifeBalance"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index, y=value_2.values, order=value_2.index, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by WorkLifeBalance", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())


def plot_attrition_by_total_working_years(employee_data):
    # Define the bin edges for the groups
    bin_edges = [0, 5, 10, 20, 50]
    
    # Define the labels for the groups
    bin_labels = ['0-5 years', '5-10 years', '10-20 years', "20+ years"]
    
    # Cut the TotalWorkingYears column into groups
    employee_data["TotalWorkingYearsGroup"] = pd.cut(employee_data['TotalWorkingYears'], bins=bin_edges, labels=bin_labels)

    plt.figure(figsize=(14, 6))
    
    # Total Employees by TotalWorkingYearsGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["TotalWorkingYearsGroup"].value_counts()
    plt.title("Employees by TotalWorkingYears", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#E84040', '#E96060', '#E88181', '#E7A1A1'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by TotalWorkingYearsGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["TotalWorkingYearsGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by TotalWorkingYears", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())



def plot_attrition_by_years_at_company(employee_data):
    # Define the bin edges and labels
    bin_edges = [0, 1, 5, 10, 20]
    bin_labels = ['0-1 years', '2-5 years', '5-10 years', "10+ years"]
    
    # Create YearsAtCompanyGroup if not exists
    if 'YearsAtCompanyGroup' not in employee_data.columns:
        employee_data["YearsAtCompanyGroup"] = pd.cut(employee_data['YearsAtCompany'], bins=bin_edges, labels=bin_labels)

    plt.figure(figsize=(13, 6))

    # Total Employees by YearsAtCompanyGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["YearsAtCompanyGroup"].value_counts()
    plt.title("Employees by YearsAtCompany", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.8, startangle=90,
            colors=['#FFB300', '#FFC300', '#FFD700', '#FFFF00'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)

    # Attrition Rate by YearsAtCompanyGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["YearsAtCompanyGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by YearsAtCompany", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())  




def plot_attrition_by_years_in_current_role(employee_data):
    # Define the bin edges and labels
    bin_edges = [0, 1, 5, 10, 20]
    bin_labels = ['0-1 years', '2-5 years', '5-10 years', "10+ years"]
    
    # Create YearsInCurrentRoleGroup if not exists
    if 'YearsInCurrentRoleGroup' not in employee_data.columns:
        employee_data["YearsInCurrentRoleGroup"] = pd.cut(employee_data['YearsInCurrentRole'], bins=bin_edges, labels=bin_labels)
    
    plt.figure(figsize=(13, 6))

    # Total Employees by YearsInCurrentRoleGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["YearsInCurrentRoleGroup"].value_counts()
    plt.title("Employees by YearsInCurrentRole", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#6495ED', '#87CEEB', '#00BFFF', '#1E90FF'], textprops={"fontweight": "black", "size": 15, "color": "black"})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by YearsInCurrentRoleGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["YearsInCurrentRoleGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by YearsInCurrentRole", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())  # Display in Streamlit





def plot_attrition_by_years_since_last_promotion(employee_data):
    # Define the bin edges and labels
    bin_edges = [0, 1, 5, 10, 20]
    bin_labels = ['0-1 years', '2-5 years', '5-10 years', "10+ years"]
    
    # Create YearsSinceLastPromotionGroup if not exists
    if 'YearsSinceLastPromotionGroup' not in employee_data.columns:
        employee_data["YearsSinceLastPromotionGroup"] = pd.cut(employee_data['YearsSinceLastPromotion'], bins=bin_edges, labels=bin_labels)
    
    plt.figure(figsize=(13, 6))

    # Total Employees by YearsSinceLastPromotionGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["YearsSinceLastPromotionGroup"].value_counts()
    plt.title("Employees by YearsSinceLastPromotion", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#FF6D8C', '#FF8C94', '#FFAC9B', '#FFCBA4'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by YearsSinceLastPromotionGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["YearsSinceLastPromotionGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by YearsSinceLastPromotion", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())  # Display in Streamlit







def plot_attrition_by_years_with_current_manager(employee_data):
    # Define the bin edges and labels
    bin_edges = [0, 1, 5, 10, 20]
    bin_labels = ['0-1 years', '2-5 years', '5-10 years', "10+ years"]
    
    # Create YearsWithCurrManagerGroup if not exists
    if 'YearsWithCurrManagerGroup' not in employee_data.columns:
        employee_data["YearsWithCurrManagerGroup"] = pd.cut(employee_data['YearsWithCurrManager'], bins=bin_edges, labels=bin_labels)
    
    plt.figure(figsize=(13, 6))

    # Total Employees by YearsWithCurrManagerGroup
    plt.subplot(1, 2, 1)
    value_1 = employee_data["YearsWithCurrManagerGroup"].value_counts()
    plt.title("Employees by YearsWithCurrManager", fontweight="black", size=20, pad=20)
    plt.pie(value_1.values, labels=value_1.index, autopct="%.1f%%", pctdistance=0.75, startangle=90,
            colors=['#FF8000', '#FF9933', '#FFB366', '#FFCC99'], textprops={"fontweight": "black", "size": 15})
    center_circle = plt.Circle((0, 0), 0.4, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    
    # Attrition Rate by YearsWithCurrManagerGroup
    plt.subplot(1, 2, 2)
    new_df = employee_data[employee_data["Attrition"] == "Yes"]
    value_2 = new_df["YearsWithCurrManagerGroup"].value_counts()
    attrition_rate = np.floor((value_2 / value_1) * 100).values
    sns.barplot(x=value_2.index.tolist(), y=value_2.values, palette=["#11264e", "#6faea4", "#FEE08B", "#D4A1E7", "#E7A1A1"])
    plt.title("Attrition Rate by YearsWithCurrManager", fontweight="black", size=20, pad=20)
    for index, value in enumerate(value_2):
        plt.text(index, value, f"{value} ({int(attrition_rate[index])}%)", ha="center", va="bottom", size=15, fontweight="black")
    
    plt.tight_layout()
    st.pyplot(plt.gcf())  # Display in Streamlit  







def plot_avg_monthly_income_by_jobrole(employee_data):
    # Group and calculate average income
    avg_income = employee_data.groupby("JobRole")["MonthlyIncome"].mean().sort_values(ascending=False)

    # Plot setup
    plt.figure(figsize=(22, 8))
    plt.subplot(1, 2, 1)
    palette_colors = ["#FFA07A", "#D4A1E7", "#FFC0CB", "#87CEFA", "#98FB98", "#FFDEAD", "#BA55D3", "#40E0D0", "#FFD700"]
    sns.barplot(x=avg_income.index, y=avg_income.values, order=avg_income.index, palette=palette_colors)

    # Title and annotations
    plt.title("Average Monthly Income by Job Role", fontweight="black", size=20, pad=15)
    for index, value in enumerate(avg_income.values):
        plt.text(index, value, f"${int(value):,}", ha="center", va="bottom", fontweight="black", size=12)

    # Styling
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Streamlit render
    st.pyplot(plt.gcf())






def plot_attrition_by_salary_band(employee_data):
    # Convert Attrition to numeric
    employee_data['Attrition_numeric'] = employee_data['Attrition'].map({'Yes': 1, 'No': 0})

    # Assign Salary Band
    def assign_salary_band(income):
        if income <= 3000:
            return 'Low Income'
        elif income <= 6000:
            return 'Mid Income'
        elif income <= 10000:
            return 'Upper Mid'
        else:
            return 'High Income'

    employee_data['SalaryBand'] = employee_data['MonthlyIncome'].apply(assign_salary_band)

    # Group and calculate attrition rate
    attrition_by_band = (
        employee_data.groupby('SalaryBand')['Attrition_numeric']
        .mean()
        .multiply(100)
        .round(2)
        .sort_values(ascending=False)
    )

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=attrition_by_band.index, y=attrition_by_band.values, palette="Set2")
    plt.title("Attrition Rate by Salary Band", fontsize=18, fontweight='bold')
    plt.xlabel("Salary Band", fontsize=14)
    plt.ylabel("Attrition Rate (%)", fontsize=14)

    # Annotate each bar
    for index, value in enumerate(attrition_by_band.values):
        plt.text(index, value + 1, f"{value}%", ha="center", va="bottom", fontsize=12, fontweight='bold')

    plt.tight_layout()
    st.pyplot(plt.gcf())







def plot_income_by_job_level(employee_data):
    plt.figure(figsize=(12, 6))

    # Ensure JobLevel is sorted (if numeric)
    sorted_levels = sorted(employee_data["JobLevel"].unique())

    # Boxplot
    sns.boxplot(
        x="JobLevel",
        y="MonthlyIncome",
        data=employee_data,
        order=sorted_levels,
        palette="pastel",
        showfliers=False
    )

    # Mean Monthly Income per JobLevel
    income_means = employee_data.groupby("JobLevel")["MonthlyIncome"].mean().loc[sorted_levels]

    # Plot the mean line
    plt.plot(sorted_levels, income_means, marker='o', color='red', linewidth=2, label="Average Income")

    # Annotate mean values
    for idx, val in enumerate(income_means):
        plt.text(idx, val + 500, f"${int(val)}", ha='center', fontsize=12, fontweight="bold", color="black")

    # Titles and labels
    plt.title("Monthly Income Trend by Job Level", fontweight="black", size=18, pad=30)
    plt.xlabel("Job Level", fontweight="bold")
    plt.ylabel("Monthly Income ($)", fontweight="bold")
    plt.legend()
    plt.tight_layout()

    # Display in Streamlit
    st.pyplot(plt.gcf())






def plot_gender_distribution_by_department(employee_data):
    plt.figure(figsize=(16, 6))
    
    # Create the count plot
    ax = sns.countplot(x="Department", hue="Gender", data=employee_data, palette=["#4C9C57", "#F99D1C"])

    # Set titles and labels
    plt.title("Number of Male and Female Employees by Department", fontweight="black", fontsize=20, pad=15)
    plt.xlabel("Department", fontsize=14, fontweight="bold")
    plt.ylabel("Number of Employees", fontsize=14, fontweight="bold")

    # Annotate bar counts
    for p in ax.patches:
        height = int(p.get_height())
        ax.annotate(
            f'{height}',
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center',
            va='center',
            size=12,
            weight='bold',
            color='black',
            xytext=(0, 5),
            textcoords='offset points'
        )

    # Final layout adjustments
    plt.tight_layout()
    st.pyplot(plt.gcf())







def anova_test_feature_importance(employee_data):
    st.subheader("ANOVA Test: Numerical Feature Importance in Employee Attrition")

    # Select only numeric columns
    num_cols = employee_data.select_dtypes(include=np.number).columns.tolist()

    # Create a copy to modify Attrition
    new_df = employee_data.copy()
    new_df["Attrition"] = new_df["Attrition"].replace({"No": 0, "Yes": 1})

    # Initialize dictionaries to store f-scores and p-values
    f_scores = {}
    p_values = {}

    # Perform ANOVA test for each numerical feature
    for column in num_cols:
        try:
            f_score, p_value = stats.f_oneway(new_df[column], new_df["Attrition"])
            f_scores[column] = f_score
            p_values[column] = p_value
        except Exception as e:
            st.warning(f"Could not compute ANOVA for {column}: {e}")

    # Create DataFrame from results
    anova_results = pd.DataFrame({
        "Features": list(f_scores.keys()),
        "F_Score": list(f_scores.values())
    })
    anova_results["P_Value"] = [format(p, '.20f') for p in p_values.values()]

    # Sort by F_Score descending
    anova_results = anova_results.sort_values(by="F_Score", ascending=False)

    # Display DataFrame in Streamlit
    st.dataframe(anova_results.style.background_gradient(cmap="coolwarm"))

    # Visualization
    st.subheader("F-Score Comparison Across Features")
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.barplot(x="Features", y="F_Score", data=anova_results, palette="viridis", ax=ax)
    ax.set_title("ANOVA Test F-Scores Comparison", fontweight="bold", fontsize=20, pad=15)
    ax.set_ylabel("F-Score", fontweight="bold")
    ax.set_xlabel("Numerical Features", fontweight="bold")
    plt.xticks(rotation=90)

    # Add value labels
    for index, value in enumerate(anova_results["F_Score"]):
        ax.text(index, value, f"{int(value)}", ha="center", va="bottom", fontweight="bold", fontsize=12)

    # Show plot in Streamlit
    st.pyplot(fig)







def chi_square_test_feature_importance(employee_data):
    st.subheader("Chi-Square Test: Categorical Feature Importance in Employee Attrition")

    # Select only categorical columns
    cat_cols = employee_data.select_dtypes(include="object").columns.tolist()
    if "Attrition" in cat_cols:
        cat_cols.remove("Attrition")

    chi2_statistic = {}
    p_values = {}

    # Perform chi-square test for each categorical feature
    for col in cat_cols:
        try:
            contingency_table = pd.crosstab(employee_data[col], employee_data['Attrition'])
            chi2, p_value, _, _ = chi2_contingency(contingency_table)
            chi2_statistic[col] = chi2
            p_values[col] = p_value
        except Exception as e:
            st.warning(f"Could not compute Chi-Square for {col}: {e}")

    # Convert results to a DataFrame
    chi2_results = pd.DataFrame({
        "Features": list(chi2_statistic.keys()),
        "Chi2_Statistic": list(chi2_statistic.values())
    })
    chi2_results["P_Value"] = [format(p, '.20f') for p in p_values.values()]

    # Display table
    st.dataframe(chi2_results.style.background_gradient(cmap="Blues"))

    # Visualization
    st.subheader("Chi-Square Statistic Comparison Across Features")
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.barplot(x="Features", y="Chi2_Statistic", data=chi2_results, palette="cubehelix", ax=ax)
    ax.set_title("Chi-Square Statistic Value of Categorical Features", fontweight="bold", fontsize=20, pad=15)
    ax.set_ylabel("Chi2 Statistic", fontweight="bold")
    ax.set_xlabel("Categorical Features", fontweight="bold")
    plt.xticks(rotation=90)

    # Add value labels
    for index, value in enumerate(chi2_results["Chi2_Statistic"]):
        ax.text(index, value, f"{round(value, 2)}", ha="center", va="bottom", fontweight="bold", fontsize=12)

    st.pyplot(fig)



