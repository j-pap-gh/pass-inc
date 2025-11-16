
"""init

Revision ID: 0001
Revises:
Create Date: 2024-01-01 00:00:00
"""

from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("is_premium", sa.Boolean, default=False)
    )
    op.create_table(
        "ideas",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("description", sa.Text)
    )
    op.create_table(
        "plans",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("summary", sa.Text),
        sa.Column("capital", sa.String),
        sa.Column("timeframe", sa.String),
        sa.Column("risk", sa.String),
        sa.Column("details", sa.Text),
        sa.Column("steps", sa.Text),
    )

def downgrade() -> None:
    op.drop_table("plans")
    op.drop_table("ideas")
    op.drop_table("users")
