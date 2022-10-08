from os import system

# Programs
def install():  
    system("xbps-install -Su xbps tor-browser neovim bspwm polybar sxhkd rofi fish-shell pavucontrol pywal alacritty firefox pulseaudio blueman feh flameshot gvfs-mtp btop mtpfs nemo nodejs noto-fonts-emoji pavucontrol tlp unzip mpv git base-devel")
    print("Programs done")
    system("ln -s /etc/sv/bluetoothd /var/service/")


def edit_fstab():
    system("mkdir /code /films /important /tutorials /misc /anime")
    with open("/etc/fstab", "a") as fstab:
        fstab.write(
            """

UUID=908d171c-d003-4a70-9ea5-2ce6267a23a9 /code btrfs defaults,noatime 0 1
UUID=7cd2166c-e744-416c-8390-ddeb09de9d0f /misc btrfs defaults,noatime 0 1
UUID=0423513a-e50e-4a20-9975-81640333b1d8 /tutorials btrfs defaults,noatime 0 1
UUID=15e22881-ee5e-4ecb-819c-94454c77f8c6 /anime btrfs defaults,noatime 0 1

UUID=99739e7d-2713-d801-9053-9e7d2713d801 /films ext4 defaults,noatime 0 1
UUID=01D806FA07C373F0 /important ntfs defaults,noatime 0 1
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
