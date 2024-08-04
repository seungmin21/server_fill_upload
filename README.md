### 설치 명령어
pip install dotenv
pip install dropbox
python -m venv .venv

### 스크립트 용도
수동으로 클라우드에 업로드 하는 행동의 단계를 줄이고자 기획

초반에 업데이트를 감지해서 업로드하는 코드를 작성했으나
계획하는 의도와 맞지 않아서 파일을 업로드하는 것으로 변경

사용 클라우드는 dropbox를 채택

### 액세스 토큰 발급
dropbox app console - Oauth2탭에서 발급

### 클라우드 경로
액세스 토큰 발급을 위한 app이 아닌 dropbox에 생성된 폴더의 경로를 말한다.