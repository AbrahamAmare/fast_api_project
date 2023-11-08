"""add content col to posts table

Revision ID: 335c7a7d3815
Revises: 460a277c1184
Create Date: 2023-11-08 11:30:09.569335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '335c7a7d3815'
down_revision: Union[str, None] = '460a277c1184'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
