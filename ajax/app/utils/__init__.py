# converts sql row to dict
def build_object(row):
    d = {}
    if row is None:
        return d

    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


# converts sql rows to list of dicts
def build_objects(rows):
    return [build_object(row) for row in rows]


# helper for PATCH
def update_model(resource, model):
    for k, v in resource.items():
        if v is not None:
            model.__setattr__(k, v)