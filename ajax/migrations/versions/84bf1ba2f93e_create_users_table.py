"""create users table

Revision ID: 84bf1ba2f93e
Revises: 
Create Date: 2016-03-25 10:59:03.185323

"""

# revision identifiers, used by Alembic.
revision = '84bf1ba2f93e'
down_revision = None

from alembic import op
import sqlalchemy as sa

from app.utils.alchemy import UUID


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', UUID, primary_key=True, nullable=False),
        sa.Column('name', sa.VARCHAR(191), nullable=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4',
    )


def downgrade():
    op.drop_table('users')
