from tkinter import *
import tkinter as tk
from transformers import AutoModelWithLMHead, AutoTokenizer
from transformers import pipeline
import threading

'App initialization, title etc'
app = Tk()
app.title("Machine Translation [German to English]")
app.geometry('1200x600')

app.configure(padx = 20, pady = 40,background='#f0f0f0')

'Add GUI elements'
'1. Add a text box'
inputText = tk.Text(app, height=10, width=600)
inputText.pack()
#Default text
inputText.insert(tk.END, "Enter German text for translation")

translatedOutput = ""

'2. Add a button'
def translateFromDEtoEn(inputText):
    # German to English translation
    global translatedOutput

    #Load the pre-trained german to english model
    model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-de-en")
    #Tokenizer is needed to prepare input for the model
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-de-en")

    translationArchitecture = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)

    input = inputText.get("1.0", END)
    # print(input)

    #Max input length of Helsinki is 512
    translatedOutput = translationArchitecture(input,max_length = 600)

    # print(translatedOutput[0])

    # print(translatedOutput[0]['translation_text'])

    '3. Add an output box'
    translatedText = tk.Text(app, height=10, width=600)
    translatedText.pack()
    # Default text
    translatedText.insert(tk.END, translatedOutput[0]['translation_text'])
    # return translatedOutput

# def callTranslate():


'Start a thread'
thread = threading.Thread(name="first_thread", target=Button(app, text = "Translate", command = lambda: translateFromDEtoEn(inputText), bg='#14639e').pack())
thread.start()

app.mainloop()
