from datetime import datetime
from time import time
from pathlib import Path


def get_photo_name() -> str:
    prefix = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    suffix = str(time()).split('.')[1]
    return f'photo_{prefix}_{suffix}.jpg'


def get_new_file_name(old_file_name: str) -> str:
    prefix = f"{'.'.join(old_file_name.split('.')[:-1])}_{str(time()).split('.')[1]}"
    suffix = old_file_name.split('.')[-1]
    return f'{prefix}.{suffix}'


def create_user_path(user_id: int, content_type: str) -> str:
    cur_path = Path(Path.cwd(), 'static', str(user_id), content_type)
    if not Path.exists(cur_path):
        cur_path.mkdir(parents=True, exist_ok=True)
    return cur_path
