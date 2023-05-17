import os
import shutil
from pathlib import Path

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

zip = (".zip", ".rar")

xml = (".xml", ".xmls")

spreadsheets = (".csv", ".xlsx")

document = (".pdf", ".txt", ".doc", ".docx", ".pptx")

executable = (".exe", ".msi")


def is_audio(file):
    return os.path.splitext(file)[1] in audio


def is_video(file):
    return os.path.splitext(file)[1] in video


def is_image(file):
    return os.path.splitext(file)[1] in img


def is_zipped(file):
    return os.path.splitext(file)[1] in zip


def is_xml(file):
    return os.path.splitext(file)[1] in xml


def is_spreadsheets(file):
    return os.path.splitext(file)[1] in spreadsheets


def is_document(file):
    return os.path.splitext(file)[1] in document


def is_executable(file):
    return os.path.splitext(file)[1] in executable


def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()


os.chdir("C:/Users/Orucho Onsare/Downloads")

for file in os.listdir():
    print(file)
    if is_audio(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/audio"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/New/audio")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/audio")
    elif is_video(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/video"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/video")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/video")
    elif is_zipped(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/Zipped"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/Zipped")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/Zipped")
    elif is_xml(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/XML Files/"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/XML FIles/")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/XML Files/")
    elif is_spreadsheets(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/SpreadSheets"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/Spreadsheets")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/Spreadsheets")
    elif is_document(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/Documents/"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/Documents/")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/Documents/")
    elif is_executable(file):
        if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/Programs/"):
            os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/Programs/")
        shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/Programs/")

    elif is_image(file):
        if is_screenshot(file):
            if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/Screenshots"):
                os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/Screenshots")
            shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/screenshots")
        else:
            if not os.path.exists("C:/Users/Orucho Onsare/Downloads/Newp/Images"):
                os.mkdir("C:/Users/Orucho Onsare/Downloads/Newp/Images")
            shutil.move(file, "C:/Users/Orucho Onsare/Downloads/Newp/Images")
