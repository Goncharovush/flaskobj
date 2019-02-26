"""empty message

Revision ID: 15e33370d5d8
Revises: 
Create Date: 2019-02-21 22:26:00.533272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15e33370d5d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    # ### end Alembic commands ###
