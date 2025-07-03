import gradio as gr
from ask import initialize_retrieval_pipeline, answer_question

# Initialize everything before starting the UI
initialize_retrieval_pipeline()

iface = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=3, placeholder="Ask a question about inventory..."),
    outputs="text",
    title="Warehouse Assistant",
    description="Ask questions about warehouse inventory, network equipment, and processes."
)

if __name__ == "__main__":
    iface.launch(share=True)