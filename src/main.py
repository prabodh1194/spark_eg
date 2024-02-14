import pandas as pd
from deltalake import DeltaTable
from deltalake.writer import write_deltalake

df = pd.DataFrame(range(5))  # Create Pandas DataFrame
write_deltalake("/tmp/deltars_table", df)  # Write Delta Lake table
df = pd.DataFrame(range(6, 11))  # Generate new data
write_deltalake("/tmp/deltars_table", \
                df, mode="append")  # Append new data
dt = DeltaTable("/tmp/deltars_table")  # Read Delta Lake table
dt.to_pandas()  # Show Delta Lake table
