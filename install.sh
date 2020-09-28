#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


if [[ $# -eq 0 ]]; then
    echo "número de argumentos não bate"
    echo "arg0 = web_site"
    echo "arg1 = email"
    echo "arg2 = password_email"
    echo "arg3 = db_name"
    echo "arg4 = db_user"
    echo "arg5 = db_password"
    exit -1
fi


#install dependencies
install_python(){
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.8 python3-pip
    pip3 install --upgrade pip
    pip3 install update pip
}

create_venv(){
    python3 -m venv venv
    source venv/bin/activate
    pip3 install --upgrade pip
    pip3 install update pip
    pip3 install -r requirements.txt
}

install_nginx(){
    sudo apt install nginx
    sudo cp ./assets/CurtaSalto.conf /etc/nginx/sites-available/
    sudo systemctl restart nginx.service
}

install_runner(){
    sudo cp ./assets/CurtaSalto.service /etc/systemd/system/
    sudo systemctl enable CurtaSalto.service
    sudo systemctl start CurtaSalto.service
}

config_site(){
    python3 helper.py $1 $2 $3 $4 $5 $6
}

install_python
create_venv
config_site
install_runner
install_nginx



