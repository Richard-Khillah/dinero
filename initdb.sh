#!/usr/bin/env bash

if [ -f app.sqlite ]; then
  echo "Removing old db"

  rm app.sqlite
fi


echo "Creating db"

python db.py >/dev/null

echo "Database created"
