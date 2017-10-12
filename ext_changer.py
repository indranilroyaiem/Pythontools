import os, sys
def extchanger():

    for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    base_file, ext = os.path.splitext(filename)
    if ext == "source_extension(ex: .txt)":
    os.rename(filename, base_file + "desired_extension(ex:html)")

extchanger()