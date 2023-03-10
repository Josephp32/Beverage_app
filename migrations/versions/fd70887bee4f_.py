"""empty message

Revision ID: fd70887bee4f
Revises: 5b46e737b17f
Create Date: 2023-03-02 14:20:39.324272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd70887bee4f'
down_revision = '5b46e737b17f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('drink', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.String(length=150), nullable=False))
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('drink', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
        batch_op.drop_column('size')

    # ### end Alembic commands ###
