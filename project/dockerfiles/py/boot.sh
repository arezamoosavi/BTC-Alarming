#!/bin/bash
#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

n=10

while [ $n -gt 0 ]
do
	echo "Wait for kafka $n more times."
	n=$(( n-1 ))
    sleep 2
done

while python db_connect.py; do echo 'connecting to database...'; sleep 2; done;

echo ". . . . . Database Connection Is Done! . . . . ."


while python run_app.py; do echo 'geting bitcoin value...'; sleep 2; done;

echo ". . . . . Bitcoin Conn Is Done! . . . . ."


while python createdb.py; do echo 'tortoise db is creating...'; sleep 2; done;

echo ". . . . . Tortoise Is Done! . . . . ."

exec "$@"