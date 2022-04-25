from os import system

# Programs
system("pacman -Syu zsh pavucontrol alacritty gnome-keyring pulseaudio pulseaudio-bluetooth blueman bluez bluez-utils feh flameshot gvfs-mtp btop mousepad mtpfs nemo nodejs npm noto-fonts-emoji noto-fonts pavucontrol telegram-desktop tlp unrar unzip vlc ttf-fira-code git base-devel")
system("git clone https://aur.archlinux.org/yay.git")
system("cd yay")
system("makepkg -si")
system("yay -S visual-studio-code-bin brave-bin pfetch")
system("pacman -Rns paru amd-ucode neofetch bash-completion betterlockscreen kitty picom")
print("Programs done")

# ZSH
system("chsh -s /bin/zsh")
system("sh -c '$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)'")
system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k")
system("cp -r $(pwd)/zsh/* ~/")


# Bluetooth and audio
system("systemctl start bluetooth.service")
system("systemctl enable bluetooth.service")
system("systemctl pulseaudio start")
print("Bluetooth and audio done")

# Fstab
system("mkdir /code /films /important /tutorials /misc")
with open ("/etc/fstab","a") as fstab:
    fstab.write(
        """
UUID=adc2ff84-d990-4297-a2b3-045d06d35764 /code ext4 defaults,noatime 0 1
UUID=01D806FA07C373F0 /important ntfs defaults,noatime 0 1
UUID=0372a82c-5380-430f-8b8d-6e4d7dd241cd /misc ext4 defaults,noatime 0 1
UUID=99739e7d-2713-d801-9053-9e7d2713d801 /films ext4 defaults,noatime 0 1
UUID=7fd4d5e2-7f1d-4e94-bbdd-fc986cae9bba /tutorials ext4 defaults,noatime 0 1
        """
    )
system("mount -a")
print("fstab done")


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

# Swap memory
system("swapon -s")
system("swapoff -a")
system("dd if=/dev/zero of=/swapfile bs=1M count=4096")
system("mkswap /swapfile")
system("chmod 600 /swapfile")
system("swapon /swapfile")
system("echo '/swapfile none    swap    defaults 0 0' | sudo tee -a /etc/fstab")
system("mount -a")
print("Swap memory")