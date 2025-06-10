from commands.pwd import PWD

class CommandHandler:
    def __init__(self):
        self.commands = {
            'pwd': PWD()
        }

    def execute(self, cmd):
        command = self.commands.get(cmd)
        if command:
            return command.execute()
        return "Command not recognized."