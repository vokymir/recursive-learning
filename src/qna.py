from datetime import date


class QnA:
    id: int
    qustion: str
    hint: str
    answer: str
    date_added: date
    g_name: str
    g_id: str
    progress: list[str]

    def __init__(self):
        pass
