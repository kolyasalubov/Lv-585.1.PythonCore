"""add created_at column for order

Revision ID: 18843cf5583e
Revises: 54fbbf63a587
Create Date: 2019-11-21 12:26:04.392814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18843cf5583e'
down_revision = '54fbbf63a587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('created_at', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'created_at')
    # ### end Alembic commands ###