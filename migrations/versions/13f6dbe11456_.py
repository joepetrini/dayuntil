"""empty message

Revision ID: 13f6dbe11456
Revises: None
Create Date: 2014-12-05 12:56:13.094584

"""

# revision identifiers, used by Alembic.
revision = '13f6dbe11456'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('twitter_id', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=True),
    sa.Column('profile_url', sa.String(length=255), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('days',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('sys_name', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('alt_names', sa.String(length=255), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=1000), nullable=True),
    sa.Column('link_title', sa.String(length=255), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_days_sys_name'), 'days', ['sys_name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_days_sys_name'), table_name='days')
    op.drop_table('days')
    op.drop_table('users')
    op.drop_table('facts')
    ### end Alembic commands ###