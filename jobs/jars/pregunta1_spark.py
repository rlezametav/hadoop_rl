from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType


spark = SparkSession.builder\
    .appName("PersonExpensesWithCreditCard").getOrCreate()

schema = StructType([
    StructField("person", StringType(), True),
    StructField("payment_method", StringType(), True),
    StructField("money_spent", IntegerType(), True)]
)

df = spark.read.csv("data/input_spark_1.txt", sep=';', header=False, schema=schema)

result = df.filter(df.payment_method == "Tarjeta de crédito")\
    .groupBy("person").sum("money_spent")#\
    #.withColumnRenamed("sum(money_spent)", "total")

output = result.rdd.map(lambda row: f"{row[0]};{row[1]}").collect()

for line in output:
    print(line)

# df.select('person').distinct().alias('a')\
# .join(result.alias('b'), df.person == result.person, 'left')\
# .selectExpr(
#     'a.person',
#     'case when b.total is null then 0 else b.total end'
# ).show()

# result.write.csv('output/result1/', header = False, sep=';')


spark.stop()