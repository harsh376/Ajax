import json


# converts sql row to dict
def build_object(row):
    d = {}
    if row is None:
        return d

    for column in row.__table__.columns:
        # TODO: Need try-except for python2.7 inside docker container
        # After figuring out venv inside docker, relative imports
        # remove this hack
        try:
            a = str(getattr(row, column.name))
        except UnicodeEncodeError:
            a = getattr(row, column.name).encode('utf-8')
        d[column.name] = a

    return d


# converts sql rows to list of dicts
def build_objects(rows):
    return [build_object(row) for row in rows]


# helper for PATCH
def update_model(resource, model):
    for k, v in resource.items():
        if v is not None:
            model.__setattr__(k, v)


# converts returned data to json; used in tests
def to_json(data):
    return json.loads(data.data.decode('utf8'))
