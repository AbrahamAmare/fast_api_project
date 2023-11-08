"""add cols to posts table

Revision ID: ec04edcfe4d0
Revises: fe388b616075
Create Date: 2023-11-08 14:15:34.913487

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec04edcfe4d0'
down_revision: Union[str, None] = 'fe388b616075'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('isPublished', sa.Boolean(), nullable=False, server_default='False'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'isPublished')
    op.drop_column('posts', 'created_at')
    pass
