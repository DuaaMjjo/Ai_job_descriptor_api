# 1. Library imports
from fastapi import FastAPI
from JobDescriptors import JobDescriptor
from fastapi.middleware.cors import CORSMiddleware

# 2. Create the app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def job_descriptor(company: str, job_title: str, job_type: str, location: str, experience: str):
    jd = JobDescriptor()
    # Run the chain only specifying the input variables.
    description = jd.my_chain.run({"name_of_company": company,
                                   "job_title": job_title,
                                   "job_type": job_type,
                                   "location": location,
                                   "year_of_experience": experience})

    return {
        'Job description': description,
    }
