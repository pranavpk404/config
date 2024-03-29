export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

plugins=(git fast-syntax-highlighting zsh-autosuggestions)

fpath+=${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions/src
source $ZSH/oh-my-zsh.sh

alias cdrp="cd /code/projects/react"
alias cdnp="cd /code/projects/nextjs"
alias cdpp="cd /code/projects/python"
alias cdjp="cd /code/projects/js"
alias rop="sudo pacman -Rns $(pacman -Qtdq)"
alias server="npm run dev"
alias startmongo="systemctl start --now mongodb"
alias open="xdg-open"
alias cnat="npx create-next-app@latest --ts"
alias tailwind="npm install -D tailwindcss postcss autoprefixer && npx tailwindcss init -p"
alias btopu="btop --utf-force"
alias update="yay"
