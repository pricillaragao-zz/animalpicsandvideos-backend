#!/usr/bin/env bash

poetry run gunicorn "animalflix:create_app()"
