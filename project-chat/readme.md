# University of Poppleton Chatbot

## Overview
A modern, feature-rich chatbot designed for the University of Poppleton using Python and Tkinter. Built with SOLID principles and clean architecture.

## Project Structure
```plaintext
project-chat/
│
├── src/
│   ├── __init__.py
│   ├── interface/
│   │   ├── __init__.py
│   │   ├── chat_window.py
│   │   ├── dialog_manager.py
│   │   └── style_config.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── message_handler.py
│   │   ├── response_manager.py
│   │   └── session_manager.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── config_loader.py
│
├── config/
│   ├── responses.json
│   ├── agents.txt
│   └── ui_config.json
│
├── logs/
│   └── chat_logs/
│
├── tests/
│   ├── test_interface.py
│   ├── test_core.py
│   └── test_utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Features
- Modern, responsive UI with professional styling
- Configurable responses via JSON
- Multiple virtual agents
- Session logging with timestamps
- Quick response buttons
- Welcome tour for new users
- Real-time typing indicators
- Random disconnection simulation
- Color-coded message display

## Technical Specifications
- Python 3.6+
- Tkinter for UI
- JSON configuration
- SOLID principles implementation
- Modular architecture

## Installation
1. Clone the repository
2. Create a virtual environment
```bash
python -m venv venv
```
3. Activate the virtual environment
```bash
source venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python main.py
```