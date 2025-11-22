"""Initial migration.

Revision ID: 0001_initial
Revises: None
Create Date: 2025-11-22

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # ### commands auto generated - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(length=256), nullable=False, unique=True),
        sa.Column("username", sa.String(length=50), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(length=256), nullable=False),
        sa.Column("plan", sa.Enum('free','pro', name='plan_type'), nullable=False, server_default='free'),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("1")),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
    )
    op.create_table(
        "income_streams",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("income_type", sa.Enum('DIVIDEND','RENTAL','ROYALTY','INTEREST','BUSINESS','OTHER', name='income_type'), nullable=False),
        sa.Column("amount_per_period", sa.Float(), nullable=False),
        sa.Column("period", sa.String(length=32), nullable=False, server_default='monthly'),
        sa.Column("currency", sa.String(length=8), nullable=False, server_default='USD'),
        sa.Column("start_date", sa.Date(), nullable=True),
        sa.Column("notes", sa.String(length=1024), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    )
    # ### end commands ###

def downgrade() -> None:
    # ### commands auto generated - please adjust! ###
    op.drop_table("income_streams")
    op.drop_table("users")
    # ### end commands ###
