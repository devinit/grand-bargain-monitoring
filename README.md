A dashboard for monitoring the progress of Grand Bargain signatories publishing humanitarian data to IATI.

Information about the Grand Bargain can be found on the [Agenda for Humanity](http://www.agendaforhumanity.org/initiatives/3861) website.

Installation
============

This assumes a typical Python development setup is available (details on such things to be provided at some point in the future).

```
# Set-up and activate a python3 virtual environment
virtualenv -p python3 pyenv
source pyenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a remote directory and download remote data
mkdir data/remote
./src/load_remote_data.py
```

Running the App
===============

```
python src/app.py
# navigate to http://127.0.0.1:5000/dashboard
```

Deployment
==========

Deployment is undertaken using ansible.

```
# follow instructions at http://docs.ansible.com/ansible/intro_installation.html
# check that ansible is working by pinging the server
ansible gbm -i deployment/inventory.ini -m ping
```

*NOTE:* You must have ssh access to hosts specified in `inventory.ini` for this to work. This file may be modified to change the specified servers.

```
# configure the server and deploy the application
ansible-playbook deployment/playbooks.yml -i deployment/inventory.ini
```
OR step-by-step

```
# configure the server
ansible-playbook deployment/setup.yml -i deployment/inventory.ini
ansible-playbook deployment/setup-numbergen.yml -i deployment/inventory.ini

# deploy the application
ansible-playbook deployment/deploy.yml -i deployment/inventory.ini
ansible-playbook deployment/deploy-numbergen.yml -i deployment/inventory.ini
```
