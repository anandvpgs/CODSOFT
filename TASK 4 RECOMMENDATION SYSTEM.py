import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample data for movies, books, and products
movies_data = {
    'ItemID': [1, 2, 3, 4, 5],
    'Title': ['GOAT', 'KANGUVA', 'AMAMRAN', 'THUG LIFE', 'VIDAMUYARCHI'],
 'Features': ['Drama, Prison', 'Crime, Drama, Mafia', 'Action, Crime, Drama, Superhero', 'Crime, Drama, Nonlinear', 'Drama, Romance, Historical']
}

books_data = {
    'ItemID': [101, 102, 103, 104, 105],
    'Title': ['TAMIL ILAKIYAM', 'KADHAL ', 'ANBU', 'ULAGAM', 'MANIDHARGAL'],
     'Features': ['Fiction, Classic, Legal', 'Fiction, Dystopian, Political', 'Fiction, Romance, Classic', 'Fiction, Classic, Jazz Age', 'Fiction, Coming-of-age, Classic']

}

products_data = {
    'ItemID': [201, 202, 203, 204, 205],
    'Title': ['Smartphone X', 'Laptop Y', 'Headphones Z', 'Smartwatch A', 'Tablet B'],
     'Features': ['Electronics, Mobile, High-performance', 'Electronics, Computer, Portable', 'Electronics, Audio, Wireless', 'Electronics, Wearable, Fitness', 'Electronics, Portable, Touchscreen']
    }


# Function to create a recommendation system for a given category
def create_recommendation_system(data):
    df = pd.DataFrame(data)
    cv = CountVectorizer()
    feature_matrix = cv.fit_transform(df['Features'])
    cosine_sim = cosine_similarity(feature_matrix)

    def get_recommendations(item_title, top_n=5):
        idx = df.index[df['Title'] == item_title].tolist()[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        item_indices = [i[0] for i in sim_scores]
        return df['Title'].iloc[item_indices].tolist()

    return get_recommendations, df['Title'].tolist()

# Create recommendation systems for each category
movie_recommender, movie_titles = create_recommendation_system(movies_data)
book_recommender, book_titles = create_recommendation_system(books_data)
product_recommender, product_titles = create_recommendation_system(products_data)

def print_recommendations(category, item, recommendations):
    print(f"\nRecommendations for users who liked '{item}' ({category}):")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")

def main():
    while True:
        print("\nMulti-Category Recommendation System")
        print("1. Movies")
        print("2. Books")
        print("3. Products")
        print("4. Exit")

        choice = input("Choose a category (1-4): ")

        if choice == '4':
            print("Thank you for using the recommendation system. Goodbye!")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        category = ['Movies', 'Books', 'Products'][int(choice) - 1]
        recommender = [movie_recommender, book_recommender, product_recommender][int(choice) - 1]
        titles = [movie_titles, book_titles, product_titles][int(choice) - 1]

        print(f"\nAvailable {category}:")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")

        item_choice = input(f"\nChoose a {category[:-1]} (1-{len(titles)}): ")
        if not item_choice.isdigit() or int(item_choice) < 1 or int(item_choice) > len(titles):
            print("Invalid choice. Please try again.")
            continue

        selected_item = titles[int(item_choice) - 1]
        recommendations = recommender(selected_item)
        print_recommendations(category, selected_item, recommendations)

if __name__ == "__main__":
    main()
