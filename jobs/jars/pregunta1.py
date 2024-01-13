from mrjob.job import MRJob
from mrjob.step import MRStep
import mrjob


class AverageJob(MRJob):

    OUTPUT_PROTOCOL = mrjob.protocol.RawValueProtocol

    def mapper(self, _, line):
        # Split the line by ";"
        key1, key2, value = line.split(";")

        # Check if value is a valid integer
        try:
            value = int(value)
        except ValueError:
            # Ignore invalid values
            return

        # Emit key-value pairs where key is a tuple of (key1, key2) and value is (1, value)
        yield (key1, key2), (1, value)

    def reducer(self, key, values):
        # Initialize total sum and count
        total_sum = 0
        count = 0

        # Iterate over values and accumulate sum and count
        for value_tuple in values:
            count += value_tuple[0]
            total_sum += value_tuple[1]

        # Calculate and format the average
        average = total_sum / count
        formatted_average = f"{average:.0f}"  # Format average to two decimal places

        # Combine key and formatted average
        output_key = ";".join(key)
        output_value = f"{output_key};{formatted_average}"

        # Emit the final key-value pair
        yield (None, output_value)

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            )
        ]

if __name__ == '__main__':
    AverageJob.run()