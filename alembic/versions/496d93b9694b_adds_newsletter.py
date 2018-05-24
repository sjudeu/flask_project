"""adds newsletter

Revision ID: 496d93b9694b
Revises: 3faf9d51249d
Create Date: 2018-05-24 13:31:34.952763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '496d93b9694b'
down_revision = '3faf9d51249d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "newsletter",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("email", sa.String, unique=True))


def downgrade():
    op.drop_table("newsletter")
