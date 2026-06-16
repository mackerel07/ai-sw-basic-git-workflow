# Git 트러블슈팅 실습

## 1. git commit --amend 실습 (담당: 김창환)
저는 git commit 중 amend 옵션을 실습했습니다.
amend는 마지막 커밋을 수정할 때 사용하는데, 대표적으로 파일을 빼먹었거나 커밋 메세지를 수정해야 할 때 사용합니다.

예를 들어서 아래와 같이 커밋 메세지를 잘못 입력한 경우엔
```
charles@ChalsBookPro B2-2_Team % git commit -am "docs: add 8-1,-a"
[main 50b613c] docs: add 8-1,-a
 1 file changed, 3 insertions(+)
```

이러한 방식으로 커밋 메세지를 수정할 수 있다.
```
charles@ChalsBookPro B2-2_Team % git commit --amend -m "docs: add 8-1-a"
[main f7598c4] docs: add 8-1-a
 Date: Mon Jun 15 16:51:48 2026 +0900
 1 file changed, 3 insertions(+)
charles@ChalsBookPro B2-2_Team %
```

## 2. Git reset --soft HEAD~1 실습 (담당: 김우종)

`git reset --soft HEAD~1` 명령어는 가장 최근 커밋을 취소하되, 변경된 작업 내역은 Staging Area에 그대로 보존하는 명령어입니다.
작업 내역은 유지하면서 커밋을 다시 하거나 여러 커밋을 하나로 합칠 때 유용합니다.

`Before`

```bash
$ git log
commit [COMMIT_HASH] (HEAD -> docs/troubleshooting-log-b)
Author: [AUTHOR] <[EMAIL]>
Date:   Mon Jun 15 16:56:06 2026 +0900

    refactor: delete line in devide.py

commit [COMMIT_HASH] (origin/main, origin/HEAD, main)
Merge: [HASH] [HASH]
Author: [AUTHOR] <[EMAIL]>
Date:   Mon Jun 15 16:37:20 2026 +0900

    Merge pull request #14 from [USER]/feature/refactor-multiply-return
    
    refactor: multiply.py
```

`After`

```bash
$ git reset --soft HEAD~1

$ git log
commit [COMMIT_HASH] (HEAD -> docs/troubleshooting-log-b, origin/main, origin/HEAD, main)
Merge: [HASH] [HASH]
Author: [AUTHOR] <[EMAIL]>
Date:   Mon Jun 15 16:37:20 2026 +0900

    Merge pull request #14 from [USER]/feature/refactor-multiply-return
    
    refactor: multiply.py
```

## 3. git revert 실습 (담당: 김명률)

revert는 이미 원격(push)에 올라간 커밋을 되돌릴 때 사용합니다.
reset과 달리 기존 커밋을 삭제하지 않고, 해당 변경을 취소하는 새 커밋을 추가하는 방식이라
히스토리가 보존되고 공유 브랜치에서도 강제 push 없이 안전하게 되돌릴 수 있습니다.

예를 들어 임시 커밋을 push한 뒤 이를 되돌리는 경우,
`Before` (되돌릴 커밋이 push된 상태)
```bash
$ git log --oneline
edccdc1 docs: add temp line for practice
```

`revert 실행` (반대 동작을 하는 새 커밋 생성 후 push)
```bash
$ git revert HEAD
$ git push
```

`After` (원래 커밋은 남고, Revert 커밋이 추가됨)
```bash
$ git log --oneline
bf96796 Revert "docs: add temp line for practice"
edccdc1 docs: add temp line for practice
```


## 4. git stash / git stash pop (담당:서채훈)

### 문제 상황

README.md를 수정한 상태에서 다른 브랜치로 이동하려고 하였다.

```bash
git checkout feature/subtract-function
```

Git은 작업 내용이 사라질 수 있으므로 브랜치 전환을 차단하였다.

### 원인

커밋되지 않은 변경 사항이 존재하는 상태에서 브랜치를 변경하려고 시도하였다.

#### 해결 방법

현재 작업 내용을 임시 보관하기 위해 stash를 사용하였다.

```bash
git stash
```

이후 브랜치 전환을 수행하였다.

```bash
git checkout feature/subtract-function
```

필요한 시점에 저장한 작업을 복원하였다.

```bash
git stash pop
```

### 결과

작업 내용을 유지한 상태로 브랜치를 전환할 수 있었고, 이후 변경 사항을 정상적으로 복원하였다.

#### 교훈

브랜치를 이동하기 전에 커밋되지 않은 변경 사항이 있다면 `git stash`를 활용하여 안전하게 작업을 보관할 수 있다.

로그:
* feature/add-function에서 작업을 함
sam@yeon-eowamaeche-ui-MacBookAir-2 src % nano calculator.py 
sam@yeon-eowamaeche-ui-MacBookAir-2 src % git checkout feature/subtract-function
error: Your local changes to the following files would be overwritten by checkout:
	src/calculator.py
Please commit your changes or stash them before you switch branches.
Aborting
sam@yeon-eowamaeche-ui-MacBookAir-2 src % 
sam@yeon-eowamaeche-ui-MacBookAir-2 src % git stash
Saved working directory and index state WIP on feature/add-function: 359fdf3 refactor: store add result in variable before return
sam@yeon-eowamaeche-ui-MacBookAir-2 src % git checkout feature/subtract-function
Switched to branch 'feature/subtract-function'
Your branch is ahead of 'origin/feature/subtract-function' by 6 commits.
  (use "git push" to publish your local commits)
sam@yeon-eowamaeche-ui-MacBookAir-2 src % git checkout feature/add-function
Switched to branch 'feature/add-function'
Your branch is ahead of 'origin/feature/add-function' by 1 commit.
  (use "git push" to publish your local commits)
sam@yeon-eowamaeche-ui-MacBookAir-2 src % git stash pop
On branch feature/add-function
Your branch is ahead of 'origin/feature/add-function' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   ../README.md
	modified:   calculator.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (87c684a04d23fc35a9d22de3eabae6ab30af4f80)
sam@yeon-eowamaeche-ui-MacBookAir-2 src % 

