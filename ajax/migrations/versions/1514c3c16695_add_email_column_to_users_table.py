"""Add email column to users table

Revision ID: 1514c3c16695
Revises: 7516b38f2f58
Create Date: 2016-05-24 23:03:37.279793

"""

# revision identifiers, used by Alembic.
revision = '1514c3c16695'
down_revision = '7516b38f2f58'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'users',
        sa.Column('email', sa.VARCHAR(128), nullable=False)
    )


def downgrade():
    op.drop_column('users', 'email')
