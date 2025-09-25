import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

filepath = 'study_rankings.csv'
filepath2 = 'study_medians.csv'

# Custom color palette
custom_pallette = {
    'o3-generated': '#FF9999',
    'MyEdit': '#99FF99',
    'Real_Recording': '#9999FF',
    'HDB': "#99FFFF"
}

def plot_violin_total(filepath):
    # Load the data
    data = pd.read_csv(filepath)

    # Drop empty columns
    data = data.dropna()

    # Filter relevant columns
    data = data[['pattern', 'score']]

    data.columns = ['Pattern-Type', 'Score']


    # Create violin plot
    plt.figure(figsize=(12, 6))
    sns.violinplot(x='Pattern-Type', y='Score', data=data, palette=custom_pallette, cut=0)
    plt.title("Violin Plot of Scores per Pattern across all Participants and Materials")
    plt.xlabel("Pattern-Type")
    plt.ylabel("Ranking Score (1-4)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_violin_per_material(filepath):
    
    # Load data
    data = pd.read_csv(filepath)
    data = data.dropna()

    # Adjust column names if necessary
    data = data.rename(columns={
        'pattern': 'Pattern-Type',
        'score': 'Score',
        'material': 'Material'  # <-- Make sure this matches your actual CSV column name!
    })


    # Get all unique materials
    materials = data['Material'].unique()

    for material in materials:
        plt.figure(figsize=(12, 6))
        material_data = data[data['Material'] == material]
        sns.violinplot(
            x='Pattern-Type',
            y='Score',
            data=material_data,
            palette=custom_pallette,
            cut=0
        )
        plt.title(f"Violin Plot of Scores per Pattern for Material: {material}")
        plt.xlabel("Pattern-Type")
        plt.ylabel("Ranking Score (1-4)")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def plot_medians():

    # Input data
    data = {
        "material": ["ceramic","denim","felt","glass","leather","metal",
                    "plastic","stone","water","wood"],
        "o3-generated": [4,2,None,2,2,2.5,1,1.5,None,1.5],
        "MyEdit": [2,2,None,2,2,3.25,2,2,None,3],
        "Real_Recording": [3,3,None,3,2,2.25,3,3,None,3],
        "HDB": [2,2,None,1,4,2.25,4,4,None,2.5]
    }
    df = pd.DataFrame(data)

    # Reshape into long form
    df_melted = df.melt(id_vars="material", var_name="method", value_name="median_score")


    # Plot
    plt.figure(figsize=(8,6))
    sns.violinplot(
        x="method", 
        y="median_score", 
        data=df_melted, 
        inner="box", 
        cut=0,
        palette=custom_pallette
    )

    plt.title("Violin Plot of Medians per Generation Method (across materials)")
    plt.xlabel("Generation Method")
    plt.ylabel("Median Score")
    plt.tight_layout()
    plt.show()





#plot_violin_total(filepath)
#plot_violin_per_material(filepath)
#plot_medians()