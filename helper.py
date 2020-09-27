import sys
import os
import binascii


def fix_nginx():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    FileName = "{}/assets/CurtaSalto.conf".format(current_dir)

    with open(FileName) as f:
        newText=f.read().replace('<HOME_TAG>', current_dir)
    with open(FileName, "w") as f:
        f.write(newText)

    FileName = "{}/assets/CurtaSalto.service".format(current_dir)

    with open(FileName) as f:
        newText=f.read().replace('<HOME_TAG>', current_dir)

    with open(FileName, "w") as f:
        f.write(newText)

def fix_settings(web_site, email, password_email, db_name, db_user, db_password):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    FileName = "{}/CurtaSalto/CurtaSalto/settings.py".format(current_dir)
    print(FileName)
    secret = binascii.hexlify(os.urandom(24))

    with open(FileName) as f:
        allowed_hosts=f.read().replace('<HOST_TAG>', web_site)
        secret_key = allowed_hosts.replace('<SECRET_KEY>', str(secret))
        email = secret_key.replace('<EMAIL_TAG>', email)
        email_password = email.replace('<EMAIL_PASSWORD>',password_email)
        db_name = email_password.replace('<DB_NAME>',db_name)
        db_pwrd = db_name.replace('<DB_PASSWORD>',db_password)
        db_user = db_pwrd.replace('<DB_USER>',db_user)
        print(db_user)
    with open(FileName, "w") as f:
        #f.write(db_user)
        pass



if __name__ == "__main__":
    web_site = sys.argv[0]
    print(sys.argv)
    email  = sys.argv[1]
    password_email = sys.argv[2]
    db_name = sys.argv[3]
    db_user = sys.argv[4]
    db_password = sys.argv[5]
    fix_nginx()
    fix_settings(web_site=web_site,
                email=email,
                password_email=password_email,
                db_name=db_name,
                db_user=db_user,
                db_password=db_password)
    


