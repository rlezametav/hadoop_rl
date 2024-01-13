from mrjob.job import MRJob
import mrjob
# from collections import defaultdict

class CitationAnalysis(MRJob):

    OUTPUT_PROTOCOL = mrjob.protocol.RawValueProtocol

    def mapper_init(self):
        """
        Skip the header row by setting a flag to True after reading the first line.
        """
        self.skip_header = True

    def mapper(self, _, line):
        """
        Skip the header row and yield (cited_article, citing_article) pairs for subsequent lines.
        """
        if self.skip_header:
            self.skip_header = False
            return

        citing, cited = line.strip().split(",")
        yield cited, citing

    def reducer(self, key, values):
        """
        Reducer function remains the same.
        """
        yield None, f'{key}    {",".join(sorted(values))}'

if __name__ == "__main__":
    CitationAnalysis.run()