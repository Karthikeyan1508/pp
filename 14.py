from mrjob.job import MRJob
from mrjob.step import MRStep
import itertools

class MovieSimilarities(MRJob):

    def mapper(self, _, line):
        """Extracts genre and movie name from each line."""
        try:
            twitter_id, movie_name, genre = line.strip().split("::")
            yield genre, movie_name
        except ValueError:
            pass  # Handle improperly formatted lines

    def reducer(self, genre, movies):
        """Generates movie pairs and calculates similarity scores."""
        movie_list = list(movies)
        for movie1, movie2 in itertools.combinations(movie_list, 2):
            yield (movie1, movie2), self.calculate_similarity(movie1, movie2)

    def calculate_similarity(self, movie1, movie2):
        """Calculates a basic similarity score based on common words."""
        words1 = set(movie1.lower().split())
        words2 = set(movie2.lower().split())
        return len(words1 & words2)  # Number of common words

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == '__main__':
    MovieSimilarities.run()
