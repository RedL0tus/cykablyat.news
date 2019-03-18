#!/bin/bash

set -e;

PID_FILE="cykablyat.pid";
SYSTEMCTL="systemctl";
SYSTEMD_UNIT="cykablyat.service";

git pull;

# Check PID file
if [[ ! -f "${PID_FILE}" ]]; then
	echo "Service isn't running, quitting...";
	exit 0;
fi

# Check changed files
if [[ $(git diff --name-only HEAD~1 HEAD~2) == *".py"* ]]; then
	echo "Python file changed, restarting service";
	sudo ${SYSTEMCTL} restart ${SYSTEMD_UNIT};
else
	echo "Reloading config files";
	sudo ${SYSTEMCTL} reload ${SYSTEMD_UNIT};
fi
