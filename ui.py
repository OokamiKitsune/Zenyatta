import os
from dotenv import load_dotenv
import gradio as gr
from ask import initialize_retrieval_pipeline, answer_question
from init import init_nlp_resources
from util.update import update_knowledge


# Access environment variables for application configuration
load_dotenv()
app_name = os.getenv('APP_NAME')
app_description = os.getenv('APP_DESCRIPTION')
print(app_name)

# Initialize everything before starting the UI
initialize_retrieval_pipeline()
update_knowledge()

iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=3, placeholder="Ask a question..."),
    outputs="text",
    title=app_name or "AI Assistant",
    description=app_description or "My custom AI Assistant",
)

if __name__ == "__main__":
    iface.launch(share=True)