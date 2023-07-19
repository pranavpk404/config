from os import system

# Programs
def install():
    system("cp global/pacman.conf /etc/pacman.conf")
    system("pacman -S artix-archlinux-support")
    system("pacman-key --populate archlinux")
    system("pacman -Syu ffmpeg ffmpeg4.4 xf86-input-synaptics torbrowser-launcher xorg-xbacklight lxappearance fzf telegram-desktop firefox neovim fish pavucontrol python-pywal alacritty pulseaudio pulseaudio-bluetooth blueman bluez bluez-utils feh flameshot gvfs-mtp btop mtpfs nemo nodejs npm noto-fonts-emoji noto-fonts pavucontrol tlp unrar unzip mpv git base-devel")
    print("Programs done")


def edit_fstab():
    system("mkdir /code /films /misc")
    with open("/etc/fstab", "a") as fstab:
        fstab.write(
            """
            UUID=09623b5a-e8e9-4741-91ed-7be4cb21d51a /films ext4 defaults,noatime 0 1
UUID=ae9107a9-8577-46f4-8d24-049005d88bed /misc ext4 defaults,noatime 0 1
UUID=651cd300-434e-4e80-80fa-9e964a330c8b /code ext4 defaults,noatime 0 1
            """
        )
    system("mount -a")
    print("fstab done")


# Swap memory
def create_swap():
    system("swapon -s")
    system("swapoff -a")
    system("dd if=/dev/zero of=/swapfile bs=1M count=4096")
    system("mkswap /swapfile")
    system("chmod 600 /swapfile")
    system("swapon /swapfile")
    system("echo '/swapfile none    swap    defaults 0 0' | sudo tee -a /etc/fstab")
    system("mount -a")
    print("Swap memory Done")



user_input = input(
    "For Installing | For Edit fstab:2 | For Create Swap:3 | For Everything:4\n")

if user_input == "1":
    install()
elif user_input == "2":
    edit_fstab()
elif user_input == "3":
    create_swap()
elif user_input == "4":
    install()
    edit_fstab()
    create_swap()

else:
    print("Wrong input")
