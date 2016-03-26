"""Create items table

Revision ID: 7516b38f2f58
Revises: 84bf1ba2f93e
Create Date: 2016-03-25 22:17:57.435511

"""

# revision identifiers, used by Alembic.
revision = '7516b38f2f58'
down_revision = '84bf1ba2f93e'

from alembic import op
import sqlalchemy as sa

from app.utils.alchemy import UUID


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', UUID, primary_key=True, nullable=False),
        sa.Column('name', sa.VARCHAR(191), nullable=False),
        sa.Column('order', sa.INTEGER, nullable=False, default=0),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4',
    )


def downgrade():
    op.drop_table('items')
