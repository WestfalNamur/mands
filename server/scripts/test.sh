clear

# Environment ----------------------------------------------

# set env vars for current shell and all processes started from current shell.
export MANDSENV="testing"
export DATABASE_URL="postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"


# Source python environment
py_interpreter=$(which python)
echo "Running Python from: $py_interpreter"


# Correctness ---------------------------------------------

python3 -m mypy app/
if [ $? -eq 1 ]
then
    echo "MyPy found something."
    exit 1
fi


# Style ---------------------------------------------------

python3 -m black app/

python3 -m isort app/ --profile black

python3 -m flake8 app/

if [ $? -eq 1 ]
then
    exit 1
fi


# Security ------------------------------------------------

bandit -r app/  --configfile bandit.yaml


# Test ----------------------------------------------------

python3 -m pytest --cov app/

if [ $? -eq 1 ]
then
    exit 1
fi