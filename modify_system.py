from os import system

# Programs
def install():  
    system("xbps-install -Su xbps tor-browser python3-tkinter python3 neovim bspwm polybar sxhkd rofi fish-shell pavucontrol pywal alacritty firefox pulseaudio blueman feh flameshot gvfs-mtp btop mtpfs nemo nodejs noto-fonts-emoji pavucontrol unzip mpv git base-devel")
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
UUID=b38d72db-f098-4323-8652-240503b93b63 /films btrfs defaults,noatime 0 1
UUID=01D806FA07C373F0 /important ntfs defaults,noatime 0 1
            """
        )
    system("mount -a")
    print("fstab done")





user_input = input(
    "For Installing | For Edit fstab:2 | For Everything:3\n")

if user_input == "1":
    install()
elif user_input == "2":
    edit_fstab()
elif user_input == "3":
    install()
    edit_fstab()

else:
    print("Wrong input")
