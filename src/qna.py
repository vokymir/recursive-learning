from datetime import date


class QnA:
    id: int = 0
    question: str = ""
    hint: str = ""
    answer: str = ""
    date_added: date = date.today()
    g_name: str = ""
    g_id: str = ""
    progress: list[str] = []

    def __init__(self):
        pass
