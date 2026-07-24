import pandas as pd
import xgboost as xgb
import streamlit as st

def main():
    
    col1, col2 = st.columns([3, 1])

    with col1:
        st.title("💰 Salary Prediction")
        st.write("This app will help you predict your salary.")

    with col2:
        # Business meeting image
        st.image(
            "https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg",
            width=250,
            caption="Business Meeting"
        )

        # Icons
        st.image(
            [
                "https://cdn-icons-png.flaticon.com/512/3063/3063822.png",
                "https://cdn-icons-png.flaticon.com/512/921/921347.png"
            ],
            width=60
        )
    
    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")

    p1 = st.number_input("Please enter age", 18,70,step=1)

    s1 = st.selectbox("Select the gender",("Male", "Female"))

    if s1=='Male':
        p2=1
    elif s1=='Female':
        p2=2
    
    s2 = st.selectbox("Select the education",("Diploma", "Bachelor", "Master","PhD"))

    if s2=='Diploma':
        p3=0
    elif s2=='Bachelor':
        p3=1
    elif s2=='Master':
        p3=2
    elif s2=='PhD':
        p3=3

    p4 = st.number_input("Please enter experience_years", 0,52,step=1)

    s3 = st.selectbox("Select the department",("Operations", "IT", "Finance", "Sales", "HR" ,"Marketing"))

    if s3=='Operations':
        p5=0
    elif s3=='IT':
        p5=1
    elif s3=='Finance':
        p5=2
    elif s3=='Sales':
        p5=3
    elif s3=='HR':
        p5=4
    elif s3=='Marketing':
        p5=5
    
    s4 = st.selectbox("Select the job_level",("Junior", "Mid", "Senior", "Lead", "Manager"))

    if s4=='Junior':
        p6=1
    elif s4=='Mid':
        p6=2
    elif s4=='Senior':
        p6=3
    elif s4=='Lead':
        p6=4
    elif s4=='Manager':
        p6=5

    p7 = st.slider("Select the performance_rating",1,5)

    p8 = st.slider("How many certifications",0,10)

    p9 = st.number_input("Select the overtime_hours", 0,60,step=1)

    s5 = st.selectbox("Select the remote_work",("Yes","No"))

    if s5=='Yes':
        p10=1
    elif s5=='No':
        p10=2

    s6 = st.selectbox("Select the city",("Hyderabad", "Mumbai", "Pune", "Chennai", "Bangalore", "Delhi"))

    if s6=='Hyderabad':
        p11=0
    elif s6=='Mumbai':
        p11=1
    elif s6=='Pune':
        p11=2
    elif s6=='Chennai':
        p11=3
    elif s6=='Bangalore':
        p11=4
    elif s6=='Delhi':
        p11=5

    p12 = st.slider("Select the company_tenure",0,15)

    p13 = st.slider("Select the projects_completed",1,30)

    p14 = st.slider("Select the Skill_Score",50,100)
    
    data_new = pd.DataFrame({
        'Age': p1,
        'Gender': p2,
        'Education':p3,
        'Experience_Years': p4,
        'Department': p5,
        'Job_Level': p6,
        'Performance_Rating': p7,
        'Certifications': p8,
        'Overtime_Hours': p9,
        'Remote_Work': p10,
        'City': p11,
        'Company_Tenure': p12,
        'Projects_Completed': p13,
        'Skill_Score': p14
    },index=[0])

    if st.button("Predict"):
        pred = model.predict(data_new)
        st.success("Your salary is {:.2f} lakhs".format(pred[0]))

if __name__ == '__main__':
    main()