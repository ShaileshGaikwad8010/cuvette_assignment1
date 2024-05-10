import re
import json

def convert_latex_to_json(latex_code):
    questions = []

    # Split LaTeX code into separate questions
    question_texts = re.split(r'(\\section\*{Question ID: \d+}|Question ID: \d+)', latex_code)[1:]

    for i in range(0, len(question_texts), 2):
        question = {}

        # Extract question ID
        question_id_match = re.search(r'Question ID: (\d+)', question_texts[i] if i % 2 == 0 else question_texts[i + 1])
        if question_id_match:
            question_id = int(question_id_match.group(1))
            question['questionNumber'] = i // 2 + 1
            question['questionId'] = question_id

            # Extract question text
            question_text_match = re.search(r'(?:\n)(.*?)(?:\n\()', question_texts[i + 1], re.DOTALL)
            question_text = question_text_match.group(1).strip() if question_text_match else ""
            question['questionText'] = question_text

            # Extract options
            options_matches = re.findall(r'\(([A-D])\) (.*?)\n', question_texts[i + 1])
            options = [{'optionNumber': ord(option[0]) - ord('A') + 1, 'optionText': option[1].strip(), 'isCorrect': False} for option in options_matches]

            # Extract correct answer
            answer_match = re.search(r'Answer \(([A-D])\)', question_texts[i + 1])
            if answer_match:
                correct_answer = answer_match.group(1)
                correct_option_index = ord(correct_answer) - ord('A')
                options[correct_option_index]['isCorrect'] = True

            question['options'] = options

            # Extract solution text
            solution_text_match = re.search(r'Sol\..*?(?=\\section|\Z)', question_texts[i + 1], re.DOTALL)
            solution_text = solution_text_match.group().strip() if solution_text_match else ""
            question['solutionText'] = solution_text

            questions.append(question)

    return questions

# Read LaTeX code from file
with open('latex_code.tex', 'r') as file:
    latex_code = file.read()

# Convert LaTeX to JSON
questions_json = convert_latex_to_json(latex_code)

# Save JSON to file
with open('questions.json', 'w') as json_file:
    json.dump(questions_json, json_file, indent=2)
