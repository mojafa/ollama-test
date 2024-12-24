#import openai
import openai

#You can change the model here
MODEL_NAME = "phi3:mini"

#Model Client Set up
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

#Set context of the conversation
messages = [
    {"role": "system", "content": "You are a chat assistant that helps people with their questions."},
]

while True:
    question = input("\nYour question: ")
    print("Sending question...")

    messages.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=1,
        max_tokens=400
    )
    bot_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_response})

    print("Answer: ")
    print(bot_response)