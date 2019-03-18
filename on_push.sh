#!/bin/bash

set -e;

PID_FILE="cykablyat.pid";
SYSTEMCTL="systemctl";
SYSTEMD_UNIT="cykablyat.service";

# Get the current commit
CURRENT_COMMIT=$(git log --pretty=format:'%H' -n 1);

git pull;

# Check PID file
if [[ ! -f "${PID_FILE}" ]]; then
	echo "Service isn't running, quitting...";
	exit 0;
fi

# Check changed files
NEW_COMMIT=$(git log --pretty=format:'%H' -n 1);
if [[ ${CURRENT_COMMIT} == ${NEW_COMMIT} ]]; then
	echo "No new commit found, quitting...";
	exit 0;
fi

if [[ $(git diff --name-only ${CURRENT_COMMIT} ${NEW_COMMIT}) == *".py"* ]]; then
	echo "Python file changed, restarting service";
	sudo ${SYSTEMCTL} restart ${SYSTEMD_UNIT};
else
	echo "Reloading config files";
	sudo ${SYSTEMCTL} reload ${SYSTEMD_UNIT};
fi
