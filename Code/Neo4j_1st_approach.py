#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install neo4j """in case not installed """


# In[9]:


from neo4j import GraphDatabase

# Function to connect to Neo4j and run a query
def run_query(uri, username, password, query):
    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            result = session.run(query)
            return result.data()

# Example usage
neo4j_uri = "bolt://localhost:7687/db/SAMPLE_1"  # Update with your Neo4j server URI
neo4j_username = "neo4j"  # Update with your Neo4j username
neo4j_password = "password"  # Update with your Neo4j password

user_input = input("Enter something: ")

# Example query

query = f"""MATCH (t1:TRACK {{track_name: '{user_input}'}})-[:BELONGS_TO]->(genre:Genre)
MATCH (t2:TRACK)-[:BELONGS_TO]->(genre) WHERE t1 <> t2
WITH t1, t2,
     gds.similarity.euclidean(
       [t1.acousticness, t1.danceability, t1.instrumentalness, t1.loudness, t1.popularity, t1.valence, t1.tempo, t1.speechiness, t1.liveness, t1.energy],
       [t2.acousticness, t2.danceability, t1.instrumentalness, t2.loudness, t2.popularity, t1.valence, t2.tempo, t2.speechiness, t2.liveness, t2.energy]
     ) AS euclideanSimilarity
ORDER BY euclideanSimilarity DESC
RETURN t2.track_name AS recommendedTrack, euclideanSimilarity
LIMIT 5; """

# Run the query
result_data = run_query(neo4j_uri, neo4j_username, neo4j_password, query)

# Print the results
for record in result_data:
    print(record)

