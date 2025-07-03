# Initialize the application and download all NLP resources

from nltk import download

def init_nlp_resources():
    """
    Initialize the NLP resources needed for the application.
    This function downloads necessary NLTK resources.
    """
    try :
        download("punkt", quiet=True)
        download("stopwords", quiet=True)

    except Exception as e:
        print(f"Error initializing NLP resources: {e}")
        raise
    print("NLP resources initialized successfully.")
