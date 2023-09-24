import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

os.environ.get("OPENAI_API_KEY")

class JobDescriptor:
    llm = OpenAI(model_name='text-davinci-003',
                 temperature=0.9,
                 max_tokens=4000)

    # @title Prompt Templat
    job_description_template = """
    I want you to act as a writer. write about job description.

    format the output like the following:

    Job Title: {job_title}

    Company: {name_of_company}

    Job Type: {job_type}

    Location: {location}

    Experience: {year_of_experience}

    then Return job description with Responsibilities and Qualifications.

    """

    prompt_template = PromptTemplate(
        input_variables=["name_of_company", "job_title", "job_type", "location", "year_of_experience"],
        template=job_description_template,
    )
    
    # querying the model with the prompt template
    my_chain = LLMChain(llm=llm, prompt=prompt_template)

