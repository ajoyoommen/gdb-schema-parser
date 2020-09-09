import sys

from dse_parser import DSESchema


if __name__ == "__main__":
    filename = sys.argv[1]

    schema = DSESchema()

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        if not line.startswith("schema."):
            continue

        line = line.split("//")[0]
        try:
            exec(line)
        except Exception as e:
            print(line, e)

    print(schema.schema)
