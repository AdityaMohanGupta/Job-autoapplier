# Auto Job Applier for LinkedIn


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience?
years_of_experience = "1"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"
'''
NOTE: You're applying globally with no location restriction. "No" is correct for jobs within India,
but WRONG for onshore roles outside India (US/UK/EU etc.) where you as an Indian citizen would need sponsorship.
Change to "Yes" if you're mainly targeting international roles.
'''

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = ""                        # TODO: Add your real GitHub URL, e.g. "https://github.com/your-username"

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/aditya-mohan-gupta-768b28259/"       # TODO: Add your real LinkedIn URL, e.g. "https://www.linkedin.com/in/your-handle"

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen seeking work authorization"           # TODO: Only relevant for US-based applications; adjust based on target country



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 800000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 510000            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Associate Software Engineer @ Consat Orahi | Java, Spring Boot, Python, React.js, GenAI/LLM" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Software Engineer with 10 months of experience building production-grade, cloud-native systems at Consat Orahi.
Skilled in Java, Spring Boot (WebFlux), Python, React.js, Kafka, Redis, gRPC, Docker, and Kubernetes. Built
GenAI-powered applications with RAG/LLM integration and MCP server frameworks using FastMCP. Strong foundation
in DSA and distributed systems, with a LeetCode rating of 1730 and Codeforces rating of 1168.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
'''

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I'm Aditya Mohan Gupta, an Associate Software Engineer at Consat Orahi with 10 months of experience building
production-grade, cloud-native systems using Java, Spring Boot (WebFlux), Python, React.js, Kafka, Redis, gRPC,
Docker, and Kubernetes. I've worked on event-driven microservices handling 100k+ operations/day, and built a
GenAI/LLM agent framework (KAI) with an MCP server exposing enterprise integrations.

I'm excited about the opportunity to bring this experience to your team and would welcome the chance to discuss
how I can contribute.

Best regards,
Aditya Mohan Gupta
"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc.
user_information_all ="""
Name: Aditya Mohan Gupta
Location: Gurugram, India
Education: B.Tech, GLA University, Mathura (Aug 2022 - May 2026), CPI 8.31

Experience:
- Consat Orahi, Associate Software Engineer (Nov 2025 - Present)
  - Project: Airlinq eSIM Fleet Orchestrator - cloud-native eSIM lifecycle management for IoT vehicle fleets,
    event-driven microservices with Kafka (100k+ ops/day), gRPC-based Business Rule Engine (<500ms), Redis
    state caching, audit-first RBAC architecture. Stack: Java 21, Spring Boot WebFlux, gRPC, Kafka, Redis,
    PostgreSQL, Keycloak, Docker, Kubernetes.
  - Project: KAI - LLM Agent & MCP Server Framework - core MCP server using FastMCP exposing GitLab/Jira/Outlook/
    Neo4j tools to LLM agents, multi-tenant RBAC on Keycloak, React.js Connectors module with OAuth2/PAT
    integrations. Stack: Python, FastAPI, FastMCP, AutoGen, React.js, Keycloak, PostgreSQL, Docker, Kubernetes.
- Ticket Boleto (Personal Project, Oct 2024 - Feb 2025): real-time ticket booking website with concurrency
  handling, JWT + Google OAuth, secure payment gateway. Stack: MongoDB, Express, Node.js, React.js.

Skills: Java, Python, JavaScript, C, Spring Boot, gRPC, REST APIs, Node.js, Express.js, FastMCP, React.js,
RAG, LLM Integration, Prompt Engineering, Vector Databases, MCP, PostgreSQL, MySQL, MongoDB, Redis, Kafka,
Keycloak, OAuth2, JWT, RBAC, Docker, Kubernetes, Jenkins, Git.

Achievements: LeetCode rating 1730, Codeforces rating 1168, solved 800+ DSA questions across platforms,
HackerRank 5-Star in C, Python and Java.
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
'''

# Name of your most recent employer
recent_employer = "Consat Orahi" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False        # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive
