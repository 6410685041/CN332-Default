#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 OLD_EMAIL NEW_EMAIL 'NEW_NAME'"
    exit 1
fi

OLD_EMAIL=$1
NEW_EMAIL=$2
NEW_NAME="$3"  # Enclose the variable in quotes to handle spaces

# Apply the filter-branch command to change the commit author email and name
git filter-branch -f --env-filter "
if [ \"\$GIT_COMMITTER_EMAIL\" = '$OLD_EMAIL' ]; then
    export GIT_COMMITTER_NAME='$NEW_NAME'
    export GIT_COMMITTER_EMAIL='$NEW_EMAIL'
fi
if [ \"\$GIT_AUTHOR_EMAIL\" = '$OLD_EMAIL' ]; then
    export GIT_AUTHOR_NAME='$NEW_NAME'
    export GIT_AUTHOR_EMAIL='$NEW_EMAIL'
fi
" --tag-name-filter cat -- --branches --tags
