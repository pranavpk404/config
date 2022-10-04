from os import system

wallpaper = {
    "nord": "https://github.com/midnitefox/Nord-Theme-Ports-and-Assets",
    "gruvbox": "https://gitlab.com/exorcist365/wallpapers/",
    "dracula": "https://github.com/dracula/wallpaper/",
    "catppuccin": "https://github.com/catppuccin/wallpapers",
    "rose_pine": "https://github.com/rose-pine/wallpapers",
    "ayu": "https://github.com/catppuccin/wallpapers",
}


def install_aur_programs():
    system("git clone https://aur.archlinux.org/yay.git")
    system("cd yay/ && makepkg -si")
    system("yay -S python-pywalfox tor-browser onlyoffice-bin")


def setup_pywall():
    system("cp -r pywal/* ~/.config/")
    system("mkdir $HOME/.local/share/fonts")
    system("cp -r global/fonts/* $HOME/.local/share/fonts")
    system("cp -r global/flameshot ~/.config/")
    system("git clone https://github.com/pranavpk404/wallpapers $HOME/Pictures/wallpapers --depth=1")


def config_system():
    theme_input = input(
        "For Catppuccin:1 | For Gruvbox:2 | For Nord:3 | For Rose Pine:4 | For Dracula:5 | For Ayu:6 || Default is Ayu\n")
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
    else:
        theme = "ayu"
     
    system("mkdir $HOME/.local/share/fonts")
    system("cp -r global/fonts/* $HOME/.local/share/fonts")
    system("cp -r global/bspwm ~/.config/")
    
    system("cp -r global/flameshot ~/.config/")
    system("cp -r global/i3 ~/.config/") 
    system(f"cp -r themes/{theme}/* $HOME/.config/")
    system(f"cp -r themes/{theme}/{theme}.rasi $HOME/")

    # Wallpaper
    print("Please wait while we download the wallpaper")
    system(f"git clone {wallpaper[theme]} $HOME/Pictures/wallpapers")
    print("config done")


def shell():
    zsh_or_fish = input("For zsh:1 | For fish:2\n")
    if zsh_or_fish == "1":
        print("You will need to rerun the script with line 56 commented to install zsh-plugins it is a known bug")
        system(
            "sh -c \"$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"")
        system("cp -r global/.zshrc $HOME/")
        system(
            "git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting")
        system(
            "git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
        system(
            "git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions")
        print("please run \"sudo pacman -Rns fish\" if not using fish")
        print("zsh done")

    elif zsh_or_fish == "2":
        system("cp -r global/fish/ $HOME/.config")
        print("please run \"sudo pacman -Rns zsh\" if not using zsh")
        print("fish done")


user_input = input(
    "For Aur Programs:1 | For config:2 | For shell:3 | For Pywal:4 \n")

if user_input == "1":
    install_aur_programs()
elif user_input == "2":
    config_system()
elif user_input == "3":
    shell()
elif user_input == "4":
    setup_pywall()

else:
    print("Please enter correct option")
