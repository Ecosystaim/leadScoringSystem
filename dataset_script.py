import csv
import random

# Feature values for Good Leads
lead_sources_g = ['REFERRAL', 'PAID', 'INBOUND']
countries_g = ['USA', 'Canada', 'UK', 'Australia', 'Japan', ]
ages_g = list(range(35, 60))
genders_g = ['MALE', 'FEMALE', 'OTHER']
education_levels_g = ['HIGH SCHOOL', 'COLLEGE', 'BACHELOR']
occupations_g = ['SELF-EMPLOYED', 'BUSINESSMAN', 'RETIRED']
industries_g = ['SERVICES', 'RETAIL', 'MANUFACTURING']
incomes_g = list(range(100000, 200000, 1000))
initial_responses_g = ['POSITIVE', 'NEUTRAL']
do_not_contacts_g = 'No'
total_calls_attended_g = list(range(3, 8))
total_meetings_attended_g = list(range(2, 4))
general_knowledge_g = ['NOVICE', 'INTERMEDIATE', 'ADVANCED']
business_knowledge_g = ['NOVICE', 'INTERMEDIATE', 'ADVANCED']
company_sizes_g = ['MEDIUM', 'LARGE']
company_estimated_revenues_g = list(range(1000000, 10000000, 1000))
lead_qualities_g = ['HOT', 'WARM']
lead_scores_g = list(range(75, 100))

# Feature values for MID Leads
lead_sources_m = ['PAID', 'OTHER']
countries_m = ['USA', 'Canada', 'UK', 'Australia', 'Japan', ]
ages_m = list(range(35, 45))
genders_m = ['MALE', 'FEMALE', 'OTHER']
education_levels_m = ['COLLEGE', 'MASTER', 'PhD']
occupations_m = ['EMPLOYEE', 'UNEMPLOYED']
industries_m = ['SERVICES', 'RETAIL', 'MANUFACTURING']
incomes_m = list(range(80000, 100000, 1000))
initial_responses_m = ['POSITIVE', 'NEUTRAL']
do_not_contacts_m = 'No'
total_calls_attended_m = list(range(3, 5))
total_meetings_attended_m = list(range(2, 3))
general_knowledge_m = ['NOVICE', 'INTERMEDIATE', 'ADVANCED']
business_knowledge_m = ['NOVICE', 'INTERMEDIATE', 'ADVANCED']
company_sizes_m = ['MEDIUM']
company_estimated_revenues_m = list(range(1000000, 10000000, 1000))
lead_qualities_m = ['HOT', 'WARM']
lead_scores_m = list(range(50, 75))

# Feature values for Bad Leads
lead_sources_b = ['REFERRAL', 'ORGANIC', 'PAID', 'OTHER']
countries_b = ['India', 'Pakistan', 'Brazil', 'China', 'Germany', 'France']
ages_b = list(range(18, 40))
genders_b = ['MALE', 'FEMALE', 'OTHER']
education_levels_b = ['BACHELOR', 'MASTER', 'PhD']
occupations_b = ['EMPLOYEE', 'UNEMPLOYED', 'BUSINESSMAN', 'OTHER']
industries_b = ['FINANCE', 'TECHNOLOGY', 'HEALTHCARE']
incomes_b = list(range(20000, 100000, 1000))
initial_responses_b = ['NEGATIVE', 'NEUTRAL']
do_not_contacts_b = ['Yes', 'No']
total_calls_attended_b = list(range(1, 3))
total_meetings_attended_b = list(range(0, 1))
general_knowledge_b = ['NOVICE', 'BASIC', 'EXPERT']
business_knowledge_b = ['NOVICE', 'BASIC', 'EXPERT']
company_sizes_b = ['MEDIUM', 'SMALL']
company_estimated_revenues_b = list(range(100000, 1000000, 1000))
lead_qualities_b = 'COLD'
lead_scores_b = list(range(10, 45))

# Generate 5,000 records with random values for good scores
leads = []
for i in range(5000):
    lead = [
        random.choice(lead_sources_g),
        random.choice(countries_g),
        random.choice(ages_g),
        random.choice(genders_g),
        random.choice(education_levels_g),
        random.choice(occupations_g),
        random.choice(industries_g),
        random.choice(incomes_g),
        random.choice(initial_responses_g),
        do_not_contacts_g,
        random.choice(total_calls_attended_g),
        random.choice(total_meetings_attended_g),
        random.choice(general_knowledge_g),
        random.choice(business_knowledge_g),
        random.choice(company_sizes_g),
        random.choice(company_estimated_revenues_g),
        random.choice(lead_qualities_g),
        random.choice(lead_scores_g),
    ]
    leads.append(lead)

# Generate 2,500 records with random values for mid scores
for i in range(1500):
    lead = [
        random.choice(lead_sources_m),
        random.choice(countries_m),
        random.choice(ages_m),
        random.choice(genders_m),
        random.choice(education_levels_m),
        random.choice(occupations_m),
        random.choice(industries_m),
        random.choice(incomes_m),
        random.choice(initial_responses_m),
        do_not_contacts_m,
        random.choice(total_calls_attended_m),
        random.choice(total_meetings_attended_m),
        random.choice(general_knowledge_m),
        random.choice(business_knowledge_m),
        random.choice(company_sizes_m),
        random.choice(company_estimated_revenues_m),
        random.choice(lead_qualities_m),
        random.choice(lead_scores_m),
    ]
    leads.append(lead)

# Generate 2,500 records with random values for low scores
for i in range(5000):
    lead = [
        random.choice(lead_sources_b),
        random.choice(countries_b),
        random.choice(ages_b),
        random.choice(genders_b),
        random.choice(education_levels_b),
        random.choice(occupations_b),
        random.choice(industries_b),
        random.choice(incomes_b),
        random.choice(initial_responses_b),
        random.choice(do_not_contacts_b),
        random.choice(total_calls_attended_b),
        random.choice(total_meetings_attended_b),
        random.choice(general_knowledge_b),
        random.choice(business_knowledge_b),
        random.choice(company_sizes_b),
        random.choice(company_estimated_revenues_b),
        lead_qualities_b,
        random.choice(lead_scores_b),
    ]
    leads.append(lead)

for i in range(10000):
    if leads[i][17] > 85:
        leads[i][8] = 'POSITIVE'
        leads[i][16] = 'HOT'
    if leads[i][17] < 50:
        leads[i][16] = 'COLD'
    if leads[i][17] <= 30:
        leads[i][8] = 'NEGATIVE'
        leads[i][9] = 'Yes'

# Write the leads to a CSV file
with open('Datasets/synthetic_leads.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'Lead_Source',
        'Country',
        'Age',
        'Gender',
        'Education_Level',
        'Occupation',
        'Industry',
        'Income',
        'Initial_Response',
        'Do_Not_Contact',
        'Total_Calls_Attended',
        'Total_Meetings_Attended',
        'General_Knowledge',
        'Business_Knowledge',
        'Company_Size',
        'Company_Estimated_Revenue',
        'Lead_Quality',
        'Lead_Score',
    ])
    for lead in leads:
        writer.writerow(lead)


