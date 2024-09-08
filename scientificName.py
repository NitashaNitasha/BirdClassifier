import pandas as pd

# Load the dataset
df = pd.read_csv('birds-dataset/birds.csv')  # Assuming 'labels' and 'scientific name' columns exist

# Get scientific name for a specific bird label
def get_scientific_name(bird_name):
    bird_name = bird_name.upper()  # Convert to uppercase for consistency
    # Filter the DataFrame for the given bird label
    result = df[df['labels'].str.upper() == bird_name]
    if not result.empty:
        return result['scientific name'].values[0]
    else:
        return "Scientific name not found"

# Example usage
def main():
    bird_name = input("Bird for which scientific name you want to get: ")
    scientific_name = get_scientific_name(bird_name)
    print(f"Scientific Name of {bird_name} is: {scientific_name}")

if __name__ == '__main__':
    main()
