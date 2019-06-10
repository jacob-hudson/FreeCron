#!/usr/bin/env bash

yes | gcloud app deploy
yes | gcloud app deploy cron.yaml