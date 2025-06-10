import os

class LS:
    def execute(self, args=None):
        """List directory contents"""
        try:
            path = args[0] if args else "."
            return "\n".join(os.listdir(path))
        except FileNotFoundError:
            return f"ls: cannot access '{path}': No such file or directory"
        except Exception as e:
            return f"ls: error: {str(e)}"