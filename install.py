from os import system


# Config
theme_input = input("Which theme for catppuccin: 1 for gruvbox: 2 for nord: 3 \n")

if theme_input == "1":
    theme = "catppuccin"
elif theme_input == "2":
    theme = "gruvbox"
elif theme_input == "3":
    theme = "nord"

system(f"cp -r {theme}/* /home/pranav/.config/")
system("mkdir /home/pranav/.local/share/fonts")
system("cp -r fonts/* /home/pranav/.local/share/fonts")
print("config done")
