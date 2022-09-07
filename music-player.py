import os
import pygame


# Prints opening message and initializes pygame mixer.
def initPlayer():
    print("", "Music Player by Dean & Aidan | Type 'help' for commands.",
          "Place mp3 files in the directory to be played.", "", sep="\n")
    pygame.mixer.init()
    cmds = ["help", "list", "play", "pause", "resume", "stop", "quit", "secret"]
    return cmds


# Scans music directory for mp3 files and adds them to the playlist.
def loadPlaylist():
    pl = [[], ["music/hidden/secret.mp3"]]
    for file in os.listdir("music"):
        if file.endswith(".mp3"):
            pl[0].append("music/" + file)
    return pl


# User inputs a command which is compared to the available commands and then returned.
def inputCmd(cmds):
    try:
        cmd = input("Command: ")
        if len(cmd) == 0:
            raise Exception("You did not enter anything.")
        if cmd.lower() not in cmds:
            raise Exception("You did not enter a valid command.")
    except KeyboardInterrupt:
        raise SystemExit
    except Exception:
        raise
    else:
        return cmd.lower()


# Used to select what song to play, user inputs a number and the number gets validated and returned.
def inputNum():
    try:
        num = input("Enter Song Number: ")
        if len(num) == 0:
            raise Exception("You did not enter anything.")
        num = int(num)
        if num <= 0:
            raise Exception("You did not enter a valid number.")
    except ValueError:
        raise Exception("You did not enter a number.")
    except KeyboardInterrupt:
        raise SystemExit
    except Exception:
        raise
    else:
        return num


# Depending on the command entered, preforms a task.
def processCmd(cmds, cmd, pl):
    if cmd == "help":
        cmdHelp(cmds)
    elif cmd == "list":
        cmdList(pl)
    elif cmd == "play":
        cmdPlay(pl, False)
    elif cmd == "pause":
        cmdPause()
    elif cmd == "resume":
        cmdResume()
    elif cmd == "stop":
        cmdStop()
    elif cmd == "quit":
        cmdQuit()
    elif cmd == "secret":
        cmdPlay(pl, True)


# Prints a list of available commands.
def cmdHelp(cmds):
    print("Available Commands:")
    print("\n".join(cmds[:-1]))


# Prints a list of available songs.
def cmdList(pl):
    if len(pl[0]) == 0:
        raise Exception("No songs available.")
    else:
        print("Available Songs:")
        for i in range(len(pl[0])):
            print(i + 1, str(pl[0][i]))


# Loads and plays the selected song.
def cmdPlay(pl, sec):
    if not pygame.mixer.music.get_busy():
        try:
            if sec:
                pygame.mixer.music.load(pl[1][0])
                print("It's a secret!")
            else:
                num = inputNum()
                pygame.mixer.music.load(pl[0][num - 1])
                print("Playing:", str(pl[0][num - 1])[6:len(pl[0][num - 1]) - 4])
            pygame.mixer.music.play()
        except IndexError:
            raise Exception("Song not found.")
        except Exception:
            raise
    else:
        raise Exception("Song already playing.")


# If a song is playing, pauses the song.
def cmdPause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        print("Song Paused.")
    else:
        raise Exception("No song to pause.")


# If a song is paused, resumes the song.
def cmdResume():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
        print("Song Resumed.")
    else:
        raise Exception("No song to resume.")


# If a song is playing, stops the song.
def cmdStop():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("Song Stopped.")
    else:
        raise Exception("No song to stop.")


# If the quit command is entered, exits program.
def cmdQuit():
    print("Thanks for using our music player!")
    raise SystemExit


# Brings everything together.
def main():
    cmds = initPlayer()
    pl = loadPlaylist()
    while True:
        try:
            cmd = inputCmd(cmds)
            processCmd(cmds, cmd, pl)
        except Exception as error:
            print(error)
        except SystemExit:
            break


main()
