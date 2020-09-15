#!/usr/bin/env bash

if ! command -v poetry &> /dev/null
then
    gunicorn "animalpicsandvideos:create_app()"
    exit
else
    poetry run gunicorn "animalpicsandvideos:create_app()"
fi
