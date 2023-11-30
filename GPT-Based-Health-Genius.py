import openai
import json

# Function to make HTTP request to OpenAI API
def make_openai_request(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Function to calculate BMI
def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height * height)
    print(f'Your BMI is: {bmi}')
    return bmi

# Function to provide health advice using OpenAI
def health_advice(api_key, bmi):
    prompt = f"Provide health advice based on BMI {bmi}"
    response = make_openai_request(prompt, api_key)
    print(f'\nHealth Advice: {response}')

# Function to Set Goal using OpenAI
def set_goal(api_key, bmi):
    prompt = f"Suggest a fitness goal based on BMI {bmi}"
    response = make_openai_request(prompt, api_key)
    print(f'\nFitness Goal: {response}')

def diet_plan(api_key, bmi):
    prompt = f"Suggest a Diet Plan of 3 meals based on BMI {bmi}"
    response = make_openai_request(prompt, api_key)
    print(f'\nDiet Plan: {response}')

if __name__ == "__main__":
    api_key = "YOUR API KEY"
    bmi = 0

    while True:
        # Menu
        print("\n*****\tHealth Care System\t*****\n")
        print("1- Calculate BMI ")
        print("2- Get health advice ")
        print("3- Set a Goal ")
        print("4- Create a diet plan ")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            bmi = calculate_bmi()
        elif choice == 2:
            health_advice(api_key, bmi)
            print("Writing Health Advice....")
        elif choice == 3:
            set_goal(api_key, bmi)
            print("Setting a Goal....")
        elif choice == 4:
            print("Creating a diet plan....")
            diet_plan(api_key, bmi)
        else:
            print("Wrong Input.")