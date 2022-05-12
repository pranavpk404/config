function cdrp
    cd /code/projects/react
end

function cdnp
    cd /code/projects/nextjs
end

function cdpp
    cd /code/projects/python
end

function cdjp
    cd /code/projects/js
end

function rop
    sudo pacman -Rns $(pacman -Qtdq)
end

function server
    npm run dev
end

function startmongo
    systemctl start --now mongodb
end

function open
    xdg-open
end

function cnat
    npx create-next-app@latest --ts
end

function tailwind
    npm install -D tailwindcss postcss autoprefixer && npx tailwindcss init -p
end

function rmd
    rm -rf
end

function btopu
    btop --utf-force
end
