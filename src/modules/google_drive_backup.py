from pathlib import Path
from datetime import datetime
import zipfile
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def _paths():
    root = Path(__file__).resolve().parents[2]
    cred = root / "google_credentials.json"
    token = root / "google_token.json"
    return root, cred, token
 
def _has_credentials():
    _, cred, _ = _paths()
    return cred.exists()

def authorize():
    root, cred, token = _paths()
    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(cred), SCOPES)
            creds = flow.run_local_server(port=0)
        token.write_text(creds.to_json(), encoding="utf-8")
    return creds

def create_zip(output_dir=None):
    root, _, _ = _paths()
    # 使用固定名称前缀 python-project，避免因本地文件夹命名不同导致备份文件名不统一
    name = f"python-project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    outdir = Path(output_dir) if output_dir else root / "output"
    outdir.mkdir(parents=True, exist_ok=True)
    zpath = outdir / name
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in root.rglob("*"):
            if ".git" in p.parts:
                continue
            if "output" in p.parts:
                continue
            if p.name in {"google_token.json", "google_credentials.json"}:
                continue
            if p.is_file():
                z.write(p, p.relative_to(root))
    return zpath

def upload_to_drive(file_path, folder_id=None):
    creds = authorize()
    service = build("drive", "v3", credentials=creds)
    metadata = {"name": Path(file_path).name}
    if folder_id:
        metadata["parents"] = [folder_id]
    media = MediaFileUpload(str(file_path), resumable=True)
    f = service.files().create(body=metadata, media_body=media, fields="id").execute()
    return f.get("id")

def run_backup(folder_id=None):
    zip_path = create_zip()
    if _has_credentials():
        file_id = upload_to_drive(zip_path, folder_id)
    else:
        file_id = None
    return str(zip_path), file_id

if __name__ == "__main__":
    run_backup()
