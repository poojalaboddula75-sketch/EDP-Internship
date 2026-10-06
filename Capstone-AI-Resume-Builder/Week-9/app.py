import streamlit as st

st.set_page_config(
    page_title="ResumeAI | AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #243b80;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #5f6b85;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #243b80;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .resume-card {
        padding: 30px;
        border-radius: 16px;
        background: white;
        box-shadow: 0 4px 20px rgba(36, 59, 128, 0.10);
        min-height: 500px;
    }

    .resume-name {
        font-size: 32px;
        font-weight: 800;
        color: #243b80;
    }

    .resume-contact {
        color: #667085;
        margin-bottom: 20px;
    }

    .resume-heading {
        font-size: 18px;
        font-weight: 700;
        color: #5b4bdb;
        border-bottom: 2px solid #e6e8f0;
        padding-bottom: 5px;
        margin-top: 18px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        background: linear-gradient(90deg, #5b4bdb, #7c5cff);
        color: white;
        font-weight: 700;
        padding: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">📄 ResumeAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Build a professional and ATS-friendly resume with AI assistance.</div>',
    unsafe_allow_html=True
)

st.divider()

left, right = st.columns([1, 1.15], gap="large")

with left:

    st.markdown(
        '<div class="section-title">👤 Personal Information</div>',
        unsafe_allow_html=True
    )

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    location = st.text_input("Location")

    st.markdown(
        '<div class="section-title">🎓 Education</div>',
        unsafe_allow_html=True
    )

    education = st.text_area(
        "Education Details",
        placeholder="Degree, college, branch, graduation year..."
    )

    st.markdown(
        '<div class="section-title">💡 Skills</div>',
        unsafe_allow_html=True
    )

    skills = st.text_area(
        "Skills",
        placeholder="Python, Java, SQL, HTML, CSS..."
    )

    st.markdown(
        '<div class="section-title">🚀 Projects</div>',
        unsafe_allow_html=True
    )

    projects = st.text_area(
        "Project Details",
        placeholder="Project name, technologies and your contribution..."
    )

    st.markdown(
        '<div class="section-title">💼 Experience</div>',
        unsafe_allow_html=True
    )

    experience = st.text_area(
        "Experience / Internship",
        placeholder="Company, role, duration and responsibilities..."
    )

    st.markdown(
        '<div class="section-title">📝 Professional Summary</div>',
        unsafe_allow_html=True
    )

    summary = st.text_area(
        "Summary",
        placeholder="Write a short professional summary..."
    )

    generate = st.button("✨ Generate Resume")

with right:

    st.markdown(
        '<div class="section-title">📋 Resume Preview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="resume-card">',
        unsafe_allow_html=True
    )

    if generate:

        if name:
            st.markdown(
                f'<div class="resume-name">{name}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="resume-name">Your Name</div>',
                unsafe_allow_html=True
            )

        contact = " • ".join(
            value for value in [email, phone, location] if value
        )

        if contact:
            st.markdown(
                f'<div class="resume-contact">{contact}</div>',
                unsafe_allow_html=True
            )

        if summary:
            st.markdown(
                '<div class="resume-heading">PROFESSIONAL SUMMARY</div>',
                unsafe_allow_html=True
            )
            st.write(summary)

        if education:
            st.markdown(
                '<div class="resume-heading">EDUCATION</div>',
                unsafe_allow_html=True
            )
            st.write(education)

        if skills:
            st.markdown(
                '<div class="resume-heading">SKILLS</div>',
                unsafe_allow_html=True
            )
            st.write(skills)

        if projects:
            st.markdown(
                '<div class="resume-heading">PROJECTS</div>',
                unsafe_allow_html=True
            )
            st.write(projects)

        if experience:
            st.markdown(
                '<div class="resume-heading">EXPERIENCE</div>',
                unsafe_allow_html=True
            )
            st.write(experience)

        st.success("Resume preview generated successfully.")

    else:

        st.markdown(
            """
            ### Your resume preview will appear here

            Fill in your information on the left and click
            **Generate Resume** to create your professional resume.
            """
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )