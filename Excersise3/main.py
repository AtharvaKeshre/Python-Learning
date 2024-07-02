import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

lst = ["Atharva", "Amisha"]

for i in lst:
    s = f"Shoutout to {i}"
    speaker.Speak(s) 

