from os import system
system("git clone https://aur.archlinux.org/yay.git")
system("cd yay")
system("makepkg -si")
system("yay -S visual-studio-code-bin brave-bin pfetch")

# ZSH
system("sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"")
system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k")
system("cp -r $(pwd)/zsh/* ~/")

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