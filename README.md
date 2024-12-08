python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate


# windows
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
pip freeze
python scrape2.py
deactivate


