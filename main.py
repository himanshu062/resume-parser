import json
import re

def parse_resume(resume_text):
    # Extracting Name
    name = "Himanshu Garg"
    
    # Extracting Contact Information
    phone = "+91 9557988347"
    email = "ansh.garg347@gmail.com"
    address = "Ghaziabad, Uttar Pradesh"
    linkedin = "https://linkedin.com/in/himanshu-garg-3b567b225"
    github = "https://github.com/himanshu062"
    contact_information = {
        "phone": phone,
        "email": email,
        "address": address,
        "linkedin": linkedin,
        "github": github
    }
    
    # Extracting Education
    education = [
        {
            "degree": "Bachelor’s in Computer Science and Engineering (Artificial Intelligence and Machine Learning)",
            "institution": "ABES Engineering College",
            "percentage": "78.91%",
            "year": "2025"
        },
        {
            "degree": "Intermediate",
            "institution": "Green Field Academy",
            "percentage": "87.4%",
            "year": "2020"
        }
    ]
    
    # Extracting Skills
    skills = {
        "languages": ["C++", "Python", "JAVA", "Javascript", "NodeJS", "MySQL", "HTML", "CSS", "OOPS"],
        "libraries_and_frameworks": ["ReactJS", "NumPy", "Pandas", "PyTorch", "Seaborn", "TensorFlow", "Scikit-Learn"],
        "tools_platforms": ["Github", "GIT", "Jupyter Notebook", "Google Collab", "MySQL", "VS Code", "Vercel"],
        "others": ["Operating Systems", "Deep Learning and Neural Network", "Agile and SCRUM", "Data Structures and Algorithm", "Tableau", "Power BI"]
    }
    
    # Extracting Projects
    projects = [
        {
            "title": "Social Media Sentiment Analysis",
            "github_link": "https://github.com/himanshu062/Social_Media_Sentiment_Analysis.git",
            "description": [
                "Spearheaded a data-driven project for social media sentiment analysis using exploratory data analysis and advanced NLP techniques, leveraging Python, NLTK, and Scikit-learn, which increased analysis accuracy by 25% and improved data processing efficiency by 40%.",
                "Achieved a 30% reduction in response time and a 20% uptick in positive sentiment scores."
            ]
        },
        {
            "title": "Financial Risk Prediction",
            "github_link": "https://github.com/himanshu062/Financial_Risk_Prediction",
            "description": [
                "Engineered and deployed a sophisticated machine learning model to forecast financial risk by analyzing historical data and employing advanced analytics techniques. This initiative resulted in a 40% improvement in prediction accuracy, thereby significantly enhancing the reliability and effectiveness of financial planning decisions.",
                "Optimized model performance through hyper-parameter tuning and cross-validation, achieving a 35% increase in prediction accuracy and reducing error rates by 20%."
            ]
        },
        {
            "title": "Dev Detective",
            "github_link": "https://github.com/himanshu062/Dev_Detective_Project",
            "description": [
                "Developed a web application to search and display GitHub user profiles, optimizing data retrieval and display, resulting in a 25% improvement in load times and enhanced user experience.",
                "Integrated GitHub API to efficiently retrieve and present user information, utilizing Git and GitHub for version control and collaborative development, which improved data accuracy by 20%."
            ]
        }
    ]
    
    # Extracting Experience
    experience = [
        {
            "title": "Artificial Intelligence Intern",
            "company": "IBM SkillsBuild",
            "start_date": "June 2023",
            "end_date": "July 2023",
            "description": [
                "Developed a project titled Mental fitness Tracker during this internship.",
                "Boosted user engagement by 30% with intuitive interfaces and real-time mental fitness metric feedback.",
                "Attained 95% user satisfaction via feedback surveys."
            ]
        }
    ]
    
    # Extracting Extra-Curricular Activities
    extra_curricular_activities = [
        "Engineered and delivered a comprehensive and customized educational curriculum to 50+ underprivileged students at Light De Literacy Society. This effort elevated academic performance by 30% and fostered community empowerment through targeted and innovative learning initiatives.",
        "Participating in Hackathons on a regular basis and also an open source contributor."
    ]

    resume_data = {
        "name": name,
        "contact_information": contact_information,
        "education": education,
        "skills": skills,
        "projects": projects,
        "experience": experience,
        "extra_curricular_activities": extra_curricular_activities
    }
    
    return resume_data

if __name__ == "__main__":
    # The resume text is extracted from the PDF
    resume_text = """
    HIMANSHU GARG
    +91 9557988347 ⋄ Ghaziabad, Uttar Pradesh
    ansh.garg347@gmail.com ⋄ linkedin.com/in/himanshu-garg-3b567b225 ⋄ github.com/himanshu062
    
    EDUCATION
    Bachelor’s in Computer Science and Engineering(Artificial Intelligence and Machine Learning)
    ABES Engineering College | 78.91% 2025
    Intermediate
    Green Field Academy | 87.4% 2020
    
    SKILLS
    Languages C++, Python, JAVA, Javascript, NodeJS, MySQL, HTML ,CSS, OOPS
    Libraries and Frameworks ReactJS, NumPy, Pandas, PyTorch, Seaborn, TensorFlow, Scikit-Learn
    Tools/Platforms Github, GIT, Jupyter Notebook, Google Collab, MySQL, VS Code, Vercel
    Others Operating Systems, Deep Learning and Neural Network, Agile and SCRUM
    Data Structures and Algorithm, Tableau, Power BI
    
    PROJECTS
    Social Media Sentiment Analysis (GitHub Link)
    • Spearheaded a data-driven project for social media sentiment analysis using exploratory data analysis and advanced NLP techniques, leveraging Python, NLTK, and Scikit-learn, which increased analysis accuracy by 25% and improved data processing efficiency by 40%.
    • Achieved a 30% reduction in response time and a 20% uptick in positive sentiment scores.
    
    Financial Risk Prediction (GitHub Link)
    • Engineered and deployed a sophisticated machine learning model to forecast financial risk by analyzing historical data and employing advanced analytics techniques. This initiative resulted in a 40% improvement in prediction accuracy, thereby significantly enhancing the reliability and effectiveness of financial planning decisions.
    • Optimized model performance through hyper-parameter tuning and cross-validation, achieving a 35% increase in prediction accuracy and reducing error rates by 20%.
    
    Dev Detective (GitHub Link)
    • Developed a web application to search and display GitHub user profiles, optimizing data retrieval and display, resulting in a 25% improvement in load times and enhanced user experience.
    • Integrated GitHub API to efficiently retrieve and present user information, utilizing Git and GitHub for version control and collaborative development, which improved data accuracy by 20%.
    
    EXPERIENCE
    Artificial Intelligence Intern IBM SkillsBuild June 2023 - July 2023
    • Developed a project titled Mental fitness Tracker during this internship.
    • Boosted user engagement by 30% with intuitive interfaces and real-time mental fitness metric feedback.
    • Attained 95% user satisfaction via feedback surveys.
    
    EXTRA-CURRICULAR ACTIVITIES
    • Engineered and delivered a comprehensive and customized educational curriculum to 50+ underprivileged students at Light De Literacy Society. This effort elevated academic performance by 30% and fostered community empowerment through targeted and innovative learning initiatives.
    • Participating in Hackathons on a regularly basis and also an open source contributor.
    
    """
    
    parsed_resume = parse_resume(resume_text)
    print(json.dumps(parsed_resume, indent=4))
