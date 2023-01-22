#!/bin/bash

python src/manage.py collectstatic --noinput
python src/manage.py migrate
"$@"

