"""add to client age field

Revision ID: 41031ee5a6cd
Revises: 09c220b82855
Create Date: 2022-02-26 12:13:32.574726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41031ee5a6cd'
down_revision = '09c220b82855'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'age')
    # ### end Alembic commands ###
