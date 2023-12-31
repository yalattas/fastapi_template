"""add app2

Revision ID: 3_02d8ce465cd5
Revises: 2_3f1adbd9fc04
Create Date: 2023-07-04 13:16:48.367926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3_02d8ce465cd5'
down_revision = '2_3f1adbd9fc04'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app2_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_app2_users_email'), 'app2_users', ['email'], unique=True)
    op.create_index(op.f('ix_app2_users_id'), 'app2_users', ['id'], unique=False)
    op.create_table('app2_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['app2_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_app2_items_id'), 'app2_items', ['id'], unique=False)
    op.create_index(op.f('ix_app2_items_title'), 'app2_items', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_app2_items_title'), table_name='app2_items')
    op.drop_index(op.f('ix_app2_items_id'), table_name='app2_items')
    op.drop_table('app2_items')
    op.drop_index(op.f('ix_app2_users_id'), table_name='app2_users')
    op.drop_index(op.f('ix_app2_users_email'), table_name='app2_users')
    op.drop_table('app2_users')
    # ### end Alembic commands ###
