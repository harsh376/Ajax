"""create user_v2 table

Revision ID: 8793bd307961
Revises: 222a81ae3abc
Create Date: 2016-12-26 13:48:36.992428

"""

# revision identifiers, used by Alembic.
revision = '8793bd307961'
down_revision = '222a81ae3abc'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

from app.utils.alchemy import UUID


def upgrade():
    op.create_table(
        'users_v2',
        sa.Column('id', UUID, primary_key=True, nullable=False),
        sa.Column('email', sa.VARCHAR(128), nullable=False, unique=True),
        sa.Column('password', sa.VARCHAR(1024), nullable=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4',
    )


def downgrade():
    op.drop_table('users_v2')
