
"""add optional metadata to ideas

Revision ID: 0002
Revises: 0001
Create Date: 2024-01-01 00:15:00
"""

from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column("ideas", sa.Column("category", sa.String, nullable=True))
    op.add_column("ideas", sa.Column("difficulty", sa.String, nullable=True))

def downgrade() -> None:
    op.drop_column("ideas", "difficulty")
    op.drop_column("ideas", "category")
