class FunctionRules:
    name: str
    args: str
    chunks: list
    minSize: int
    maxSize: int

    def __init__(self, name: str, args: str, chunks: list, minimum_body_size: int, maximum_body_size: int) -> None:
        self.name = name
        self.args = args
        self.chunks = chunks
        self.minSize = minimum_body_size
        self.maxSize = maximum_body_size
