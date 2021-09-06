WORK_DIR=files/analyses/$1

echo Creating $WORK_DIR
mkdir -p $WORK_DIR

REPO_DIR=repositories/$1

echo Analysing $REPO_DIR, result on $WORK_DIR
java -jar ck.jar $REPO_DIR true 0 false $WORK_DIR

echo removing $REPO_DIR
rm -rf $REPO_DIR 