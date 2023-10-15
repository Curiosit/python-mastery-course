import reader
port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])