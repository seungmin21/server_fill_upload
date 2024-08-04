import os
import time
import dropbox  # Dropbox 예시. 다른 클라우드 서비스의 SDK를 사용할 수도 있습니다.

# Dropbox 액세스 토큰
ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# 로컬 디렉토리와 클라우드 경로 설정
LOCAL_DIR = '/path/to/local/directory'
CLOUD_DIR = '/path/in/dropbox'

def upload_file(file_path):
    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read(), CLOUD_DIR + '/' + os.path.basename(file_path), mode=dropbox.files.WriteMode('overwrite'))

def monitor_directory():
    known_files = set(os.listdir(LOCAL_DIR))
    while True:
        current_files = set(os.listdir(LOCAL_DIR))
        new_files = current_files - known_files
        for file in new_files:
            upload_file(os.path.join(LOCAL_DIR, file))
        known_files = current_files
        time.sleep(10)  # 10초마다 체크

monitor_directory()
