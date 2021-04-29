"""added Product model

Revision ID: 9844f39bbc1d
Revises: 159e562d8c3f
Create Date: 2021-04-29 11:25:46.212619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9844f39bbc1d'
down_revision = '159e562d8c3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('tax', sa.Float(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###