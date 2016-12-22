#!/usr/bin/env bash

echo "Removing old db"

rm app.sqlite

echo "Creating db"

python db.py >/dev/null 2>&1

echo "Database created"
