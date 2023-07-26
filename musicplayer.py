import os
from pygame import mixer

def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def main():
    while True:
        print("1. Play Music")
        print("2. Stop Music")
        print("3. Pause Music")
        print("4. Resume Music")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = "C:/Users/narasimha/Desktop/Thunder-ImagineDragons_128-(DJMaza).mp3"
            if os.path.exists(file_path):
                print("hai")
                play_music(file_path)
            else:
                print("File not found!")

        elif choice == '2':
            stop_music()

        elif choice == '3':
            pause_music()

        elif choice == '4':
            resume_music()

        elif choice == '5':
            stop_music()
            break

        else:
            print("Invalid choice. Please try again.")
            break

main()