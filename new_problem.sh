if [[ $1 == "" ]]
then
    echo "Give problem number"
else
    number=$(printf "%03d" $1)
    mkdir "problem_$number"
    cd "problem_$number"
    touch script.py
    echo -e "all: test\ntest:\n	python script.py" > Makefile
fi
