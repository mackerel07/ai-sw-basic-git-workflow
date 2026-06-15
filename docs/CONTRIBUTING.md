# Contributing Guide

## 브랜치 전략 (GitHub Flow)

* main: 항상 안정적인 상태를 유지한다.
* feature/*: 기능 개발 또는 문서 작업을 진행한다.
* 모든 작업은 Issue 생성 후 feature 브랜치에서 진행한다.

### GitHub Flow를 선택한 이유

1. 작업 단위별로 독립적인 개발이 가능하다.
2. Pull Request를 통해 코드 리뷰를 진행할 수 있다.
3. main 브랜치의 안정성을 유지할 수 있다.

---

## 브랜치 네이밍 규칙

```text
feature/<task-name>
```

예시

```text
feature/add-function
feature/subtract-function
feature/contributing-guide
feature/conflict-log-1
```

---

## 커밋 메시지 컨벤션

형식

```text
<type>: <description>
```

사용 가능한 타입

```text
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
refactor: 코드 개선
test: 테스트 추가
```

예시

```text
feat: add addition function
docs: add contributing guide
fix: resolve merge conflict
```

금지 예시

```text
update
fix
temp
wip
final
```

---

## Pull Request 규칙

모든 작업은 Pull Request를 통해 main 브랜치에 병합한다.

PR 본문 필수 항목

### 연결 이슈

```text
Closes #이슈번호
```

### 변경 사항 (What)

무엇을 변경했는지 작성

### 변경 이유 (Why)

왜 변경했는지 작성

### 테스트 방법 (How)

어떻게 검증했는지 작성

---

## 코드 리뷰 규칙

* 단순 LGTM만 작성하지 않는다.
* 파일 또는 코드 라인을 기준으로 리뷰한다.
* 질문, 개선 제안, 리스크 지적 중 최소 1개 이상 작성한다.
* PR 작성자는 리뷰에 답글을 남기거나 수정 커밋으로 반영한다.

---

## 충돌 대응 흐름

1. 충돌 발생 확인
2. 팀원에게 공유
3. 충돌 해결
4. conflict-resolution.md 기록
5. PR 업데이트 후 재검토 요청

---

## 병합 조건

* 최소 1명 승인 필요
* CI 또는 테스트 실패 시 병합 금지
* 충돌 발생 시 해결 후 병합

