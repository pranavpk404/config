from os import system


def neovim():
    system("git clone https://github.com/bushblade/nvim.git ~/.config/nvim")
    system("git clone https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim")
    system("git clone https://github.com/github/copilot.vim.git  ~/.config/nvim/pack/github/start/copilot.vim")
    system("chmod 777 ~/.config/nvim/")
    system("pacman -S neovim lua-language-server pyright nodejs-lts-gallium")
    system("npm install -g typescript typescript-language-server vscode-langservers-extracted vls @tailwindcss/language-server yaml-language-server @prisma/language-server emmet-ls neovim graphql-language-service-cli graphql-language-service-server prettier")


neovim()
