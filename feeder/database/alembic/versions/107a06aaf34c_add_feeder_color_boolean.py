"""Add feeder color boolean

Revision ID: 107a06aaf34c
Revises: bfe421f787d4
Create Date: 2020-12-25 16:26:59.643936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107a06aaf34c'
down_revision = 'bfe421f787d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    connection = op.get_bind()
    connection.execute('pragma foreign_keys=OFF')
    with op.batch_alter_table('kronos_device', schema=None) as batch_op:
        batch_op.add_column(sa.Column('black', sa.Boolean(), nullable=True))
    connection.execute('pragma foreign_keys=ON')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    connection = op.get_bind()
    connection.execute('pragma foreign_keys=OFF')
    with op.batch_alter_table('kronos_device', schema=None) as batch_op:
        batch_op.drop_column('black')
    connection.execute('pragma foreign_keys=ON')

    # ### end Alembic commands ###
