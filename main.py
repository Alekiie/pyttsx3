# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# def speak_text(text, rate=130, volume=1.0, voice_id=None):
#     engine.setProperty('rate', rate)
#     engine.setProperty('volume', volume)
#     if voice_id:
#         engine.setProperty('voice', voice_id)

#     engine.say(text)
#     engine.runAndWait()

# def list_voices():
#     voices = engine.getProperty('voices')
#     for idx, voice in enumerate(voices):
#         print(f"Voice {idx}: {voice.name}, ID: {voice.id}, Language: {voice.languages}")

# if __name__ == "__main__":
#     list_voices()
#     voice_index = int(input("Select a voice index to use (e.g., 0): "))
    
#     if voice_index < 0 or voice_index >= len(engine.getProperty('voices')):
#         print("Invalid voice index selected.")
#     else:
#         selected_voice_id = engine.getProperty('voices')[voice_index].id
#         speak_text("Hello, this is a test.", rate=120, voice_id=selected_voice_id)
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
                #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
                        #printing current volume level
engine.setProperty('volume',0.8)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say('My current speaking rate is correctly configured.' )
engine.runAndWait()
engine.stop()