"""empty message

Revision ID: bd5a72606bda
Revises: 
Create Date: 2021-11-12 19:17:48.334175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5a72606bda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('age', sa.String(length=10), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('avatar', sa.Text(), nullable=True),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('imgs', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['shop_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('imgs', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Text(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('imgs', sa.Text(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reply',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('ctime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    op.drop_table('goods')
    op.drop_table('comment')
    op.drop_table('shop')
    op.drop_table('user')
    op.drop_table('shop_type')
    # ### end Alembic commands ###