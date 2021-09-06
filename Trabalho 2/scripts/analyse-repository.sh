WORK_DIR=files/analyses/$1

mkdir -p $WORK_DIR

REPO_DIR=repositories/$1

java -jar ck.jar $REPO_DIR true 0 false $WORK_DIR

rm -rf $REPO_DIR 