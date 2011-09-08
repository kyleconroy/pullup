# Pullup - Pull Requests in git-svn

Since the current version of Github Enterprise lacks the merge button, I wrote a script that will pull down changes and apply pull reqeusts.

The script assumes that your remote is named origin and that the main branch is master

In your git repository, do

    pullup merge my-feature-branch

which is the equivalent to doing 

    git fetch origin
    git checkout -b my-feature-branch origin/my-feature-branch
    git rebase master
    git checkout master
    git merge my-feature-branch
    git push origin master    

Notice the rebase instead of the merge. That's important for git-svn 

