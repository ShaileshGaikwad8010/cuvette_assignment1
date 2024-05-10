# LaTeX to JSON Converter

This project aims to convert LaTeX documents containing formatted questions and answers into JSON format for easier processing and analysis.

## Features

- Converts LaTeX documents with formatted questions into JSON format.
- Handles different patterns for specifying question IDs.
- Extracts question text, options, correct answers, and solution text.
- Saves the extracted data into a JSON file.

## Requirements

- Python 3.x
- `re` (regular expression) module
- `json` module

## Usage

1. Place your LaTeX document (`latex_code.tex`) containing the questions in the root directory.
2. Run the Python script `latex_to_json.py`.
3. The extracted questions will be saved in a JSON file named `questions.json` in the same directory.

## Detailed Algorithm Steps

1. **Read LaTeX Code**: Read the contents of the LaTeX file (`latex_code.tex`) into a string variable.

2. **Split LaTeX Code**: Use regular expressions to split the LaTeX code into separate question texts based on the patterns for specifying question IDs. The algorithm handles two patterns:
   - Pattern 1: Questions starting with `Question ID: [ID]`.
   - Pattern 2: Questions starting with `\section*{Question ID: [ID]}`.

3. **Iterate Through Questions**:
   - For each question text extracted:
     - Extract the question ID using regular expressions based on the identified pattern.
     - Extract the question text, options, correct answers, and solution text using regular expressions.
     - Create a dictionary object representing the question data.
     - Append the question dictionary to a list of questions.

4. **Convert to JSON**: Convert the list of question dictionaries into JSON format using the `json` module.

5. **Save JSON File**: Save the JSON data into a file named `questions.json` in the same directory.

## Example

Suppose you have a LaTeX document `latex_code.tex` containing formatted questions. Running the Python script `latex_to_json.py` will convert it into a JSON file `questions.json`.


