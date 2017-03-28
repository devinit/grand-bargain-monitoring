A dashboard for monitoring the progress of Grand Bargain signatories publishing humanitarian data to IATI.

Information about the Grand Bargain can be found on the [Agenda for Humanity](http://www.agendaforhumanity.org/initiatives/3861) website.

Installation
============

This assumes a typical Python development setup is available (details on such things to be provided at some point in the future).

```
virtualenv -p python3 pyenv
source pyenv/bin/activate
pip install -r requirements.txt
./src/load_remote_data.py
```

Running the App
===============

```
python src/app.py
# navigate to http://127.0.0.1:5000/dashboard
```
