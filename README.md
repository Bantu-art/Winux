# README for Winux Shell

Winux Shell is a simple terminal application built using Python and Tkinter. It allows users to execute linux commands in a graphical user interface in any operating system.

## Features

- User-friendly interface with a text input for commands and an output display area.

## Project Structure

```
winux-shell
├── src
│   ├── commands
│   │   ├── __init__.py
│   │   └── pwd.py
│   ├── ui
│   │   ├── __init__.py
│   │   ├── terminal.py
│   │   └── styles.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── command_handler.py
│   └── main.py
├── tests
│   ├── __init__.py
│   └── test_commands.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Bantu-art/Winux.git
   ```
2. Navigate to the project directory:
   ```
   cd winux-shell
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.