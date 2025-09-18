import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account 

creds = service_account.Credentials.from_service_account_file('cambiocredentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

client = gspread.authorize(creds)

# --- 2. Open the Google Sheet ---
sheet_id = "1-47SoINk-1zj6gj1Wq4cB3LVcxazqYEL4BuKW3kumrQ"  # Your Google Sheet ID

sheet = client.open_by_key(sheet_id)
worksheet = sheet.sheet1

data = worksheet.get_all_values()


# Streamlit App Configuration
st.set_page_config(layout="wide")
st.title("Entrepreneur Compass Tool")
st.write("Please fill out the survey below. Your responses will help us tailor future workshops and opportunities for you.")

full_name = ""
email = ""
phone_number = ""
age_group = ""
borough = ""
housing_status = ""
nycha_housing = ""
nycha_lease = ""
nycha_rent = ""
entrepreneurship_interest = ""
business_idea_status = ""
business_name = ""
business_description = ""
industries = ""
organization_type = ""
social_entrepreneurship_interest = ""
milestones = ""
venture_duration = ""
full_time = ""
team_size = ""
motivation = ""
career_paths = ""
cooperative_business = ""
annual_revenue = ""
quarter_revenue = ""
completed_programs = ""
accelerator_description = ""
funding_received = ""
cash_flow_positive = ""
profitable_year = ""
learning_experience = ""
language_preference = ""
preferred_languages = ""
business_support = ""
additional_resources = ""
gender = ""
military_status = ""
zip_code = ""
family_income = ""
personal_applicability = ""
ethnic_groups = ""
employment_status = ""
family_college_attendance = ""
virtual_training_devices = ""
barriers_to_participation = ""

# Initializing variables with default values
nycha_section8_resident = False
rent = False  
lease = False
brooklyn_resident = False  
female = False  
over_18 = False  
over_49 = False  
veteran = False  
black_identity = False  
past_idea_stage = False
operating = False  
registered = False  
rev = False  
rev_3mo_500 = False  
rev_yr_5000 = False 
tech = False  
makeup_fashion = False  
cannabis = False

# PAGE 1
full_name = st.text_input("What is your full name? *", "")
email = st.text_input("What is your email address? *", "")
phone_number = st.text_input("What is your phone number?", "")
age_group = st.radio("Which age group are you in? *", ["Less than 18", "18-24", "25-34", "35-49", "50-64", "65+"], index=0)
over_18 = age_group != "Less than 18"
over_49 = age_group in ["50-64", "65+"]
borough = st.radio("What borough of NYC do you live in? *", ["Manhattan", "Queens", "Brooklyn", "The Bronx", "Staten Island", "I don't live in NYC"], index=0)
brooklyn_resident = borough in ["Brooklyn"]
housing_status = st.radio("What is your housing status? *", ["I live in NYCHA public housing", "I am a Section 8 Voucher holder", "I don't live in NYCHA or am not a Section 8 voucher holder"], index=2)
nycha_section8_resident = housing_status in ["I live in NYCHA public housing", "I am a Section 8 Voucher holder"]
nycha_housing = st.text_input("If you live in NYCHA, what housing development or building do you live in? (If not applicable, enter N/A)", "")
nycha_lease = st.radio("If you live in NYCHA, is your name on the lease?", ["Yes", "No", "N/A"], index=2)
lease = nycha_lease in ["Yes"]
nycha_rent = st.radio("If you live in NYCHA, are you current with your payments?", ["Yes", "No", "N/A"], index=2)
rent = nycha_rent in ["Yes"]


entrepreneurship_interest = st.radio("What is your level of interest in entrepreneurship or being a business owner? *",["1 - Not interested","2","3","4","5 - Extremely interested"],index=3)
business_idea_status = st.radio("Have you come up with an idea for a business or venture that you would like to pursue? *",["I don't have an idea, and have no interest in starting a business or organization","I don't really have a clear idea, but I am generally interested in learning more about entrepreneurship or starting a business","I have a lot of ideas, but have not decided on one yet","Yes, I have a clear business or venture idea that I'd like to pursue","I am past the idea stage, and have already taken steps to launch my business"],index=1)

if business_idea_status == "I am past the idea stage, and have already taken steps to launch my business":
    past_idea_stage = True
    # New Business-Related Questions
    business_name = st.text_input("Do you have a name for your organization or company?", "")
    business_description = st.text_area("What kind of product or service do you want to offer to people? Please describe very briefly below.", "")
    industries = st.multiselect("Is your business focused on any of the following industries? Please check all that apply:", ["Fashion", "Beauty", "Childcare", "Catering", "Food & Beverage", "Construction", "Manufacturing or Industrial Production", "Technology", "Cannabis", "Other"])
    tech = any(i in industries for i in ["Technology"])
    cannabis = any(i in industries for i in ["Cannabis"])
    makeup_fashion = any(i in industries for i in ["Fashion", "Beauty"])
    organization_type = st.radio("What type of organization do you want to / have started?", ["For-profit: company with business owners and shareholders that can earn profits", "Non-profit: organization driven by a social mission, that can have employees but no private shareholders", "Cooperative: an organization that is somehow collectively managed and owned by workers or other community stakeholders", "Not sure what I want to set up yet", "I have multiple organizations with different structures", "Other"])
    social_entrepreneurship_interest = st.radio("What is your level of interest in social entrepreneurship (starting a business that can also have a social or environmental impact)?", ["1 - Not interested", "2", "3", "4", "5 - Extremely interested"], index=3)
    milestones = st.multiselect("Which of the following steps have you taken, or milestones have you reached in your business?", ["Created a website or landing page", "Created a prototype, or early version product or service", "Tested your product or service with real users or customers", "Charged money for your product or service (to someone that was NOT a family member or close friend)", "Created a pitch deck or slide show presentation for your venture", "Created a business plan, or written document describing your business and growth strategy", "Pitched your company to a live audience", "Legally registered your business or organization (i.e. set up an LLC, 501c3, etc.)", "Kept some sort of accounts or financial records (tracking how much money you have spent and earned)", "Received labor from volunteers", "Hired part-time or full-time staff", "Raised funding from investors", "Acquired grants to fund your operations", "Grown rapidly with a profitable model - ready for major investment and scale"])
    registered = any(i in milestones for i in ["Legally registered your business or organization (i.e. set up an LLC, 501c3, etc.)"])
    venture_duration = st.radio("If you are actively working on this business venture, how long have you been working on this for?", ["Less than a year", "1 - 2 years", "3 - 5 years", "5+ years"])
    operating = venture_duration != "Less than a year"
    full_time = st.radio("Are you pursuing this venture full time, i.e., is this venture your only source of income?", ["Yes", "No, I still make income through other means or jobs", "Other"])
    team_size = st.radio("How big is your team? Please use the 'Other' option to describe yourself if these options feel limiting.", ["It's just me", "I have 1-2 part-time employees besides myself", "I have 1-2 full-time employees besides myself", "I have more than 3 full-time people on my team", "Other"])
    motivation = st.multiselect("What is motivating you to pursue business training or own your own company? Please check all that apply", ["I just want to learn a lot more about business & entrepreneurship", "I want to leave my current job", "I want to make my side hustle my full-time gig", "I need to create more income for myself and/or for my family", "I want to be wealthy", "I want to make a difference in my community", "Other"])

    # Display definitions for career paths
    st.write("### Entrepreneurial Career Paths")
    st.write("**Intrapreneur:** You don't want to start your own company but have an innovative role within a bigger organization.")
    st.write("**Lifestyle Entrepreneur:** You want to start a small or lifestyle business to provide for yourself and your family. This could be a mom-and-pop shop, small local business, freelancing, or remote work.")
    st.write("**Social Entrepreneur:** You want to create an organization that doesn't just generate wealth but also has a social or environmental impact.")
    st.write("**VC Backed Entrepreneur:** You want to build something that grows rapidly, disrupts markets, and generates significant revenue and returns, requiring major investment and scaling.")

    career_paths = st.multiselect("Which of these career paths are you open to?",["Intrapreneur","Lifestyle Entrepreneur","Social Entrepreneur","VC Backed Entrepreneur"])
    cooperative_business = st.radio("What is your level of interest in cooperative business (starting a business that is owned by various community members that have votes and a share of profits)?",["1 - Not interested","2","3","4","5 - Extremely interested"],index=3)

    if "Charged money for your product or service (to someone that was NOT a family member or close friend)" in milestones:
        rev = True
        annual_revenue = st.radio("How much revenue have you generated in the past year?",["I have not generated any revenue in the past year", "Less than $5,000", "More than $5,000"])
        rev_yr_5000 = annual_revenue in ["More than $5,000"]
        quarter_revenue = st.radio("How much revenue have you generated in the past 3 months?",["I have not generated any revenue in the past 3 months", "Less than $500", "More than $500"])
        rev_3mo_500 = quarter_revenue in ["More than $500"]
        completed_programs = st.multiselect("Have you completed or graduated from any of the following programs before? Check all that apply",["REES Business Pathways Programs","NYC Boss Up","Start Small Think Big Workshops","Startup NYCHA by Cambio Labs","WIBO","Communitas America"])
        accelerator_description = st.text_area("Have you participated in other Accelerator Programs or Fellowship Programs before? If so, please briefly describe what types of accelerator programs or fellowships you have participated in.")
        funding_received = st.radio("Have you received external funding previously?",["No", "I have recieved Equity Investment(s)", "I have recieved Grants", "I have recieved Personal donations","I have recieved Loans"])
        cash_flow_positive = st.radio("Has your business or organization ever become cash flow positive (you are making more than you are spending at the end of the month)?",["Yes", "No", "Other"])
        profitable_year = st.radio("Has your company ever had a profitable year?",["Yes", "No", "Other"])

# PAGE 3
learning_experience = st.radio("What kind of learning experiences do you prefer?",["In person meetings","Virtual meetings (on computers)","A blend of both"])
language_preference = st.radio("Do you prefer to take classes in another language other than English?",["Yes", "No"])
preferred_languages = st.multiselect("If no, what language(s) would you prefer?",["Spanish","Arabic","Bengali","Chinese","French","Other"])

# Areas of business development support needed
business_support = st.multiselect("What areas of business development do you need the most support in right now? Please check up to 7 boxes reflecting your top needs",
    ["Website Development",
        "Technology or Software Development",
        "IT & Hardware Support",
        "Customer Discovery & Market Research",
        "Business Plan or Business Pitch Deck Development",
        "Financial Planning, Accounting & Projections",
        "Accessing Office Space",
        "Accessing Commercial Kitchen",
        "Marketing & Sales",
        "Press Releases & Media",
        "Business Formation or Legal Registration",
        "Other Legal Assistance",
        "Advice on negotiating your lease",
        "Getting WMBE (Minority/Women Owned Business Enterprise) Certification",
        "Accessing government contracts or procurement opportunities",
        "Political or government connections",
        "Human Resources, Training & Hiring",
        "Coaching & Mentoring",
        "Seed Capital or Grant Funding",
        "Investor or Angel Fundraising",
        "Business Loans",
        "Venture Capital Fundraising",
        "Scaling operations regionally or nationally",
        "Other"],max_selections=7)

# Additional resources or challenges
additional_resources = st.text_area("Do you have anything else to add about resources that can help you, or challenges that can stop you, from starting your own company?" )
gender = st.radio("What is your gender?",["Male","Female","Prefer to not say","Other"])
female = gender in ["Female"]
military_status = st.radio("Are you a veteran of the military, military spouse, or Gold Star Family member? *", ["Yes", "No"], index=1)
veteran = military_status in ["Yes"]
zip_code = st.text_input("Please list your zip code:")
family_income = st.radio("How would you describe your family's income level?",["Under $25,000","$25,001 - $50,000","$50,001 - $75,000","$75,001 - $100,000","$100,001 - $150,000","Over $150,000","Other"])
personal_applicability = st.multiselect("Please check any of the following that personally apply",["I am a resident of public or affordable housing (i.e., NYCHA)","I participate in a lunch voucher program at my school","I am aware that members of my family receive welfare or SNAP benefits","I am currently homeless and/or live in a shelter","My family immigrated to the United States within the past 3 generations","English is not my first language","None of these apply"])
ethnic_groups = st.multiselect("Which racial or ethnic groups do you identify with? (Check all that apply).",["African","African American / Black","Caribbean American","Hispanic/Latinx","American Indian/Alaskan Native","Native Hawaiian or Pacific Islander","Middle Eastern/North African","East Asian","South Asian","Southeast Asian","White","Prefer to self-describe"])
black_identity = any(group in ethnic_groups for group in ["African", "African American / Black", "Caribbean American"])
employment_status = st.radio("How would you describe your employment status?",["Employed (Full-time)","Self-Employed (Full-time)","Employed (Part-time)","Self-Employed (Part-time)","Unemployed"])
family_college_attendance = st.radio("Has anyone in your family attended college that you know of?",["Yes","No, I don't think so","I'm not sure"])
virtual_training_devices = st.multiselect("Do you have access to the following devices to complete virtual trainings? Check all that apply",["Smartphone","Laptop","I don't have a personal smartphone or laptop","I don't have access to stable internet","Other"])
barriers_to_participation = st.text_area("Do you have any major barriers to participating in entrepreneurship programs that you want to tell us about?")

# Submit button
if st.button("Submit"):
    # Convert multiselect lists to comma-separated strings
    industries = ", ".join(industries) if isinstance(industries, list) else ""
    milestones = ", ".join(milestones) if isinstance(milestones, list) else ""
    motivation = ", ".join(motivation) if isinstance(motivation, list) else ""
    career_paths = ", ".join(career_paths) if isinstance(career_paths, list) else ""
    completed_programs = ", ".join(completed_programs) if isinstance(completed_programs, list) else ""
    preferred_languages = ", ".join(preferred_languages) if isinstance(preferred_languages, list) else ""
    business_support = ", ".join(business_support) if isinstance(business_support, list) else ""
    personal_applicability = ", ".join(personal_applicability) if isinstance(personal_applicability, list) else ""
    ethnic_groups = ", ".join(ethnic_groups) if isinstance(ethnic_groups, list) else ""
    virtual_training_devices = ", ".join(virtual_training_devices) if isinstance(virtual_training_devices, list) else ""

    user_data = [
        full_name, email, phone_number, age_group, borough, housing_status, nycha_housing,
        nycha_lease, nycha_rent, entrepreneurship_interest, business_idea_status, business_name,
        business_description, industries, organization_type, social_entrepreneurship_interest,
        milestones, venture_duration, full_time, team_size, motivation, career_paths,
        cooperative_business, annual_revenue, quarter_revenue, completed_programs,
        accelerator_description, funding_received, cash_flow_positive, profitable_year,
        learning_experience, language_preference, preferred_languages, business_support,
        additional_resources, gender, military_status, zip_code, family_income,
        personal_applicability, ethnic_groups, employment_status, family_college_attendance,
        virtual_training_devices, barriers_to_participation
    ]
    worksheet.append_row(user_data)

    st.write("### Resources and Programs you are Eligible for:")
    

# Cambio Labs and REES Biz Dev and Boss up NYCHA
    if nycha_section8_resident == True:
        st.write("Cambio Labs NYCHA Startup Accelerator: https://www.cambiolabs.org/startupnycha")
        st.write("REES Business Development Resource: https://drive.google.com/file/d/13FNLMR2Pm7DUEf2fSTkHOvgcVjdiAiN9/view")

        if past_idea_stage == True: 
            st.write("REES Home-Based Business: https://opportunitynycha.org/business-development/home-based-business/")

        if over_18 == True and rent == True and lease == True:
            st.write("Boss Up NYCHA Competition: https://www.nycbossup.org/nycha-residents")

# Bossup Vet
    if veteran == True and over_18 == True and rent == True and lease == True:
        st.write("Boss Up Veteran Competition: https://www.nycbossup.org/veterans")

# SBS
    if female == True:
        st.write("FastTrac® NewVenture™ for the Female Entrepreneur: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

        if over_49 == True:
            st.write("FastTrac® NewVenture™ 50+: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

    if black_identity == True:
        st.write("BE NYC Startup Intensive: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

    if tech == True: 
        st.write("FastTrac® TechVenture™: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

    if cannabis == True: 
        st.write("FastTrac® for Cannabis Entrepreneurs - powered by Cannabis NYC: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

    if past_idea_stage == True and operating == True:
        st.write("FastTrac® GrowthVenture™: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

        if veteran == True:
            st.write("FastTrac® GrowthVenture™ for Veterans: https://nyc-business.nyc.gov/nycbusiness/business-services/education-programs/fasttrac")

# SSTB
    if past_idea_stage == True and rev_3mo_500 == True: 
        st.write("Start Small Think Big: https://www.startsmallthinkbig.org/")

# REES
    if past_idea_stage == True and registered == True and rev == False:
        st.write("REES Idealists: https://opportunitynycha.org/business-development/")

    if past_idea_stage == True and registered == False and rev == True:
        st.write("REES Underground Entrepreneurs: https://opportunitynycha.org/business-development/")
    
    if past_idea_stage == True and registered == True and rev_yr_5000 == False:
        st.write("REES Go-getters: https://opportunitynycha.org/business-development/")
    
    if past_idea_stage == True and registered == True and rev_yr_5000 == True:
        st.write("REES Champions: https://opportunitynycha.org/business-development/")

    if past_idea_stage == False:
        st.write("REES Dreamers: https://opportunitynycha.org/business-development/")
    
# BKPL
    if brooklyn_resident == True and over_18 == True:
        st.write("Brooklyn Public Library PowerUP Business Plan Competition: https://www.bklynlibrary.org/business/powerup")
        st.write("Brooklyn Public Library Cision Communications Resource: https://www.bklynlibrary.org/online-resources/cision-communications")


    st.write(" ### Additional Resources:")
    st.write("One-on-one coaching and mentorship: Brooklyn Public Library Ask a Librarian (https://www.bklynlibrary.org/bal)")
    st.write("General Entrepreneurship and Career Resources (and more!): Brooklyn Public Library Online Resources (https://www.bklynlibrary.org/online-resources)")
    st.write("Networking events and career advancement opportunities: Brooklyn Public Library Business & Career Center (https://www.bklynlibrary.org/locations/central/business-career-center)")
    st.write("For all aspiring entrepreneurs and small business owners: Brooklyn Public Library Small Business & Entrepreneur Services (https://www.bklynlibrary.org/business/small-business)")