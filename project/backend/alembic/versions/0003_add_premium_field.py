
"""ensure premium flag exists

Revision ID: 0003
Revises: 0002
Create Date: 2024-01-01 00:30:00
"""

from alembic import op
import sqlalchemy as sa

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("is_premium", sa.Boolean, nullable=False, server_default="0")
    )

def downgrade() -> None:
    op.drop_column("users", "is_premium")
