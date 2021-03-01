function deploy {
    student=$1
    TMP="temporary_branch_for_remote_"
    branchname="$TMP$1"
    cowsay "Deploying new exercises to $student"
    git branch -d $branchname
    git checkout -b $branchname $student/main
    git pull --no-edit
    git merge --no-edit origin/main
    git push --force $student HEAD:main
    git checkout main
    git branch -d $branchname
}


if [ -z "$(git status --porcelain)" ]; then 
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
    if [[ "$BRANCH" != "main" ]]; then
        echo "Wrong branch"
        exit 1
    fi

    cowsay "First push changes to origin if not yet there..."
    git push origin

    source `dirname $0`/remotes.sh
    if [ -z "$1" ]; then
        for remote in ${remotes[@]}; do
            deploy $remote
        done
    else
        deploy $1
    fi
else
    echo "Commit changes first"
    exit 2
fi 


