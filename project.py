import openai

# Define your OpenAI API key
openai.api_key = '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'

# Function to interact with the user and collect responses
def interact():
    education_level = input("What is your current class or level of education? ")
    goal = input("What is your goal in life? ")
    location = input("Please provide your location (city/place/country): ")
    interests = input("Please specify your interests: ")
    gender = input("What is your gender (male/female)? ")

    return education_level, goal, location, interests, gender

# Function to generate response using the LLM
def generate_response(education_level, goal, location, interests, gender):
    prompt = f"After completing {education_level} grade, my goal in life is to {goal}. I live in {location}. My interests are {interests}. My gender is {gender}."
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Main function
def main():
    education_level, goal, location, interests, gender = interact()
    response = generate_response(education_level, goal, location, interests, gender)
    print("Chatbot Response:")
    print(response)

if __name__ == "__main__":
    main()
