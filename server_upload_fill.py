import dropbox
import os
from dotenv import load_dotenv

# .env 파일의 환경 변수 로드
load_dotenv()

# 환경 변수에서 액세스 토큰 읽기
ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')

if not ACCESS_TOKEN:
    raise ValueError("DROPBOX_ACCESS_TOKEN environment variable is not set.")

# 업로드할 폴더 경로
LOCAL_FOLDER = '/path/to/your/local/folder'
# Dropbox에서의 경로 (업로드할 위치)
DROPBOX_FOLDER = '/folder/in/dropbox'

def upload_files(local_folder, dropbox_folder):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    for root, dirs, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(local_path, local_folder)
            dropbox_path = os.path.join(dropbox_folder, relative_path).replace("\\", "/")

            with open(local_path, 'rb') as f:
                print(f"Uploading {local_path} to {dropbox_path}...")
                try:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
                    print(f"Uploaded {local_path} to {dropbox_path}")
                except dropbox.exceptions.ApiError as e:
                    print(f"Failed to upload {local_path}. Error: {e}")

if __name__ == '__main__':
    upload_files(LOCAL_FOLDER, DROPBOX_FOLDER)
