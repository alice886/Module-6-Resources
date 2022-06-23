""" create User, Joke and likes tables

Revision ID: 50e4f5fbf2c3
Revises: 
Create Date: 2022-06-16 12:30:22.886362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50e4f5fbf2c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('jokes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('joke_body', sa.String(length=255), nullable=False),
    sa.Column('punchline', sa.String(length=255), nullable=False),
    sa.Column('rating', sa.String(length=10), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('users', sa.Integer(), nullable=False),
    sa.Column('jokes', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['jokes'], ['jokes.id'], ),
    sa.ForeignKeyConstraint(['users'], ['users.id'], ),
    sa.PrimaryKeyConstraint('users', 'jokes')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    op.drop_table('jokes')
    op.drop_table('users')
    # ### end Alembic commands ###