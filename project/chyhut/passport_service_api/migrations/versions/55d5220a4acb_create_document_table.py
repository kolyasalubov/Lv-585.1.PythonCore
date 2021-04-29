"""create document table

Revision ID: 55d5220a4acb
Revises: 6e206a40ac76
Create Date: 2019-11-06 22:57:44.201463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d5220a4acb'
down_revision = '6e206a40ac76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('data', sa.Binary(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document')
    # ### end Alembic commands ###
