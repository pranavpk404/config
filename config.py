from os import system
system("git clone https://aur.archlinux.org/yay.git")
system("cd yay")
system("makepkg -si")
system("yay -S visual-studio-code-bin brave-bin pfetch mongodb mongodb-tools mongodb-compass protonvpn")

# Fish
system("""
set -l _tide_tmp_dir (command mktemp -d)
curl https://codeload.github.com/ilancosman/tide/tar.gz/v5 | tar -xzC $_tide_tmp_dir
command cp -R $_tide_tmp_dir/*/{completions,conf.d,functions} $__fish_config_dir
exec fish --init-command "set -g fish_greeting; emit _tide_init_install"
""")
system("cp -r fish/ ~/config/")

# Config
theme_input = input("For Catppuccin:1 | For Gruvbox:2 | For Nord:3 | For Rose Pine:4 \n")

if theme_input == "1":
    theme = "catppuccin"
elif theme_input == "2":
    theme = "gruvbox"
elif theme_input == "3":
    theme = "nord"
elif theme_input == "4":
    theme = "rose_pine"


system(f"cp -r {theme}/* /home/pranav/.config/")
system("mkdir /home/pranav/.local/share/fonts")
system("cp -r fonts/* /home/pranav/.local/share/fonts")
print("config done")