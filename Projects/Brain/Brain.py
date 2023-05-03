# Api Key
fileopen = open("I:\\Projects\\Modules\\Api.txt","r")
API = fileopen.read()
fileopen.close()

# Importing
import openai
from dotenv import load_dotenv

#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    FileLog = open("I:\\Projects\Logs\\chat_log.txt","r", encoding="utf-8", errors="replace")
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nRapheal : '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 20,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_template_Update = chat_log_template + f"\nYou : {question} \nRaphael : {answer}"
    FileLog = open("I:\\Projects\Logs\\chat_log.txt" ,"w", encoding="utf-8",errors="replace")
    FileLog.write(chat_log_template_Update)
    FileLog.close()
    return answer

