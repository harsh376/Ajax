def build_object(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


def build_objects(rows):
    return [build_object(row) for row in rows]
