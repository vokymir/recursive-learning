from datetime import date, timedelta


class QnA:
    id: int = -1
    question: str = ""
    hint: str = ""
    answer: str = ""
    date_added: date = date.today()
    g_name: str = ""
    g_id: str = ""
    progress: list[str] = list()

    def __init__(self):
        self.progress = list()

    def should_present(self, intervals: list[int]) -> bool:
        """
        Should this QnA be presented to the user?
        Calculate which interval is this QnA in and if it was already solved or not.
        Return True if should be presented, False if not.
        """
        progress = self.progress

        for i in range(len(intervals)):

            interval = intervals[i]
            date_i = self.date_added + timedelta(days=interval)
            """ If this date already was and either dont have enough progress entries
                or do have, and the entry for this interval is 'X' - meaning unresolved.
            """
            if date_i <= date.today() and (
                len(progress) < i + 1 or (len(progress) >= i + 1 and progress[i] == "X")
            ):
                return True

        return False
