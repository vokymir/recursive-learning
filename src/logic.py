class Logic:
    basefolder: str
    intervals: list[int]

    def __init__(self, basefolder: str, intervals: list[int]):
        self.basefolder = basefolder
        self.intervals = intervals

    def parse_args(self, args: list[str]) -> bool:
        should_compile: bool = False
        should_run: bool = False
        should_add_qna: bool = False
        should_add_qroup: bool = False
        should_edit_qna: bool = False
        should_edit_group: bool = False
        should_del_group: bool = False
        should_del_qna: bool = False
        skip: bool = False

        for i in range(len(args)):
            if skip:
                continue

            arg = args[i]

            match arg:
                case "-c":
                    should_compile = True
                    break

                case "-r":
                    should_run = True
                    break

                case "-a":
                    should_add_qna = True
                    break

                case "-g":
                    should_add_qroup = True
                    break

                case "-e":
                    should_edit_qna = True
                    break

                case "-ge":
                    should_edit_group = True

                case "-d":
                    should_del_qna = True

                case "-gd":
                    should_del_group = True

        if should_del_group:
            self.del_group()
        if should_del_qna:
            self.del_qna()
        if should_edit_group:
            self.edit_group()
        if should_edit_qna:
            self.edit_qna()
        if should_add_qroup:
            self.add_group()
        if should_add_qna:
            self.add_qna()
        if should_compile:
            self.compile()
        if should_run:
            self.run_qnas()

    def compile(self) -> bool:
        """
        Compile all groups into one file with only relevant QnAs.
        """
        pass

    def run_qnas(self) -> bool:
        """
        Open compiled file and show user one question after another.
        """
        pass
