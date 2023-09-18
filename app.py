# 1. Library imports
from fastapi import FastAPI
from JobDescriptors import JobDescriptor

# 2. Create the app object
app = FastAPI()


# 3. update scores from the passed description
@app.post('/')
def job_descriptor(company: str, position: str, exp: str):
    jd = JobDescriptor()
    # Run the chain only specifying the input variables.
    description = jd.my_chain.run({"name_of_company": company, "job_Position": position, "year_of_experience": exp})

    return {
        'Job description': description,
    }
