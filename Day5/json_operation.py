import json
from prettytable import PrettyTable
with open("sample.json",'r') as fobj:
    data = json.load(fobj)
    
table = PrettyTable()
table.field_names = ["Category", "Question", "Options", "Answer"]

for category, category_data in data["quiz"].items():
    for question_id, question_data in category_data.items():
        question = question_data["question"]
        options = "\n".join([f"{idx}. {option}" for idx, option in enumerate(question_data["options"], start=1)])
        answer = question_data["answer"]
        
        table.add_row([category, question, options, answer])

print(table)