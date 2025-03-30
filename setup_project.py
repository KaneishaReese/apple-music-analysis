import os

def create_project_structure():
    project_structure = {
        "data": ["raw", "processed", "interim", "external"],
        "notebooks": [],
        "scripts": [],
        "reports": ["figures"],
        "models": [],
        "references": []
    }
    
    base_path = os.getcwd()
    
    for folder, subfolders in project_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for subfolder in subfolders:
            os.makedirs(os.path.join(folder_path, subfolder), exist_ok=True)
    
    # Create empty files
    files_to_create = [
        "README.md", "requirements.txt", ".gitignore", "config.yaml"
    ]
    
    for file in files_to_create:
        with open(os.path.join(base_path, file), "w") as f:
            pass  # Create empty files
    
    print("Project structure has been set up successfully!")

if __name__ == "__main__":
    create_project_structure()

## Creates the file structure seen below into folder this file is located within.
# data-analysis-project/
# │── data/                    # Raw and processed data
# │   ├── raw/                 # Original, unmodified data
# │   ├── processed/           # Cleaned or transformed data
# │   ├── interim/             # Intermediate files (optional)
# │   ├── external/            # External datasets (if any)
# │
# │── notebooks/               # Jupyter notebooks for analysis
# │
# │── scripts/                 # Python scripts for automation
# │
# │── reports/                 # Generated reports and presentations
# │   ├── figures/             # Saved plots/images
# │
# │── models/                  # Trained models (if applicable)
# │
# │── references/              # Documentation, research papers, links
# │
# │── requirements.txt         # Required Python libraries
# │── README.md                # Project overview and instructions
# │── .gitignore               # Files to ignore in version control
# │── config.yaml              # Configuration settings (if needed)