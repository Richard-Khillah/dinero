#!/usr/bin/env bash

sh ./initdb.sh

echo "Seeding db"

python seed.py

echo "Done seeding"