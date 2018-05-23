"""adds html render to article table

Revision ID: 3faf9d51249d
Revises: 3c39da5d71ca
Create Date: 2018-05-23 11:12:52.314040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3faf9d51249d'
down_revision = '3c39da5d71ca'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
            sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")
