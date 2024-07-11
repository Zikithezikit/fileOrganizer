# Imports
import os
import shutil



# File types

Music = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

Videos  = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

Images  = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

Documents = (".Documents",".pdf",".txt", ".xlsx",".pptx")


# Current directory
pwd = os.path.abspath(os.getcwd())



def main():
    # make directories
    try:
        if not os.path.exists(pwd+"/Music"):
            os.makedirs(pwd+"/Music")
        if not os.path.exists(pwd+"/Documents"):
            os.makedirs(pwd+"/Documents")
        if not os.path.exists(pwd+"/Images "):
            os.makedirs(pwd+"/Images ")
        if not os.path.exists(pwd+"/Videos "):
            os.makedirs(pwd+"/Videos ")
        if not os.path.exists(pwd+"/misc"):
            os.makedirs(pwd+"/misc")
    except: pass

    # Check every file in the listed directory 
    for file in os.listdir():

        # Organize the files
        try:
            if(file == "organizer.py"):
                pass
            elif(os.path.isdir(file)):
                pass
            elif(fileCategory(file) == "Music"):
                os.replace(pwd + "/" + file, pwd+"/Music/"+file)
            elif(fileCategory(file) == "Documents"):
                os.replace(pwd + "/" + file, pwd+"/Documents/"+file)
            elif(fileCategory(file) == "Images "):
                os.replace(pwd + "/" + file, pwd+"/Images /"+file)
            elif(fileCategory(file) == "Videos "):
                os.replace(pwd + "/" + file, pwd+"/Videos /"+file)
            else: 
                os.replace(pwd + "/" + file, pwd+"/misc/"+file)
        except:
            print("Error in organizing files")



# Find the category of file
def fileCategory(file):
    file_name, file_extension = os.path.splitext(pwd + "/" + file)
    if(file_extension in Music):
        return "Music"
    elif(file_extension in Videos ):
        return "Videos "
    elif(file_extension in Images ):
        return "Images "
    elif(file_extension in Documents):
        return "Documents"
    else: return "misc"




main()