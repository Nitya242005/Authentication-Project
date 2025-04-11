
from core.models import Interaction, Athlete
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

def get_recommendations(scout_id, num_recommendations=5):
    interactions = Interaction.objects.filter(scout_id=scout_id)
    all_athletes = list(Athlete.objects.all().values())

    if not interactions.exists():
        return all_athletes[:num_recommendations]  # fallback if no interaction

    liked_athlete_ids = interactions.filter(action='shortlisted').values_list('athlete_id', flat=True)
    liked_athletes = Athlete.objects.filter(id__in=liked_athlete_ids).values()

    df = pd.DataFrame(liked_athletes)
    if df.empty or 'age' not in df.columns:
        return all_athletes[:num_recommendations]

    # Select features for clustering
    feature_columns = ['age', 'sport', 'level']
    for col in feature_columns:
        if col not in df.columns:
            df[col] = ""

    # Encode categorical features
    for col in ['sport', 'level']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

    X = df[feature_columns]
    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(X)

    # Get cluster of a typical liked athlete
    cluster_label = kmeans.predict([X.iloc[0]])[0]

    # Prepare all athletes for matching
    all_df = pd.DataFrame(all_athletes)
    for col in feature_columns:
        if col not in all_df.columns:
            all_df[col] = ""

    # Apply same encoding to full dataset
    for col in ['sport', 'level']:
        le = LabelEncoder()
        all_df[col] = le.fit_transform(all_df[col].astype(str))

    all_X = all_df[feature_columns]
    all_df['cluster'] = kmeans.predict(all_X)

    # Filter athletes in the same cluster
    recommended = all_df[all_df['cluster'] == cluster_label]
    return recommended.head(num_recommendations).to_dict(orient='records')
