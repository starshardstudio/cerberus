#!/usr/bin/env bash
poetry run styxctl person create dev
poetry run styxctl person passwd dev dev
poetry run styxctl identity create dev dev1
poetry run styxctl identity create dev dev2
