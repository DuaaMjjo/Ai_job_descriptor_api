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
@app.post('/')
def job_descriptor(company: str, position: str, exp: str):
    jd = JobDescriptor()
    # Run the chain only specifying the input variables.
    description = jd.my_chain.run({"name_of_company": company, "job_Position": position, "year_of_experience": exp})

    return {
        'Job description': description,
    }
