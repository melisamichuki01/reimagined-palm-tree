import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
stsurveydf = pd.read_csv(r'C:\Users\PC\surveywebapp\stsurveydf.csv', index_col=None)
Mentordf = pd.read_csv(r'C:\Users\PC\surveywebapp\Mentordf.csv', index_col=0)  # Assuming 'Unnamed: 0' is the index column, adjust accordingly
#Mentordf.drop('Unnamed: 0', axis=1, inplace=True)

# Define a function to generate the report
def generate_survey_report():
    # Introduction
    st.title("Report on Student Survey Findings")
    st.markdown("## Introduction:")
    st.write("We conducted a comprehensive survey to gather insights from 291 respondents across various classes at eMobilis. The objective was to understand student satisfaction, evaluate lecturer support and knowledge, assess curriculum relevance, learning objectives, teaching methods, engagement levels, and overall program satisfaction.")

    # Respondent Demographics
    st.markdown("## Respondent Demographics:")
    st.write("The survey included students from different classes, with the highest number in the Samsung class (37 respondents) and the lowest in the Microsoft class (18 respondents). The respondents were taught by a diverse group of lecturers, with Mr. Erick and Mr. Walter having the highest counts of 63 and 62, respectively.")

    # Key Findings
    st.markdown("## Key Findings:")
    
    # 1. Student Satisfaction Levels
    st.subheader("1. Student Satisfaction Levels:")
    st.write("- **Program Satisfaction:** A majority of students (176 out of 291) expressed being very satisfied with the program, followed by 105 students who reported satisfaction.")
    st.write("- **Recommendation:** An overwhelming majority (289 out of 291) would recommend the program, indicating a high level of satisfaction and endorsement.")

    # 2. Lecturer Support/Knowledge
    st.subheader("2. Lecturer Support/Knowledge:")
    st.write("- **Lecturer Ratings:** The lecturers received excellent ratings from the majority (245 out of 291) of the students.")
    st.write("- **Mentor Support:** 250 students acknowledged receiving sufficient support from mentors, while 34 reported receiving support sometimes, and only 5 students claimed no support.")

    # 3. Meeting of Expectations/Level
    st.subheader("3. Meeting of Expectations/Level:")
    st.write("- **Curriculum Relevance:** A significant number (124 out of 291) strongly agreed that the curriculum is relevant, with only 34 expressing strong disagreement.")
    st.write("- **Learning Objectives:** The majority (190 out of 291) rated the learning objectives as excellent.")

    # 4. Pace of the Class
    st.subheader("4. Pace of the Class:")
    st.write("- **Engagement Levels:** The class pace was perceived positively, with 144 students finding it highly engaging, and 87 finding it engaging.")
    st.write("- **LMS Helpfulness:** 149 students found the Learning Management System (LMS) very helpful.")
    
    # 5. Count summary for 'TeachingMethods'
    teaching_methods_data = {
        'One on one with Lecturers, Peer Group Discussions, Guidance from mentors': 105,
        'One on one with Lecturers': 89,
        'One on one with Lecturers, Guidance from mentors': 31,
        'One on one with Lecturers, Peer Group Discussions': 27,
        'Guidance from mentors': 22,
        'Peer Group Discussions, Guidance from mentors': 9,
        'Peer Group Discussions': 8
    }

    st.subheader("Count summary for TeachingMethods :")
    st.table(pd.DataFrame({'Count': list(teaching_methods_data.values())}, index=list(teaching_methods_data.keys())))

    # Conclusion on Teaching Methods
    st.markdown("## Conclusion on Teaching Methods:")
    st.write("The count summary for teaching methods reveals a diverse range of preferences among students. The most preferred method is 'One on one with Lecturers, Peer Group Discussions, Guidance from mentors,' with 105 respondents favoring this approach. This indicates a positive inclination towards collaborative learning and mentor guidance. Understanding these preferences can guide future curriculum development and teaching strategies to better align with student expectations.")

    # 5. Grouping of Recommendations
    st.subheader("6. Grouping of Recommendations:")
    st.write("- **Class-wise Recommendations:** The recommendations were overwhelmingly positive across all classes, with specific quantities detailed in the count summary.")

    # Conclusion
    st.markdown("## Conclusion:")
    st.write("The survey results indicate a high level of satisfaction among students at eMobilis. The positive feedback on curriculum relevance, learning objectives, lecturer support, and program satisfaction reflects the effectiveness of the Web Development Program. Recommendations from students further strengthen the program's credibility. These insights will be crucial for continuous improvement and tailoring the learning experience to meet the expectations of future students.")

