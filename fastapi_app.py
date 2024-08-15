import uvicorn
import os

from openai import OpenAI
from fastapi import FastAPI
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)


def get_icd_codes(user_input):
    completion = client.chat.completions.create(
      model="ft:gpt-4o-mini-2024-07-18:xeven-solutions:icd10amft:9sptHxFn",
      messages=[
        {"role": "system", "content": "You are expert in providing ICD codes and description"},
        {"role": "user", "content": user_input}
      ]
    )
    response = completion.choices[0].message

    return response.content.replace('"', '')


app = FastAPI()


@app.get("/get_icd_codes_and_description")
def get_icd_codes_and_description(input: str):
    response = get_icd_codes(input)
    return {"message": response}


if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
