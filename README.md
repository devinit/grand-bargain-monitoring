A dashboard for monitoring the progress of Grand Bargain signatories publishing humanitarian data to IATI.

Information about the Grand Bargain can be found on the [Agenda for Humanity](http://www.agendaforhumanity.org/initiatives/3861) website.

Installation
============

This assumes a typical Python development setup is available (details on such things to be provided at some point in the future).

```
# Create and activate a virtual environment
python3 -m venv pyenv
source pyenv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set-up remote data
mkdir data/remote
./src/load_remote_data.py
```

Running the App
===============

```
python src/app.py
# Use your browser to navigate to http://127.0.0.1:5000/dashboard
```

Deployment
==========

Deployment is undertaken using ansible.

```
# Follow instructions at http://docs.ansible.com/ansible/intro_installation.html
# Check that ansible is working by pinging the server
ansible gbm -i deployment/inventory.ini -m ping
```

*NOTE:* You must have ssh access to hosts specified in `inventory.ini` for this to work. This file may be modified to change the specified servers.

```
# Configure the server and deploy the application
ansible-playbook deployment/playbooks.yml -i deployment/inventory.ini
```
OR step-by-step

```
# Configure the server
ansible-playbook deployment/setup.yml -i deployment/inventory.ini
ansible-playbook deployment/setup-numbergen.yml -i deployment/inventory.ini

# Deploy the application
ansible-playbook deployment/deploy.yml -i deployment/inventory.ini
ansible-playbook deployment/deploy-numbergen.yml -i deployment/inventory.ini
```
