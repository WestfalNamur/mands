clear

# Environment ----------------------------------------------

export MANDSENV="dev"
export DATABASE_URL="postgresql://mands_user:mands_pw@localhost:5432/mands_db?sslmode=disable"

# Correct directory?
if  [ ! -f "./app/__init__.py" ]
then
    echo "You are not in the correct directory. Navigate to mands/server/"
    exit 1
fi

# Correct Python environment?
if  [ ! -d "./env" ]
then
    echo "Did not find an virtual environment for Python under ./env/"
    exit 1
fi

# Source python environment
source env/bin/activate
py_interpreter=$(which python)
echo "Running Python from: $py_interpreter"


# Correctness ---------------------------------------------

# Type checking
python3 -m mypy app/
if [ $? -eq 1 ]
then
    echo "MyPy found something."
    exit 1
fi


# Style ---------------------------------------------------

python3 -m black app/

python3 -m flake8 app/


# Run -----------------------------------------------------

clear

# - run app as a module via -m and then app.
# - important to use app not app/
python3 -m app 