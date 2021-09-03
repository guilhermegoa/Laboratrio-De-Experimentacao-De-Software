echo Getting repository:
echo $2

WORK_DIR=repositories/$1

mkdir -p $WORK_DIR

echo Fake clone of repository $1...
# git clone $2 $WORK_DIR