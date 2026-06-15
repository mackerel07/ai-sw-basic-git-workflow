# Git 트러블슈팅 실습

### git commit --amend 실습 (담당: 김창환)
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