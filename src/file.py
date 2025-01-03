from qna import QnA
from helper import Priority


class Group:
    """
    Encapsulation of Group in file. Holds info about it and serves as mediator who can directly access and edit file.
    """

    g_name: str
    g_id: str
    g_par_id: str
    g_priority: Priority
    next_qna_id: int

    def __init__(self):
        pass

    def create_group(
        self,
        g_name: str,
        g_id: str,
        g_par_id: str,
        g_priority: Priority = Priority.NORMAL,
    ) -> bool:
        """
        Creating a new group, creates a new file with specified parameters.
        """
        self.g_name = g_name
        self.g_id = g_id
        self.g_par_id = g_par_id
        self.g_priority = g_priority
        self.next_qna_id = 0

    def load_group(self, g_id: str):
        """
        Load
        """

    def create_qna(self, g_id: str, qna: QnA):
        """ """
        pass
