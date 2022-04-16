def row_to_dict(object):
    row = {}
    for column in object.__table__.columns:
        row[column.name] = str(getattr(object, column.name))

    return row
