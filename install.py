
from os import system

# Programs
def install_and_remove():
    system("pacman -Syu typescript neovim fish pavucontrol alacritty gnome-keyring pulseaudio pulseaudio-bluetooth blueman bluez bluez-utils feh flameshot gvfs-mtp btop mtpfs nemo nodejs npm noto-fonts-emoji noto-fonts pavucontrol telegram-desktop tlp unrar unzip vlc ttf-fira-code git base-devel")
    system("pacman -Rns paru vim amd-ucode neofetch bash-completion betterlockscreen kitty picom")
    print("Programs done")

# Fstab
def edit_fstab ():
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


system("systemctl start bluetooth.service")
system("systemctl enable bluetooth.service")
system("systemctl pulseaudio start")
print("Bluetooth and audio done")


install_and_remove()
edit_fstab()
create_swap()