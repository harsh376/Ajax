"""Add email-auth_type unique constraint

Revision ID: 222a81ae3abc
Revises: 64e96fb75a03
Create Date: 2016-05-28 18:53:33.461251

"""

# revision identifiers, used by Alembic.
revision = '222a81ae3abc'
down_revision = '64e96fb75a03'

from alembic import op


def upgrade():
    op.create_unique_constraint(
        'uq_email_auth_type',
        'users',
        ['email', 'external_auth_type'],
    )


def downgrade():
    op.drop_constraint(
        'uq_email_auth_type',
        'users',
        'unique',
    )
