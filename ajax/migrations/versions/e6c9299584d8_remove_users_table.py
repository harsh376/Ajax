"""Remove users table

Revision ID: e6c9299584d8
Revises: 1514c3c16695
Create Date: 2016-05-27 21:03:12.546687

"""

# revision identifiers, used by Alembic.
revision = 'e6c9299584d8'
down_revision = '1514c3c16695'

from alembic import op
import sqlalchemy as sa

from app.utils.alchemy import UUID


def upgrade():
    op.drop_table('users')


def downgrade():
    op.create_table(
        'users',
        sa.Column('id', UUID, primary_key=True, nullable=False),
        sa.Column('name', sa.VARCHAR(191), nullable=False),
        sa.Column('email', sa.VARCHAR(128), nullable=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4',
    )
