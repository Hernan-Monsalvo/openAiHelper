#pip install openai
import openai
from config import API_KEY
from sys import exit


def AIHelper(command="say hello world on ten different languages", lenght=200, temperature=0.1):

    if "song" in command or "cancion" in command:
        temperature = 0.8 # raise "creativity" for songs

    openai.api_key = API_KEY
    response = openai.Completion.create(model="text-davinci-002", prompt=command, temperature=temperature, max_tokens=lenght)
    return response


if __name__ == "__main__":
    command = input("Command: ")
    try:
        lenght = int(input("output max lenght: "))
    except:
        print("error")
        exit()

    response = AIHelper(command, lenght)
    print(response["choices"][0]["text"])

    input=("press enter to exit")
    exit()