
import streamlit as st
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import base64
from scipy.stats import chi2_contingency  
import scipy.stats as stats
from streamlit_lottie import st_lottie
import requests
import time



from VisualizationofallAnalysis import (
    # Descriptive
    plot_attrition_rate,
    plot_attrition_by_gender,
    plot_attrition_by_age,
    plot_attrition_by_department,
    plot_attrition_by_marital_status,
    plot_attrition_by_job_roles,
    plot_attrition_by_education_field,

    # Diagnostic
    plot_attrition_by_business_travel,
    plot_attrition_by_daily_rate,
    plot_attrition_by_distance_from_home,
    plot_attrition_by_education,
    plot_attrition_by_environment_satisfaction,
    plot_attrition_by_job_level,
    plot_attrition_by_job_satisfaction,
    plot_attrition_by_monthly_income,
    plot_attrition_by_work_experience,
    plot_attrition_by_overtime,
    plot_attrition_by_salary_hike,
    plot_attrition_by_performance_rating,
    plot_attrition_by_relationship_satisfaction,
    plot_attrition_by_work_life_balance,
    plot_attrition_by_total_working_years,
    plot_attrition_by_years_at_company,
    plot_attrition_by_years_in_current_role,
    plot_attrition_by_years_since_last_promotion,
    plot_attrition_by_years_with_current_manager,



    # Predictive Analysis
    anova_test_feature_importance,
    chi_square_test_feature_importance,


    
    # Some more Analysis
    plot_avg_monthly_income_by_jobrole,
    plot_attrition_by_salary_band,
    plot_income_by_job_level,
    plot_gender_distribution_by_department
)

# ---------------------- Page Configuration ----------------------
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📉",
    layout="wide"
)

# ---------------------- Load Data ----------------------

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("IBM-HR-Analytics-Employee-Attrition-and-Performance-Revised.csv")
        return df
    except FileNotFoundError:
        st.error("Dataset not found. Please ensure the CSV file is in the correct path.")
        return pd.DataFrame()

employee_data = load_data()

# ---------------------- Helper Functions ----------------------