# Define a function to generate the mentor report
def generate_mentor_report():
    st.title("Report on Mentor Survey Findings")
    st.markdown("## Introduction:")
    st.write("We conducted a survey to gather insights from mentors to assess their perspectives on various aspects of the Web Development Program at eMobilis.")

    # Count summary for 'Curriculum_Relevance'
    st.subheader("Count summary for 'Curriculum Relevance':")
    st.table(pd.DataFrame({'Count': [6, 3, 1, 1]}, index=['Agree', 'Strongly Agree', 'Neutral', 'Strongly Disagree']))

    # Conclusion for 'Curriculum Relevance'
    st.markdown("### Conclusion on Curriculum Relevance:")
    st.write("The count summary for curriculum relevance indicates that the majority of mentors either agree or strongly agree that the curriculum is relevant. This positive feedback suggests that the curriculum effectively meets the needs and expectations of mentors, providing valuable insights for maintaining or enhancing the current curriculum.")

    # Count summary for 'Teaching_Methods_Engagement'
    st.subheader("Count summary for 'Teaching Methods Engagement':")
    st.table(pd.DataFrame({'Count': [6, 3, 2]}, index=['Highly Engaging', 'Moderate', 'Engaging']))

    # Conclusion for 'Teaching Methods Engagement'
    st.markdown("### Conclusion on Teaching Methods Engagement:")
    st.write("The count summary for teaching methods engagement reveals that the majority of mentors find the teaching methods to be highly engaging. This positive response suggests that the current teaching methods effectively capture the interest and involvement of mentors, contributing to a positive learning experience.")

    # Count summary for 'LMS_Working'
    st.subheader("Count summary for 'LMS Working':")
    st.table(pd.DataFrame({'Count': [4, 4, 3]}, index=['Very Helpful', 'Moderate', 'Helpful']))

    # Conclusion for 'LMS Working'
    st.markdown("### Conclusion on LMS Working:")
    st.write("The count summary for LMS working indicates that mentors find the Learning Management System (LMS) to be very helpful or moderately helpful. This positive feedback suggests that the LMS effectively supports mentors in their role, providing valuable resources and tools for a smoother mentoring experience.")

    # Count summary for 'Lecturer_Knowledge_Rating'
    st.subheader("Count summary for 'Lecturer Knowledge Rating':")
    st.table(pd.DataFrame({'Count': [8, 2, 1]}, index=['Excellent', 'Good', 'Fair']))

    # Conclusion for 'Lecturer Knowledge Rating'
    st.markdown("### Conclusion on Lecturer Knowledge Rating:")
    st.write("The count summary for lecturer knowledge rating shows that the majority of mentors rate the knowledge of lecturers as excellent. This positive assessment reflects the high level of confidence mentors have in the expertise of lecturers, indicating a strong foundation for effective mentorship.")

    # Count summary for 'Communication_Support_Rating'
    st.subheader("Count summary for 'Communication Support Rating':")
    st.table(pd.DataFrame({'Count': [6, 5]}, index=['Very Good', 'Good']))

    # Conclusion for 'Communication Support Rating'
    st.markdown("### Conclusion on Communication Support Rating:")
    st.write("The count summary for communication support rating reveals positive feedback, with the majority of mentors rating communication support as very good. This suggests effective communication channels and support mechanisms in place, fostering a collaborative and supportive environment for mentors.")

    # Count summary for 'Recommendation'
    st.subheader("Count summary for 'Recommendation':")
    st.write("Yes: 11")
    

    # Conclusion for 'Recommendation'
    st.markdown("### Overall Recommendation:")
    st.write("All 11 respondents recommend the program, indicating unanimous support from mentors. This strong vote of confidence is a positive indicator of the program's effectiveness and the satisfaction of mentors. It highlights the program's success in meeting the expectations and needs of mentors.")





# Set the layout to center the logo
st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 1100px;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }}
        img{{
            max-width: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 20px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Include the logo
st.image('emobilisLogo.png', width=1000)
# Page 1: Barplot for stsurveydf
st.sidebar.title("Page Navigation")
page = st.sidebar.radio("Select Page", ["stsurveydf Plots", "Mentordf Plots"])

if page == "stsurveydf Plots":
    generate_survey_report()

    columns = [
        'Classes',
        'lecturers',
        'CurriculumRelevance',
        'LearningObjectives',
        'LMS_Helpfulness',
        'Lecturer_Rating',
        'ComfortAskingQuestions',
        'Mentor_Support',
        'Mentor_Knowledge',
        'PeerGroupDiscussions_Helpful',
        'Program_Satisfaction',
        'Recommendation'
    ]

    # Sidebar for user selection
    selected_column = st.sidebar.selectbox("Select Column for Barplot", columns)
    st.title("Student Survey  Plots")

    # Checkbox for filtering by Class
    filter_class = st.sidebar.checkbox("Filter by Class")

    # Checkbox for filtering by Lecturer
    filter_lecturer = st.sidebar.checkbox("Filter by Lecturer")

    # Filtering data based on user selection
    if filter_class:
        selected_class = st.sidebar.multiselect("Select Class", stsurveydf['Class'].unique())
        stsurveydf = stsurveydf[stsurveydf['Class'].isin(selected_class)]

    if filter_lecturer:
        selected_lecturer = st.sidebar.multiselect("Select Lecturer", stsurveydf['Lecturer'].unique())
        stsurveydf = stsurveydf[stsurveydf['Lecturer'].isin(selected_lecturer)]

    # Barplot
    fig = px.bar(stsurveydf, x=selected_column, title=f'Distribution of {selected_column}')
    st.plotly_chart(fig)
    
    

    # Display Mentordf table if selected
    display_stsurveydf = st.sidebar.checkbox("Display stsurveydf Table")
    if display_stsurveydf:
        st.subheader("stsurveydf Table:")
        st.table(stsurveydf)

elif page == "Mentordf Plots":
   
    # Display the mentor report
    generate_mentor_report()
    
    # Categorical columns for plots
    categorical_columns = [
        'Curriculum_Relevance',
        'Teaching_Methods_Engagement',
        'LMS_Working',
        'Lecturer_Knowledge_Rating',
        'Communication_Support_Rating',
        'Recommendation'
    ]

    # Sidebar for user selection
    selected_column = st.sidebar.selectbox("Select Column for Barplot", categorical_columns)
    st.title("Mentor Survey  Plots")

    # Barplot
    fig = px.bar(Mentordf, x=selected_column, title=f'Distribution of {selected_column}')
    st.plotly_chart(fig)

    # Display Mentordf table if selected
    display_mentordf = st.sidebar.checkbox("Display Mentordf Table")
    if display_mentordf:
        st.subheader("Mentordf Table:")
        st.table(Mentordf)
