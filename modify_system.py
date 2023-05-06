from os import system

# Programs
def install():  
    system("pacman -Syu neovim fish pavucontrol python-pywal alacritty pulseaudio pulseaudio-bluetooth blueman bluez bluez-utils feh flameshot gvfs-mtp btop mtpfs nemo nodejs npm noto-fonts-emoji noto-fonts pavucontrol tlp unrar unzip mpv git base-devel")
    print("Programs done")


def edit_fstab():
    system("mkdir /code /films /important /tutorials /misc")
    with open("/etc/fstab", "a") as fstab:
        fstab.write(
            """
UUID=908d171c-d003-4a70-9ea5-2ce6267a23a9 /code btrfs defaults,noatime 0 1
UUID=7cd2166c-e744-416c-8390-ddeb09de9d0f /misc btrfs defaults,noatime 0 1
UUID=0423513a-e50e-4a20-9975-81640333b1d8 /tutorials btrfs defaults,noatime 0 1
UUID=b38d72db-f098-4323-8652-240503b93b63 /films btrfs defaults,noatime 0 1
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
