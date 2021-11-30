import datetime as dt
import uuid

def generate_unique_id() -> str:
    time: str = dt.datetime.now().strftime("%y%m%d-%H%M%S-%f")
    random_id: str = str(uuid.uuid4())
    return "-".join([time, random_id])
