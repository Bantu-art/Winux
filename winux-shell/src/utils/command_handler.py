from commands.pwd import PWD
from commands.ls import LS

class CommandHandler:
    def __init__(self):
        self.commands = {
            'pwd': PWD(),
            'ls': LS()
        }

    def execute(self, cmd):
        # Split command and arguments
        parts = cmd.split()
        command_name = parts[0]
        args = parts[1:] if len(parts) > 1 else None

        command = self.commands.get(command_name)
        if command:
            return command.execute(args)
        return "Command not recognized."