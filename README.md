# Python Multithreaded Port Scanner

A multithreaded TCP port scanner built with Python.

This project is the second step of my Python Cybersecurity Roadmap. It improves the previous Port Scanner by using multiple threads to scan ports concurrently, making the scanning process significantly faster.

## Features

- Scan a specific port range
- Scan all ports (1-65535)
- Detect open TCP ports
- Identify common services running on open ports
- Concurrent scanning using ThreadPoolExecutor
- Simple command-line interface

## Technologies

- Python 3
- socket
- concurrent.futures

## Project Structure

```
.
├── main.py
├── scanner.py
├── input_handler.py
├── ui.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
```

## How to Run

```bash
python main.py
```

## Example Output

```
Port: 22 | Service: ssh
Port: 80 | Service: http
Port: 443 | Service: https
```

## What I Learned

During this project I learned:

- How TCP port scanning works
- How to create reusable functions
- Single Responsibility Principle (SRP)
- How ThreadPoolExecutor works
- What a Thread is
- What a Future is
- How concurrent port scanning improves performance
- How to organize Python projects into modules

## Future Improvements

- Export results to a file
- Add progress bar
- Add custom thread count
- Improve error handling

## Author

Jose Seminario