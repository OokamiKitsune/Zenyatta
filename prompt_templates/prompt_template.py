from langchain.prompts import PromptTemplate
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(script_dir, 'prompt_template.txt')

with open(template_path, 'r', encoding='utf-8') as file:
    prompt_template_text = file.read().strip()

prompt_template = PromptTemplate.from_template(prompt_template_text)