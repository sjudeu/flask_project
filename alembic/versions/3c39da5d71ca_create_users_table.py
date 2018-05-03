"""Create users table

Revision ID: 3c39da5d71ca
Revises: 
Create Date: 2018-05-01 16:33:23.091321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c39da5d71ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "user",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")

