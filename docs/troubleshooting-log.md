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