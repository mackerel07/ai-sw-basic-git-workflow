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