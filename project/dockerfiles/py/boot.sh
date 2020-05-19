#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


while python db_connect.py; do echo 'connecting to database...'; sleep 2; done;

echo ". . . . . Done! . . . . ."

exec "$@"