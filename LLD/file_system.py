class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root = Directory("")
        self.current = self.root
        self.current_path = "/"

    def _resolve_path(self, path):
        if not path:
            return self.current
        if path.startswith("/"):
            node = self.root
            parts = path.strip("/").split("/")
        else:
            node = self.current
            parts = path.strip().split("/")

        for part in parts:
            if not part or part == ".":
                continue
            elif part == "..":
                raise Exception("Parent navigation not supported in this simple version.")
            elif part not in node.children:
                raise FileNotFoundError(f"Path segment '{part}' not found")
            node = node.children[part]
            if isinstance(node, File):
                raise NotADirectoryError(f"'{part}' is a file, not a directory")
        return node

    def mkdir(self, path):
        node = self.root if path.startswith("/") else self.current
        parts = path.strip("/").split("/")
        for part in parts:
            if part not in node.children:
                node.children[part] = Directory(part)
            node = node.children[part]
    def create_file(self, path, content=""):
        if "/" in path:
            dir_path, file_name = path.rsplit("/", 1)
            dir_node = self._resolve_path(dir_path or "/")
        else:
            dir_node = self.current
            file_name = path
        dir_node.children[file_name] = File(file_name)
        dir_node.children[file_name].content = content

    def read_file(self, path):
        if "/" in path:
            dir_path, file_name = path.rsplit("/", 1)
            dir_node = self._resolve_path(dir_path or "/")
        else:
            dir_node = self.current
            file_name = path
        file_node = dir_node.children.get(file_name)
        if not isinstance(file_node, File):
            raise FileNotFoundError("File not found")
        return file_node.content


    def ls(self, path="."):
        try:
            node = self._resolve_path(path)
        except NotADirectoryError:
            # It's a file
            return [path.rsplit("/", 1)[-1]]
        return sorted(node.children.keys())

    def cd(self, path):
        node = self._resolve_path(path)
        self.current = node
        self.current_path = path if path.startswith("/") else self.current_path.rstrip("/") + "/" + path

    def rm(self, path):
        dir_path, name = path.rsplit("/", 1)
        dir_node = self._resolve_path(dir_path or "/")
        if name not in dir_node.children:
            raise FileNotFoundError(f"'{name}' not found in {dir_path}")
        del dir_node.children[name]

    def pwd(self):
        return self.current_path


if __name__ == "__main__":
    fs = FileSystem()

    fs.mkdir("/a/b")
    fs.create_file("/a/b/file1.txt", "Hello World!")
    print("Read file1:", fs.read_file("/a/b/file1.txt"))

    print("List /a:", fs.ls("/a"))
    print("List /a/b:", fs.ls("/a/b"))

    fs.cd("/a/b")
    print("PWD:", fs.pwd())
    print("LS .:", fs.ls("."))

    fs.create_file("file2.txt", "From CWD")
    print("Read file2:", fs.read_file("/a/b/file2.txt"))

    fs.rm("/a/b/file1.txt")
    print("After rm, LS /a/b:", fs.ls("/a/b"))
