## 8.18.07

- python directory
```
/home/nymsite11/webapps/nym_django/lib/
```

/home/nymsite11/webapps/nym_django/lib/python2.7

## pip + virtualenv

  - see: https://community.webfaction.com/questions/4253/simple-virtualenv-usage-with-django

```
mkdir -p $HOME/lib/python2.7
easy_install-2.7 pip

pip install --user virtualenv
pip install --user virtualenvwrapper

PYTHONVER=2.7
PYTHON=python${PYTHONVER}

echo 'export PATH="$HOME/bin:$PATH"' >> $HOME/.bashrc
echo 'export TEMP="$HOME/tmp"' >> $HOME/.bashrc
echo "alias python=${PYTHON}" >> $HOME/.bashrc
echo "export PYTHON=${PYTHON}" >> $HOME/.bashrc
echo 'export WORKON_HOME="$HOME/.virtualenvs"' >> $HOME/.bashrc
echo 'export VIRTUALENVWRAPPER_TMPDIR="$WORKON_HOME/tmp"' >> $HOME/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/$PYTHON" >> $HOME/.bashrc
echo 'source $HOME/bin/virtualenvwrapper.sh' >> $HOME/.bashrc
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> $HOME/.bashrc
echo 'export PIP_RESPECT_VIRTUALENV=true' >> $HOME/.bashrc

source $HOME/.bashrc
hash -r

```

## SSH keys

- See:
    - https://docs.webfaction.com/user-guide/access.html?highlight=ssh
    - https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-linux

```
mkdir -p $HOME/.ssh
cd $HOME/.ssh
ssh-keygen -t rsa -b 4096 -C "raprasad@gmail.com"
vim ~/.ssh/id_rsa.pub
# copy to github
```

## Clone scdrecipe repo

```
cd /home/rpscd/webapps/scd_django/
git clone git@github.com:raprasad/scdrecipe.com.git
```

## Make virtualenv

```
mkvirtualenv nym_django
```

- if it doesn't work:
```
source $HOME/.bashrc
hash -r
```

-  Install pip packages

```
cd /home/rpscd/webapps/scd_django/scdrecipe.com
pip install -r requirements/prod.txt
```

- Update postactive for convenience

```
# open the postactivate file
vim /home/nymsite11/.virtualenvs/nym_django/bin/postactivate

# add these lines:
export DJANGO_SETTINGS_MODULE=nymdesign.settings.webfaction
```


## Update the WSGI

- reference: https://docs.webfaction.com/software/mod-wsgi.html?highlight=virtualenv#using-a-virtual-environment-with-mod-wsgi

- open the apache conf file:
```
vim /home/nymsite11/webapps/nym_django/apache2/conf/httpd.conf
```

- change the `WSGIDaemonProces` line to:
```
WSGIDaemonProcess nym_django processes=2 threads=12 python-path=/home/nymsite11/webapps/nym_django:/home/nymsite11/webapps/nym_django/NYMDesign:/home/nymsite11/.virtualenvs/nym_django:/home/nymsite11/.virtualenvs/nym_django/lib/python2.7:/home/nymsite11/.virtualenvs/nym_django/lib/python2.7/site-packages:/home/nymsite11/webapps/nym_django/lib/python2.7
```

- change `WSGIScriptAlias` line to:
```
WSGIScriptAlias / /home/nymsite11/webapps/nym_django/NYMDesign/nymdesign/wsgi.py
```

## Static
