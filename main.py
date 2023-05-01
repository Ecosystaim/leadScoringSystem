# Dependencies
import traceback
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import bz2file as bz2
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define possible origins of requests
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "https://stormsales.netlify.app/"
]

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Class to define API input / Prospect Data
class apiInput(BaseModel):
    lead_source: str
    country: str
    age: int
    gender: str
    education_level: str
    occupation: str
    industry: str
    income: int
    initial_response: str
    do_not_contact: str
    total_calls_attended: int
    total_meetings_attended: int
    general_knowledge: str
    business_knowledge: str
    company_size: str
    company_estimated_revenue: int
    lead_quality: str


leads_categorical_columns = ['lead_source',
                             'country',
                             'gender',
                             'education_level',
                             'occupation',
                             'industry',
                             'initial_response',
                             'do_not_contact',
                             'general_knowledge',
                             'business_knowledge',
                             'company_size',
                             'lead_quality']

leads_numeric_columns = ['age',
                         'income',
                         'total_calls_attended',
                         'total_meetings_attended',
                         'company_estimated_revenue', ]

leads_response_columns = ['lead_score']

cols = ['age', 'income', 'total_calls_attended', 'total_meetings_attended',
        'company_estimated_revenue', 'lead_source_inbound',
        'lead_source_organic', 'lead_source_other', 'lead_source_paid',
        'lead_source_referral', 'country_australia', 'country_brazil',
        'country_canada', 'country_china', 'country_france', 'country_germany',
        'country_india', 'country_japan', 'country_pakistan', 'country_uk',
        'country_usa', 'gender_female', 'gender_male', 'gender_other',
        'education_level_bachelor', 'education_level_college',
        'education_level_high school', 'education_level_master',
        'education_level_phd', 'occupation_businessman', 'occupation_employee',
        'occupation_other', 'occupation_retired', 'occupation_self-employed',
        'occupation_unemployed', 'industry_finance', 'industry_healthcare',
        'industry_manufacturing', 'industry_retail', 'industry_services',
        'industry_technology', 'initial_response_negative',
        'initial_response_neutral', 'initial_response_positive',
        'do_not_contact_no', 'do_not_contact_yes', 'general_knowledge_advanced',
        'general_knowledge_basic', 'general_knowledge_expert',
        'general_knowledge_intermediate', 'general_knowledge_novice',
        'business_knowledge_advanced', 'business_knowledge_basic',
        'business_knowledge_expert', 'business_knowledge_intermediate',
        'business_knowledge_novice', 'company_size_large',
        'company_size_medium', 'company_size_small', 'lead_quality_cold',
        'lead_quality_hot', 'lead_quality_warm']


def pre_process_leads_data(df, fitted_scaler, ):
    # create new df with selected columns
    df[leads_categorical_columns] = df[leads_categorical_columns].apply(lambda x: x.str.lower())
    df = pd.get_dummies(df)

    _df = pd.DataFrame(columns=cols)
    _df = pd.concat([_df, df], axis=0, ignore_index=True, sort=False)

    empty_cols = _df.columns[_df.isnull().any()]
    _df[empty_cols] = _df[empty_cols].fillna(False)

    _df[leads_numeric_columns] = fitted_scaler.transform(_df[leads_numeric_columns])

    return _df


# with open('./Models/model.pkl', 'rb') as f:
#    model = pickle.load(f)

model = bz2.BZ2File('./Models/model2.pbz2', 'rb')
model = joblib.load(model)

with open('./Models/scaler2.joblib', 'rb') as f:
    scaler = joblib.load(f)


@app.post('/')
async def calcscore(item: apiInput):
    try:
        df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())

        df_clean = pre_process_leads_data(df=df, fitted_scaler=scaler)

        yhat = model.predict(df_clean)

        return {"Lead_Score": int(yhat)}
    except Exception as e:
        errmsg = traceback.format_exception()
        return {"error": errmsg}
