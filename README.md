# Music-Recommendation-on-Neo4j

__Approaches to Node Relationship Establishment: A Comparative Analysis__

In the context of building a recommendation system for music tracks, we have explored two distinct approaches, each emphasizing different aspects of data representation and retrieval efficiency.

__1. Genre and Artist-Based Relationships:__

Our initial strategy involved establishing explicit relationships between nodes (songs) based on genre and artist associations. This method began with the creation of genre and artist nodes, followed by connecting individual tracks to their respective genres and artists. Subsequently, the database was queried to extract recommended songs based on genre and artist relationships. This approach prioritizes the inherent organizational structure of music, emphasizing genre and artist affiliations.

![image](https://github.com/kumarsauravjha/Music-Recommendation-on-Neo4j/assets/143224932/a053fcc5-d29d-4441-9236-46f559ff5f87)

![image](https://github.com/kumarsauravjha/Music-Recommendation-on-Neo4j/assets/143224932/0a294367-91ba-4fe6-a520-fb23b1aed3b7)


__2. Similarity-Based Relationships using Machine Learning:__

The second approach adopted a machine learning algorithm to infer similarity-based relationships between tracks. Leveraging a sampled dataset derived from the extensive Spotify dataset, we utilized a graph data science library to compute Euclidean similarity scores between tracks. Subsequently, the database was queried to retrieve recommended songs based on these similarity scores. This approach focuses on leveraging machine learning to establish implicit connections between songs, potentially uncovering less evident relationships.

![image](https://github.com/kumarsauravjha/Music-Recommendation-on-Neo4j/assets/143224932/0fcdc44a-cfd8-4d44-88ae-cfdf977c1d0e)

__Data Preprocessing:__

Prior to establishing relationships, a dataset comprising 19,432 rows (Spotify_ft.csv) was sampled from the original Spotify dataset, which consists of 176,774 rows. The selection of relevant columns was performed, and the data was appropriately scaled using Python to ensure uniformity and comparability.

__Programming Languages Used:__

The coding implementations were carried out using Python for data preprocessing and Cypher Query Language (CQL) for interacting with the Neo4j graph database. A separate Python file (.pynb) will be provided to showcase the Python code in detail. This comprehensive methodology allows for a nuanced exploration of the strengths and considerations associated with both relational and similarity-based approaches within the context of music recommendation systems.
