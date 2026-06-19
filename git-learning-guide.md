# Git Practice Guide

This guide is for learning advanced Git commands in this repo by using the two Django apps that already exist:

- demoapp
- featureapp

Repository root:

- /home/sys-25/migration_practice/migration_prac/

## What You Will Practice

You will use small, safe code changes in both apps to practice these commands:

- git cherry-pick
- git reset
- git rebase
- git log
- git status
- git branch
- git checkout or git switch

## Important Files For Practice

Use these files as your demo area:

- [demoapp/views.py](demoapp/views.py)
- [demoapp/models.py](demoapp/models.py)
- [demoapp/tests.py](demoapp/tests.py)
- [featureapp/views.py](featureapp/views.py)
- [featureapp/models.py](featureapp/models.py)
- [featureapp/tests.py](featureapp/tests.py)

Current example functions already exist and can be used as practice targets:

- [demoapp/views.py](demoapp/views.py) has get_user and get_dashboard
- [featureapp/views.py](featureapp/views.py) has calculate_round_data

## Practice Strategy

Use one app to create a feature branch, and the other app to simulate a second line of work. That way you can safely move commits around without touching unrelated code.

Suggested branch layout:

- practice/cherry-pick
- practice/reset
- practice/rebase

## Step-By-Step Plan

### 1. Start From A Clean State

Run:

```bash
git status
git branch
git log --oneline --decorate -5
```

Make sure the working tree is clean before each exercise.

### 2. Create A Simple Demo Change In demoapp

Add or change one small function in demoapp/views.py.

Example practice ideas:

- make get_dashboard return a slightly richer dictionary
- add a new helper like format_user_name
- add a tiny test in demoapp/tests.py

Commit it:

```bash
git add demoapp/views.py demoapp/tests.py
git commit -m "demoapp: add practice change"
```

### 3. Practice Cherry-Pick

Cherry-pick is used when you want one commit from one branch on another branch.

Workflow:

```bash
git checkout -b practice/cherry-pick
git log --oneline
git cherry-pick <commit-hash>
```

What to observe:

- the commit is copied, not moved
- the same change can exist on more than one branch

### 4. Practice Reset

Reset is used when you want to move branch history backward.

Use a temporary branch for this practice:

```bash
git checkout -b practice/reset
git log --oneline
git reset --soft HEAD~1
```

Then compare different reset modes:

```bash
git reset --mixed HEAD~1
git reset --hard HEAD~1
```

What to observe:

- soft keeps changes staged
- mixed keeps changes in the working tree
- hard removes changes completely

Only use hard on throwaway practice commits.

### 5. Practice Rebase

Rebase is used to rewrite commits so history becomes linear.

Create two or more small commits, then replay them onto another branch:

```bash
git checkout -b practice/rebase
git log --oneline
git rebase main
```

If your main branch name is different, replace main with the correct branch.

Useful rebase variations:

```bash
git rebase -i HEAD~3
git rebase --abort
git rebase --continue
```

What to observe:

- commit order can be changed
- commit messages can be edited during interactive rebase
- conflicts must be resolved before continuing

## Recommended Learning Order

1. Learn git status, git add, and git commit first.
2. Practice git cherry-pick using a single small commit.
3. Practice git reset on throwaway commits only.
4. Practice git rebase after you are comfortable with commit history.

## Safe Rules

- Do not use git reset --hard on important work.
- Keep practice changes small and isolated.
- Use separate branches for each exercise.
- Check git status before every risky command.
- If something goes wrong, run git log --oneline --decorate --graph to understand the history.

## Suggested Demo Work In This Repo

You can use these simple ideas for practice changes:

- add a helper in demoapp/views.py
- add a second helper in featureapp/views.py
- add a small model field change in one app only
- write a small test in demoapp/tests.py or featureapp/tests.py

Keep each change easy to identify so you can see exactly what Git commands are doing.

## Quick Cheat Sheet

```bash
git status
git add .
git commit -m "message"
git log --oneline --graph --decorate --all
git cherry-pick <commit-hash>
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git rebase main
git rebase -i HEAD~3
```

## Best Place To Start

Start in [demoapp/views.py](demoapp/views.py), make one small change, commit it, and then practice moving that commit between branches.
