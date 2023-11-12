import os
import speech_recognition as sr

def create_note():
  
  note = input("Enter your note: ")
  
  with open("notes.txt", "a") as f:
    f.write(note + "\n")
  print("Note saved successfully!")

def edit_note():
  
  line_number = int(input("Enter the line number of the note you want to edit: "))
  
  with open("notes.txt", "r") as f:
    lines = f.readlines()
  
  if line_number > 0 and line_number <= len(lines):
    
    new_note = input("Enter the new note: ")
    
    lines[line_number - 1] = new_note + "\n"
    
    with open("notes.txt", "w") as f:
      f.writelines(lines)
    print("Note updated successfully!")
  else:
    print("Invalid line number!")

def record_note():
  r = sr.Recognizer()
  print("Start speaking now:")
  with sr.Microphone() as source:
    audio = r.listen(source)
    try:
      # recognize the spoken text
      text = r.recognize_google(audio)
      # write the note to a file
      with open("notes.txt", "a") as f:
        f.write(text + "\n")
        print("Note saved successfully!")
    except sr.UnknownValueError:
      print("Could not recognize your voice. Please try again.")
    except sr.RequestError as e:
      print("Error connecting to the server: {0}".format(e))

def main():

    print("1. Create a new note")
    print("2. Edit an existing note")
    print("3. Record a note using your device's microphone")
    print("4. Exit")


    option = int(input("Enter your option: "))

    if option == 1:
        create_note()
    elif option == 2:
        edit_note()
    elif option == 3:
        record_note()
    elif option == 4:
        exit()
    else:
        print("Invalid option! Please try again.")

if not os.path.exists("notes.txt"):
    with open("notes.txt", "w"):
        pass

while True:
    main()