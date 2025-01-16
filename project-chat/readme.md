# University of Poppleton Chatbot

## Overview
A modern, feature-rich chatbot designed for the University of Poppleton using Python and Tkinter. Built with SOLID principles and clean architecture. The chatbot provides an interactive interface for students to get information about courses, fees, and campus life.

## Project Structure
```plaintext
project-chat/
│
├── src/
│   ├── __init__.py
│   ├── interface/
│   │   ├── __init__.py
│   │   ├── chat_window.py      # Main UI components
│   │   ├── dialog_manager.py   # Manages chat flow
│   │   └── style_config.py     # UI styling configuration
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── message_handler.py  # Processes user messages
│   │   ├── response_manager.py # Manages bot responses
│   │   └── session_manager.py  # Handles chat sessions
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py          # Logging functionality
│   │   └── config_loader.py   # Configuration management
│
├── config/
│   ├── responses.json         # Chatbot response templates
│   ├── agents.txt            # Virtual agent names
│   └── ui_config.json        # UI configuration
│
├── logs/
│   └── chat_logs/            # Session logs storage
│
├── tests/
│   ├── test_interface.py     # UI tests
│   ├── test_core.py         # Core functionality tests
│   └── test_utils.py        # Utility function tests
│
├── main.py                   # Application entry point
├── requirements.txt          # Project dependencies
└── README.md
```


## Key Features
✨ **User Interface**
- Modern Tkinter-based UI with professional styling
- Color-coded message display for enhanced readability
- Interactive quick response buttons
- Real-time typing indicators
- First-time user welcome tour

🔧 **Core Functionality**
- Dynamic response system using JSON configuration
- Multiple virtual agent personalities
- Random disconnection simulation
- Configurable response templates
- Error handling and graceful degradation

📝 **Logging & Management**
- Comprehensive session logging with timestamps
- UTF-8 encoding support

## Technical Stack
- Python 3.6+
- Tkinter for GUI components
- JSON for configuration management
- Datetime for logging functionality
- Random for agent selection

## Installation
1. Clone the repository
```bash
git clone https://github.com/NirnayaT/project-chat.git
```
2. Create a virtual environment
```bash
python -m venv venv
```
3. Activate the virtual environment
```bash
venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python main.py
```

## Configuration
📁 **Config Files**
- `config/responses.json`: Customize chatbot responses
- `config/agents.txt`: Add or modify virtual agent names
- `config/ui_config.json`: Adjust UI settings

## Logging
📊 **Log Management**
- Location: `logs/chat_logs/`
- Format: `YYYYMMDD_HHMMSS.log`
- Timestamp-based organization

## Development
🔧 **Architecture**
- Implements SOLID principles
- Modular architecture for maintainability
- Comprehensive test coverage
- Clean code practices

## Contributing
🤝 **How to Contribute**
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## Guidelines
- Write clear commit messages
- Follow existing code style
- Add tests for new features
- Update documentation

## License
📝 MIT License - Feel free to use and modify

## Author
👨‍💻 Nirnaya Thapaliya

## Acknowledgments
🌟 **Special Thanks**
- University of Poppleton
- Python Community
- Tkinter Documentation
- Stack Overflow