def show_login():

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # If user is already logged in and remembered, skip login
    if st.session_state.get("logged_in") and st.session_state.get("remember_me"):
        st.success(f"✅ Welcome back, {st.session_state.username}!")
        return

    # ---- Header with Animation ----
    with st.container():
        col1 = st.columns([1, 2, 1])[1]
        with col1:
            lottie_animation = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_wqypnpu5.json")
            if lottie_animation:
                st_lottie(lottie_animation, height=200, key="attrition")

            st.markdown(
                """
                <div style='background-color: #1A1A40; padding: 10px; border-radius: 10px; margin-top: -50px;'>
                    <h1 style='text-align: center; color: white;'>🔐 Employee Attrition Web Application</h1>
                </div>
                """,
                unsafe_allow_html=True
            )  

    st.write("")  # spacing

    # ---- Centered Login Form ----
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.form("login_form"):
                st.markdown(
                    """
                    <div style="
                        background-color:  #FFD9E6;
                        padding: 30px;
                        border-radius: 15px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
                        border: 2px solid #1A1A1A;
                        text-align: center;
                    ">
                    <h2 style='margin-bottom: 20px; color: #333;'>Login to Continue</h2>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <style>
                        .stTextInput>div>div>input {
                            text-transform: uppercase;
                            font-size: 16px;
                            padding: 10px;
                            text-align: center;
                        }
                        .stTextInput>label {
                            font-weight: bold;
                            text-transform: uppercase;
                            font-size: 14px;
                        }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("<h3 style='font-weight: bold; text-transform: uppercase;'>🙂 Please Enter !</h3>", unsafe_allow_html=True)
                username = st.text_input("Username", placeholder="Enter your username")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                remember_me = st.checkbox("Remember Me", value=False)
                
                login_button = st.form_submit_button("Login", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            if login_button:
                if not username or not password:
                    st.warning("⚠️ Please fill in both Username and Password.")
                else:
                    with st.spinner('Authenticating...'):
                        time.sleep(1)

                        if username in ["somya", "viewer", "admin"] and password == "admin@1234":
                            st.session_state.logged_in = True
                            st.session_state.username = username
                            st.session_state.role = "admin" if username == "admin" else "viewer"
                            st.session_state.remember_me = remember_me
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error("❌ Incorrect username or password.")

    st.write("")  # spacing

    # ---- Footer ----
    st.markdown(
        """
        <hr style='border: 1px solid #ccc;'>
        <p style='text-align: center; color: gray;'>© 2025 Employee Attrition Analysis. All rights reserved.</p>
        <p style='text-align: center; color: gray;'>For support, contact us at: <a href='mailto:kharesomya251@gmail.com' style='color: gray;'>kharesomya251@gmail.com</a></p>
        """,
        unsafe_allow_html=True
    )


def show_main_menu():
    with st.sidebar:
        st.markdown("## 📋 Navigation Menu", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"👤 **User:** `{st.session_state.username}`")
        st.markdown(f"⏰ **Login Time:** `{datetime.now().strftime('%I:%M:%S %p')}`")
        st.markdown("---")
        
        if st.session_state.role == "admin":
            page = st.radio(
                "🔎 **Select a Page:**",
                [
                    "📊 Overview Dashboard",
                    "📝 Descriptive Analysis",
                    "🛠️ Diagnostic Analysis",
                    "🔮 Predictive Analysis",
                    "🧮 Some More Analysis",
                    "📈 Correlation Heatmap",
                    "🚪 Logout"
                ],
                label_visibility="collapsed"
            )
        else:
            page = st.radio(
                "🔎 **Select a Page:**",
                [
                    "📝 Descriptive Analysis",
                    "🛠️ Diagnostic Analysis",
                    "🔮 Predictive Analysis",
                    "🧮 Some More Analysis",
                    "🚪 Logout"
                ],
                label_visibility="collapsed"
            )
        
        st.markdown("---")
        st.caption("Made with ❤️ by Somya Khare")

    return page





def show_dashboard(data):
    st.title("📊 Overview Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Attrition Rate", f"{data[data['Attrition'] == 'Yes'].shape[0] / data.shape[0] * 100:.1f}%")
    col2.metric("Total Employees", f"{data.shape[0]}")
    col3.metric("Average Monthly Income", f"${data['MonthlyIncome'].mean():,.2f}")

    st.markdown("---")
    st.subheader("Filter Data")
    department = st.selectbox("Select Department", ["All"] + list(data["Department"].unique()))
    gender = st.selectbox("Select Gender", ["All"] + list(data["Gender"].unique()))

    filtered_data = data.copy()
    if department != "All":
        filtered_data = filtered_data[filtered_data["Department"] == department]
    if gender != "All":
        filtered_data = filtered_data[filtered_data["Gender"] == gender]

    st.write(filtered_data)
    csv = filtered_data.to_csv(index=False).encode()
    st.download_button("Download Filtered Data", csv, "filtered_employee_data.csv", "text/csv")

def show_correlation_heatmap(data):
    st.title("📌 Correlation Heatmap")
    numeric_data = data.select_dtypes(include=['int64', 'float64'])
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)




def show_descriptive_analysis(data):
    st.title("📝 Descriptive Analysis")


# Create columns
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)

    with col1:
        department = st.selectbox("Select Department", ["All"] + list(data["Department"].unique()))
    with col2:
        education = st.selectbox("Select Education Field", ["All"] + list(data["EducationField"].unique()))
    with col3:
        gender = st.selectbox("Select Gender", ["All"] + list(data["Gender"].unique()))
    with col4:
        job_role = st.selectbox("Select Job Role", ["All"] + list(data["JobRole"].unique()))
    with col5:
        marital_status = st.selectbox("Select Marital Status", ["All"] + list(data["MaritalStatus"].unique()))
    with col6:
        overtime = st.selectbox("Select OverTime", ["All"] + list(data["OverTime"].unique()))
    with col7:
        business_travel = st.selectbox("Select Business Travel", ["All"] + list(data["BusinessTravel"].unique()))
    with col8:
        performance_rating = st.selectbox("Select Performance Rating", ["All"] + sorted(data["PerformanceRating"].unique()))
    with col9:
        job_level = st.selectbox("Select Job Level", ["All"] + sorted(data["JobLevel"].unique()))
    with col10:
        work_life_balance = st.selectbox("Select Work Life Balance", ["All"] + sorted(data["WorkLifeBalance"].unique()))

    # Age Range Slider
    min_age = int(data["Age"].min())
    max_age = int(data["Age"].max())
    age_range = st.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

    # Filter the data based on selections
    filtered_data = data.copy()

    if department != "All":
        filtered_data = filtered_data[filtered_data["Department"] == department]
    if education != "All":
        filtered_data = filtered_data[filtered_data["EducationField"] == education]
    if gender != "All":
        filtered_data = filtered_data[filtered_data["Gender"] == gender]
    if job_role != "All":
        filtered_data = filtered_data[filtered_data["JobRole"] == job_role]
    if marital_status != "All":
        filtered_data = filtered_data[filtered_data["MaritalStatus"] == marital_status]
    if overtime != "All":
        filtered_data = filtered_data[filtered_data["OverTime"] == overtime]
    if business_travel != "All":
        filtered_data = filtered_data[filtered_data["BusinessTravel"] == business_travel]
    if performance_rating != "All":
        filtered_data = filtered_data[filtered_data["PerformanceRating"] == performance_rating]
    if job_level != "All":
        filtered_data = filtered_data[filtered_data["JobLevel"] == job_level]
    if work_life_balance != "All":
        filtered_data = filtered_data[filtered_data["WorkLifeBalance"] == work_life_balance]

    # Filter based on Age Range
    filtered_data = filtered_data[(filtered_data["Age"] >= age_range[0]) & (filtered_data["Age"] <= age_range[1])]



    option = st.selectbox("Select an Analysis", [
        "Attrition Rate",
        "Attrition by Gender",
        "Attrition by Age",
        "Attrition by Department",
        "Attrition by Marital Status",
        "Attrition by Job Role",
        "Attrition by Education Field"])

    if option == "Attrition Rate":
        plot_attrition_rate(filtered_data)
    elif option == "Attrition by Gender":
        plot_attrition_by_gender(filtered_data)
    elif option == "Attrition by Age":
        plot_attrition_by_age(filtered_data)
    elif option == "Attrition by Department":
        plot_attrition_by_department(filtered_data)
    elif option == "Attrition by Marital Status":
        plot_attrition_by_marital_status(filtered_data)
    elif option == "Attrition by Job Role":
        plot_attrition_by_job_roles(filtered_data)
    elif option == "Attrition by Education Field":
        plot_attrition_by_education_field(filtered_data)




def show_diagnostic_analysis(data):
    st.title("🛠️ Diagnostic Analysis")

 # Create columns
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)

    with col1:
        department = st.selectbox("Select Department", ["All"] + list(data["Department"].unique()))
    with col2:
        education = st.selectbox("Select Education Field", ["All"] + list(data["EducationField"].unique()))
    with col3:
        gender = st.selectbox("Select Gender", ["All"] + list(data["Gender"].unique()))
    with col4:
        job_role = st.selectbox("Select Job Role", ["All"] + list(data["JobRole"].unique()))
    with col5:
        marital_status = st.selectbox("Select Marital Status", ["All"] + list(data["MaritalStatus"].unique()))
    with col6:
        overtime = st.selectbox("Select OverTime", ["All"] + list(data["OverTime"].unique()))
    with col7:
        business_travel = st.selectbox("Select Business Travel", ["All"] + list(data["BusinessTravel"].unique()))
    with col8:
        performance_rating = st.selectbox("Select Performance Rating", ["All"] + sorted(data["PerformanceRating"].unique()))
    with col9:
        job_level = st.selectbox("Select Job Level", ["All"] + sorted(data["JobLevel"].unique()))
    with col10:
        work_life_balance = st.selectbox("Select Work Life Balance", ["All"] + sorted(data["WorkLifeBalance"].unique()))

    # Age Range Slider
    min_age = int(data["Age"].min())
    max_age = int(data["Age"].max())
    age_range = st.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

    # Filter the data based on selections
    filtered_data = data.copy()

    if department != "All":
        filtered_data = filtered_data[filtered_data["Department"] == department]
    if education != "All":
        filtered_data = filtered_data[filtered_data["EducationField"] == education]
    if gender != "All":
        filtered_data = filtered_data[filtered_data["Gender"] == gender]
    if job_role != "All":
        filtered_data = filtered_data[filtered_data["JobRole"] == job_role]
    if marital_status != "All":
        filtered_data = filtered_data[filtered_data["MaritalStatus"] == marital_status]
    if overtime != "All":
        filtered_data = filtered_data[filtered_data["OverTime"] == overtime]
    if business_travel != "All":
        filtered_data = filtered_data[filtered_data["BusinessTravel"] == business_travel]
    if performance_rating != "All":
        filtered_data = filtered_data[filtered_data["PerformanceRating"] == performance_rating]
    if job_level != "All":
        filtered_data = filtered_data[filtered_data["JobLevel"] == job_level]
    if work_life_balance != "All":
        filtered_data = filtered_data[filtered_data["WorkLifeBalance"] == work_life_balance]

    # Filter based on Age Range
    filtered_data = filtered_data[(filtered_data["Age"] >= age_range[0]) & (filtered_data["Age"] <= age_range[1])]



    
    option = st.selectbox("Select an Analysis", [
        "Attrition by Business Travel",
        "Attrition by Daily Rate",
        "Attrition by Distance From Home",
        "Attrition by Education",
        "Attrition by Environment Satisfaction",
        "Attrition by Job Level",
        "Attrition by Job Satisfaction",
        "Attrition by Monthly Income",
        "Attrition by Work Experience",
        "Attrition by OverTime",
        "Attrition by Salary Hike",
        "Attrition by Performance Rating",
        "Attrition by Relationship Satisfaction",
        "Attrition by Work Life Balance",
        "Attrition by Total Working Years",
        "Attrition by Years at Company",
        "Attrition by Years in Current Role",
        "Attrition by Years Since Last Promotion",
        "Attrition by Years with Current Manager"])

    if option == "Attrition by Business Travel":
        plot_attrition_by_business_travel(filtered_data)
    elif option == "Attrition by Daily Rate":
        plot_attrition_by_daily_rate(filtered_data)
    elif option == "Attrition by Distance From Home":
        plot_attrition_by_distance_from_home(filtered_data)
    elif option == "Attrition by Education":
        plot_attrition_by_education(filtered_data)
    elif option == "Attrition by Environment Satisfaction":
        plot_attrition_by_environment_satisfaction(filtered_data)
    elif option == "Attrition by Job Level":
        plot_attrition_by_job_level(filtered_data)
    elif option == "Attrition by Job Satisfaction":
        plot_attrition_by_job_satisfaction(filtered_data)
    elif option == "Attrition by Monthly Income":
        plot_attrition_by_monthly_income(filtered_data)
    elif option == "Attrition by Work Experience":
        plot_attrition_by_work_experience(filtered_data)
    elif option == "Attrition by OverTime":
        plot_attrition_by_overtime(filtered_data)
    elif option == "Attrition by Salary Hike":
        plot_attrition_by_salary_hike(filtered_data)
    elif option == "Attrition by Performance Rating":
        plot_attrition_by_performance_rating(filtered_data)
    elif option == "Attrition by Relationship Satisfaction":
        plot_attrition_by_relationship_satisfaction(filtered_data)
    elif option == "Attrition by Work Life Balance":
        plot_attrition_by_work_life_balance(filtered_data)
    elif option == "Attrition by Total Working Years":
        plot_attrition_by_total_working_years(filtered_data)
    elif option == "Attrition by Years at Company":
        plot_attrition_by_years_at_company(filtered_data)
    elif option == "Attrition by Years in Current Role":
        plot_attrition_by_years_in_current_role(filtered_data)
    elif option == "Attrition by Years Since Last Promotion":
        plot_attrition_by_years_since_last_promotion(filtered_data)
    elif option == "Attrition by Years with Current Manager":
        plot_attrition_by_years_with_current_manager(filtered_data)



def Predictive_Analysis(employee_data):
    st.title("🔮 Predictive Analysis")

    # Create columns
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)

    with col1:
        department = st.selectbox("Select Department", ["All"] + list(employee_data["Department"].unique()))
    with col2:
        education = st.selectbox("Select Education Field", ["All"] + list(employee_data["EducationField"].unique()))
    with col3:
        gender = st.selectbox("Select Gender", ["All"] + list(employee_data["Gender"].unique()))
    with col4:
        job_role = st.selectbox("Select Job Role", ["All"] + list(employee_data["JobRole"].unique()))
    with col5:
        marital_status = st.selectbox("Select Marital Status", ["All"] + list(employee_data["MaritalStatus"].unique()))
    with col6:
        overtime = st.selectbox("Select OverTime", ["All"] + list(employee_data["OverTime"].unique()))
    with col7:
        business_travel = st.selectbox("Select Business Travel", ["All"] + list(employee_data["BusinessTravel"].unique()))
    with col8:
        performance_rating = st.selectbox("Select Performance Rating", ["All"] + sorted(employee_data["PerformanceRating"].unique()))
    with col9:
        job_level = st.selectbox("Select Job Level", ["All"] + sorted(employee_data["JobLevel"].unique()))
    with col10:
        work_life_balance = st.selectbox("Select Work Life Balance", ["All"] + sorted(employee_data["WorkLifeBalance"].unique()))

    # Age Range Slider
    min_age = int(employee_data["Age"].min())
    max_age = int(employee_data["Age"].max())
    age_range = st.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

    # Filter the data based on selections
    filtered_data = employee_data.copy()

    if department != "All":
        filtered_data = filtered_data[filtered_data["Department"] == department]
    if education != "All":
        filtered_data = filtered_data[filtered_data["EducationField"] == education]
    if gender != "All":
        filtered_data = filtered_data[filtered_data["Gender"] == gender]
    if job_role != "All":
        filtered_data = filtered_data[filtered_data["JobRole"] == job_role]
    if marital_status != "All":
        filtered_data = filtered_data[filtered_data["MaritalStatus"] == marital_status]
    if overtime != "All":
        filtered_data = filtered_data[filtered_data["OverTime"] == overtime]
    if business_travel != "All":
        filtered_data = filtered_data[filtered_data["BusinessTravel"] == business_travel]
    if performance_rating != "All":
        filtered_data = filtered_data[filtered_data["PerformanceRating"] == performance_rating]
    if job_level != "All":
        filtered_data = filtered_data[filtered_data["JobLevel"] == job_level]
    if work_life_balance != "All":
        filtered_data = filtered_data[filtered_data["WorkLifeBalance"] == work_life_balance]

    # Filter based on Age Range
    filtered_data = filtered_data[(filtered_data["Age"] >= age_range[0]) & (filtered_data["Age"] <= age_range[1])]

    # Dropdown for selecting the type of analysis
    option = st.selectbox("Select Analysis Type", [
        "Chi-Square Test (Categorical Features)",
        "ANOVA Test (Numerical Features)"
    ])

    if option == "Chi-Square Test (Categorical Features)":
        chi_square_test_feature_importance(filtered_data)

    elif option == "ANOVA Test (Numerical Features)":
        anova_test_feature_importance(filtered_data)




def show_some_more_analysis(data):
    st.title("🧮 Some More Analysis")

   # Create columns
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)

    with col1:
        department = st.selectbox("Select Department", ["All"] + list(data["Department"].unique()))
    with col2:
        education = st.selectbox("Select Education Field", ["All"] + list(data["EducationField"].unique()))
    with col3:
        gender = st.selectbox("Select Gender", ["All"] + list(data["Gender"].unique()))
    with col4:
        job_role = st.selectbox("Select Job Role", ["All"] + list(data["JobRole"].unique()))
    with col5:
        marital_status = st.selectbox("Select Marital Status", ["All"] + list(data["MaritalStatus"].unique()))
    with col6:
        overtime = st.selectbox("Select OverTime", ["All"] + list(data["OverTime"].unique()))
    with col7:
        business_travel = st.selectbox("Select Business Travel", ["All"] + list(data["BusinessTravel"].unique()))
    with col8:
        performance_rating = st.selectbox("Select Performance Rating", ["All"] + sorted(data["PerformanceRating"].unique()))
    with col9:
        job_level = st.selectbox("Select Job Level", ["All"] + sorted(data["JobLevel"].unique()))
    with col10:
        work_life_balance = st.selectbox("Select Work Life Balance", ["All"] + sorted(data["WorkLifeBalance"].unique()))

    # Age Range Slider
    min_age = int(data["Age"].min())
    max_age = int(data["Age"].max())
    age_range = st.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

    # Filter the data based on selections
    filtered_data = data.copy()

    if department != "All":
        filtered_data = filtered_data[filtered_data["Department"] == department]
    if education != "All":
        filtered_data = filtered_data[filtered_data["EducationField"] == education]
    if gender != "All":
        filtered_data = filtered_data[filtered_data["Gender"] == gender]
    if job_role != "All":
        filtered_data = filtered_data[filtered_data["JobRole"] == job_role]
    if marital_status != "All":
        filtered_data = filtered_data[filtered_data["MaritalStatus"] == marital_status]
    if overtime != "All":
        filtered_data = filtered_data[filtered_data["OverTime"] == overtime]
    if business_travel != "All":
        filtered_data = filtered_data[filtered_data["BusinessTravel"] == business_travel]
    if performance_rating != "All":
        filtered_data = filtered_data[filtered_data["PerformanceRating"] == performance_rating]
    if job_level != "All":
        filtered_data = filtered_data[filtered_data["JobLevel"] == job_level]
    if work_life_balance != "All":
        filtered_data = filtered_data[filtered_data["WorkLifeBalance"] == work_life_balance]

    # Filter based on Age Range
    filtered_data = filtered_data[(filtered_data["Age"] >= age_range[0]) & (filtered_data["Age"] <= age_range[1])]



    option = st.selectbox("Select an Analysis", [
        "Average Monthly Income by Job Role",
        "Attrition by Salary Band",
        "Monthly Income by Job Level",
        "Gender Distribution by Department"])

    if option == "Average Monthly Income by Job Role":
        plot_avg_monthly_income_by_jobrole(filtered_data)
    elif option == "Attrition by Salary Band":
        plot_attrition_by_salary_band(filtered_data)
    elif option == "Monthly Income by Job Level":
        plot_income_by_job_level(filtered_data)
    elif option == "Gender Distribution by Department":
        plot_gender_distribution_by_department(filtered_data)




def logout():
    st.session_state.logged_in = False
    st.success("You have been logged out.")
    # Redirect to the login page
    st.rerun()

# ---------------------- Main App Logic ----------------------

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        show_login()  # Show the login page
    else:
        page = show_main_menu()  # Show the main menu once logged in

        if page == "📊 Overview Dashboard":
            show_dashboard(employee_data)
        elif page == "📝 Descriptive Analysis":
            show_descriptive_analysis(employee_data)
        elif page == "🛠️ Diagnostic Analysis":
            show_diagnostic_analysis(employee_data)
        elif page == "🔮 Predictive Analysis":  
            Predictive_Analysis(employee_data)
        elif page == "🧮 Some More Analysis":
            show_some_more_analysis(employee_data)
        elif page == "📈 Correlation Heatmap":
            show_correlation_heatmap(employee_data)
        elif page == "🚪 Logout":
            logout()  # Logout and redirect to the login page

if __name__ == "__main__":
    main()
