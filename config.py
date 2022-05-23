from os import system

system("git clone https://aur.archlinux.org/yay.git")
system("cd yay")
system("makepkg -si")
system("yay -S visual-studio-code-bin brave-bin pfetch mongodb-bin mongodb-tools-bin mongosh-bin mongodb-compass")


# Config
theme_input = input("For Catppuccin:1 | For Gruvbox:2 | For Nord:3 | For Rose Pine:4 | For Dracula:5 | For Ayu:6\n")

if theme_input == "1":
    theme = "catppuccin"
elif theme_input == "2":
    theme = "gruvbox"
elif theme_input == "3":
    theme = "nord"
elif theme_input == "4":
    theme = "rose_pine"
elif theme_input == "5":
    theme = "dracula"
elif theme_input == "6":
    theme = "ayu"

system(f"cp -r {theme}/* /home/pranav/.config/")
system("mkdir /home/pranav/.local/share/fonts")
system("cp -r fonts/* /home/pranav/.local/share/fonts")
system("cp -r fish/ /home/pranav/.config")
print("config done")
