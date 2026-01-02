import pandas as pd


# -------------------------------
# Load Dataset
# -------------------------------
def load_data(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError("Dataset file not found. Check the path.")


# -------------------------------
# Distance Proxy Score
# -------------------------------
def compute_distance_score(df: pd.DataFrame, source_city: str) -> pd.Series:
    source_city = source_city.strip().lower()

    source_row = df[df['City'].str.lower() == source_city]

    if source_row.empty:
        raise ValueError(f"Source city '{source_city}' not found in dataset.")

    source_state = source_row.iloc[0]['State']
    source_zone = source_row.iloc[0]['Zone']

    def score(row):
        if row['City'].lower() == source_city:
            return 0.0         
        elif row['State'] == source_state:
            return 1.5
        elif row['Zone'] == source_zone:
            return 0.5
        else:
            return 0.1

    return df.apply(score, axis=1)


# -------------------------------
# Ranking Logic
# -------------------------------
def rank_destinations(df: pd.DataFrame, source_city: str, top_n: int = 5) -> pd.DataFrame:
    df = df.copy()

    # Normalize rating (out of 5)
    df['rating_score'] = df['Google review rating'] / 5

    # Normalize popularity
    df['popularity_score'] = (
        df['Number of google review in lakhs'] /
        df['Number of google review in lakhs'].max()
    )

    # Distance score
    df['distance_score'] = compute_distance_score(df, source_city)

    # Final weighted score
    df['final_score'] = (
    0.30 * df['rating_score'] +
    0.30 * df['popularity_score'] +
    0.40 * df['distance_score']
)
    df['final_score'] = df['final_score'] / df['final_score'].max()


    # Remove source city from recommendations
    df = df[df['City'].str.lower() != source_city.lower()]

    ranked = df.sort_values(by='final_score', ascending=False)

    return ranked[['Name', 'City', 'State', 'final_score']].head(top_n)


# -------------------------------
# User Input
# -------------------------------
def get_user_cities() -> list:
    print("\nEnter 3 source cities (comma separated)")
    cities = input("Example: Delhi, Mumbai, Kolkata\n> ")

    city_list = [city.strip() for city in cities.split(",")]

    if len(city_list) != 3:
        raise ValueError("Please enter exactly 3 cities.")

    return city_list


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    try:
        data = load_data("data/Top Indian Places to Visit.csv")

        print("\nAvailable Cities:")
        print(", ".join(sorted(data['City'].unique())))
        print("-" * 60)

        cities = get_user_cities()

        with open("output/sample_output.txt", "w", encoding="utf-8") as f:
            for city in cities:
                f.write(f"\nTop Weekend Getaways from {city}:\n")
                f.write("-" * 40 + "\n")

                results = rank_destinations(data, city)
                f.write(results.to_string(index=False))
                f.write("\n\n")

        print("\nRecommendation results saved to output/sample_output.txt")

    except Exception as e:
        print(f"\nError: {e}")
