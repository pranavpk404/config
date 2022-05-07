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