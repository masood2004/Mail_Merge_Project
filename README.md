# Mail Merge Project

Welcome to the Mail Merge Project! This project automates the process of generating personalized letters using a pre-defined template and a list of recipient names. It reads input files containing names and a letter template, replaces placeholders in the template with actual names, and outputs individualized letters for each recipient.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Mail merge is a process used to create personalized documents, such as letters or emails, by combining a template with a list of data (e.g., names). This project automates the mail merge process by:
1. Reading a list of names from an input file.
2. Loading a pre-written letter template with a placeholder for the name.
3. Replacing the placeholder in the template with the names from the list.
4. Saving the personalized letters as individual files ready to be sent.

The project is written in Python and is simple to use. It is designed to work with plain text files containing the names and the letter template.

## Features

- **Customizable Template**: You can create your own letter template with a `[name]` placeholder.
- **Batch Processing**: It can handle any number of recipients by reading from a list of names.
- **Automated Letter Generation**: Automatically generates one letter for each recipient and saves it as an individual file.
- **Simple to Use**: Just input your names and letter template, and the script takes care of the rest.

## Installation

To use the Mail Merge Project, you'll need to have Python installed on your computer. Follow the steps below to set up the project:

### Prerequisites

- Python 3.x: You can download it from [python.org](https://www.python.org/downloads/).
- Git (optional): If you'd like to clone the repository, you can install Git from [git-scm.com](https://git-scm.com/).

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/masood2004/Mail_Merge_Project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Mail_Merge_Project
   ```

3. Install any required dependencies (if there are any, though this project doesn't require additional dependencies outside of Python itself):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After setting up the project, follow these steps to use the mail merge script:

### Step 1: Prepare Input Files
1. **List of Names**: Create a text file `invited_names.txt` in the `./Input/Names/` folder. Each line should contain one name (e.g., `John Doe`).
2. **Letter Template**: Create a letter template in the file `starting_letter.txt` in the `./Input/Letters/` folder. Use the placeholder `[name]` where you want each recipient's name to appear in the letter.

Example of `starting_letter.txt`:
```
Dear [name],

We are pleased to invite you to our upcoming event. We look forward to your participation.

Best regards,
The Event Team
```

### Step 2: Run the Script

Run the Python script `mail_merge.py`:

```bash
python mail_merge.py
```

This will:
1. Replace the `[name]` placeholder in the template with each name from `invited_names.txt`.
2. Create a personalized letter for each name and save it in the `./Output/ReadyToSend/` folder.

Each personalized letter will be saved as `letter_for_<name>.txt`.

### Step 3: Check the Output

After the script finishes running, you'll find the generated letters in the `./Output/ReadyToSend/` directory. Each file will be named according to the recipient, for example, `letter_for_John_Doe.txt`.

## File Structure

The project follows a simple directory structure:

```
Mail_Merge_Project/
│
├── Input/
│   ├── Names/
│   │   └── invited_names.txt        # List of recipient names (one per line)
│   └── Letters/
│       └── starting_letter.txt      # Letter template with placeholder [name]
│
├── Output/
│   └── ReadyToSend/
│       └── letter_for_<name>.txt    # Personalized letters for each recipient
│
├── mail_merge.py                    # The main Python script for performing the mail merge
└── README.md                        # Project documentation (this file)
```

## Contributing

Contributions to this project are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Create a pull request.

Please ensure that your code follows the project's style guidelines and is well-documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
