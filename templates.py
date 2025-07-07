import os

# Define the folder and file structure
structure = {
    'static': {},
    'src': {
        'api': {
            '__init__.py': '',
            'papers.py': '',
            'notes.py': '',
            'rag.py': '',
            'summarize.py': '',
        },
        'models': {
            '__init__.py': '',
            'schemas.py': '',
            'db.py': '',
            'summarizer': {
                '__init__.py': '',
                'model.py': '',
                'train.py': '',
                'utils.py': '',
            },
            'rag': {
                '__init__.py': '',
                'retriever.py': '',
                'generator.py': '',
            },
        },
        'services': {
            '__init__.py': '',
            'recommender.py': '',
            'paper_service.py': '',
            'note_service.py': '',
            'rag_service.py': '',
            'summarize_service.py': '',
        },
        'utils': {
            '__init__.py': '',
            'logger.py': '',
            'exception.py': '',
        },
    },
    'tests': {
        'api': {},
        'models': {},
        'services': {},
    },
    'app.py': '',
    'requirements.txt': '',
    'README.md': '',
    'setup.py': '',
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Only create file if it doesn't exist
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    create_structure(base, structure)
    print('Folders and files created successfully!')
