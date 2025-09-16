#!/bin/bash
source venv/bin/activate
pytest -n 2 --browser chromium --browser firefox --headed