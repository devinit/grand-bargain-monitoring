A dashboard for monitoring the progress of Grand Bargain signatories publishing humanitarian data to IATI.

Information about the Grand Bargain can be found on the [Agenda for Humanity](http://www.agendaforhumanity.org/initiatives/3861) website.

Installation
============

This assumes a typical Python development setup is available (details on such things to be provided at some point in the future).

```
virtualenv -p python3 pyenv
source pyenv/bin/activate
pip install -r requirements.txt
./src/load-remote-data.py
```
