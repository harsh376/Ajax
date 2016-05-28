"""Create users table again

Revision ID: 64e96fb75a03
Revises: e6c9299584d8
Create Date: 2016-05-27 21:12:41.183270

"""

# revision identifiers, used by Alembic.
revision = '64e96fb75a03'
down_revision = 'e6c9299584d8'

from alembic import op
import sqlalchemy as sa

from app.utils.alchemy import UUID


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', UUID, primary_key=True, nullable=False),
        sa.Column('first_name', sa.VARCHAR(128), nullable=False),
        sa.Column('last_name', sa.VARCHAR(128)),
        sa.Column('email', sa.VARCHAR(128), nullable=False),
        sa.Column('photo_url', sa.VARCHAR(1024)),
        sa.Column('external_auth_type', sa.VARCHAR(128), nullable=False),
        sa.Column('external_auth_id', sa.VARCHAR(128), nullable=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4',
    )


def downgrade():
    op.drop_table('users')
