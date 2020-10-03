#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
web_site=$1
email=$2
password_email=$3
db_name=$4
db_user=$5
db_password=$6

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
    sudo apt update
    sudo apt install python3.8 python3.8-dev python3.8-venv
    sudo apt install python3.8-distutils
    sudo apt install python3.8-venv python3.8-dev
    curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
    python3.8 get-pip.py
    pip install --upgrade pip setuptools wheel
    pip install --upgrade pip
    pip install update pip
}

create_venv(){
    python3.8 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install update pip
    pip install -r requirements.txt
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
    python3.8 helper.py $web_site $email $password_email $db_name $db_user $db_password
}

install_python
create_venv
config_site
install_runner
install_nginx



