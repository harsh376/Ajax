import json
import uuid
import pytz

from datetime import datetime, time

from sqlalchemy.types import (
    TypeDecorator,
    INTEGER,
    VARBINARY,
    VARCHAR,
    TEXT,
    FLOAT,
    TIME,
)


class UnboundTypeDecorator(TypeDecorator):

    def result_processor(self, dialect, coltype):
        return lambda value: self.process_result_value(value, dialect)

    def bind_processor(self, dialect):
        """ Simple override to avoid pre-processing before
        process_bind_param. This is for when the Python type can't
        be easily coerced into the `impl` type."""
        return lambda value: self.process_bind_param(value, dialect)


class UnixTimestamp(UnboundTypeDecorator):
    impl = INTEGER

    def process_bind_param(self, value, dialect):
        # datetime.timestamp returns a float
        return value if value is None else int(value.timestamp())

    def process_result_value(self, value, dialect):
        return value if value is None else (datetime.utcfromtimestamp(value)
                                                    .replace(tzinfo=pytz.UTC))


class UnixTimestampHires(UnboundTypeDecorator):
    """ Unix timestamp with microsecond resolution. Older mysql versions have
    a TIMESTAMP/DATETIME with second resolution. Represented as a DOUBLE in
    the database. Result is a naive datetime.
    """

    impl = FLOAT(53)

    def process_bind_param(self, value, dialect):
        return value if value is None else value.replace(
            tzinfo=pytz.UTC).timestamp()

    def process_result_value(self, value, dialect):
        return value if value is None else datetime.utcfromtimestamp(value)


class UUID(UnboundTypeDecorator):
    """ A memory-efficient MySQL UUID-type. """

    impl = VARBINARY(16)

    def process_bind_param(self, value, dialect):
        """ Emit the param in hex notation. """
        value = uuid.UUID(str(value))
        return value if value is None else value.bytes

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            assert len(value) == 16, "Expected 16 bytes, got %d" % len(value)
            return uuid.UUID(bytes=value)


class JSON(UnboundTypeDecorator):
    """ Introduces a complex JSON-type for MySQL.
    This is valuable for storing complex, immutable data, while avoiding joins.
    Then rather than having separate serialization schemes for separate
    services, a single one can be used that works for most Python objects.
    """

    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        return value if value is None else json.dumps(value, sort_keys=True)

    def process_result_value(self, value, dialect):
        return value if value is None else json.loads(value)


class TEXTJSON(JSON):
    impl = TEXT


class Time(TypeDecorator):
    """Platform-independent Time type.
    """
    impl = TEXT

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(TIME())
        else:
            return dialect.type_descriptor(TEXT())

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'mysql':
            return value
        else:
            return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'mysql':
            return value
        else:
            return time(*list(map(int, value.split(':'))))
