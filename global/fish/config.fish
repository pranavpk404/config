abbr -a -g cdrp cd /code/projects/react
abbr -a -g cdnp cd /code/projects/nextjs
abbr -a -g cdpp cd /code/projects/python/

abbr -a -g rop sudo pacman -Rns $(pacman -Qtdq)
abbr -a -g server yarn run dev
abbr -a -g startmongo systemctl start --now mongodb
abbr -a -g open xdg-open
abbr -a -g btopu btop --utf-force

function cnat
    npx create-next-app@latest --ts
end

function tailwind
    npm install -D tailwindcss postcss autoprefixer && npx tailwindcss init -p
end
function captoesc
	setxkbmap -option caps:escape
end
function resetkeymap
	setxkbmap -option
end	
