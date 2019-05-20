import errno
import os


class Files:

    # Check if file exist
    def file_exist(self, file_path: str) -> bool:
        try:
            os.stat(file_path)
        except os.error:
            return False
        return True

    # Create file and all parent directories if not exists
    def create_if_not_exist(self, file_path: str):
        if not os.path.exists(os.path.dirname(file_path)):
            try:
                os.makedirs(os.path.dirname(file_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    def save(self, file_path: str, body: str) -> None:
        self.create_if_not_exist(file_path)
        file = open(file_path, 'w+')
        file.write(body)
        file.close()

    def read(self, file_path: str) -> str:
        file = open(file_path, 'r')
        body = file.read()
        file.close()
        return body
