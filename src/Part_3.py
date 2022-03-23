"""
Part 3

> 시작하기 전에 Part 1 & 2 가 진행되어야 합니다. 

Assignment Requirement

1) 진행한 과제 변경 내용을 스테이징 영역(staging area)에 추가합니다.
2) 스테이징 영역(staging area)의 상태를 확인합니다.
3) 현재 상태를 log 에 남을 수 있도록 기록(commit)합니다.
4) 원격 레포에 로컬 상태를 반영합니다.
5) codestates/simple-git-flow main branch 에 PR을 날립니다.

참고: 앞으로의 과제는 한 스텝씩 제공하지 않습니다. 
     Assignment Requirement 는 Urclass 노트의 Getting Started 와 동일하게 제공합니다.

아래에 코드에 요구사항에 맞는 Bash 쉘 기반 CLI 명령어를 작성합니다.
요구사항을 잘 보고, 상황에 맞게 정확히 작성해 주세요.
또한, 로컬에서 해당 명령어를 실행하면서 따라와 주세요.

** 대소문자를 정확히 구분해서 작성해 주세요. **
"""

ADD_TO_STAGING_AREA = "현재 변경 내용을 '모두 한 번에' 스테이징 영역(staging area)에 추가하는 CLI 명령어를 작성합니다."

CHECK_AREA_STATEMENT = "스테이징 영역(staging area)의 상태를 확인하는 CLI 명령어를 작성합니다."

COMMIT_TO_REPO = "현재 상태를 레포지토리에 기록하는 CLI 명령어를 작성합니다. (여기서 커밋 메세지는 'Part3 commit' 로 작성합니다.)"

PUSH_TO_REMOTE = "origin 이라는 이름을 가진 원격 Repo 에 로컬의 main 브랜치 상태를 반영하는 CLI 명령어를 작성합니다."