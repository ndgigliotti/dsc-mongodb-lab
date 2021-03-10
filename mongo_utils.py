def delete_empty_keys(record: dict):
    for key in list(record.keys()):
        if record[key] is None:
            del record[key]