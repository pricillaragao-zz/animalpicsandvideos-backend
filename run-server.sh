#!/usr/bin/env bash

if ! command -v poetry &> /dev/null
then
    gunicorn "animalflix:create_app()"
    exit
else
    poetry run gunicorn "animalflix:create_app()"
fi
