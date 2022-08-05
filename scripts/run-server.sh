VENV=./venv

python3 -m venv $VENV
$VENV/bin/pip install -r requirements.txt

$VENV/bin/python zanjabil/manage.py migrate
$VENV/bin/python zanjabil/manage.py collectstatic --no-input
$VENV/bin/python zanjabil/manage.py runserver 0.0.0.0:8000

