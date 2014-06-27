if [[ $1 == "" ]]
then
    echo "Give problem number"
else
    mkdir "problem_$1"
    cd "problem_$1"
    touch script.py
    echo -e "all: test\ntest:\n	python script.py" > Makefile
fi
