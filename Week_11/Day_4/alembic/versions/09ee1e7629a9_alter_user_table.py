"""alter user table

Revision ID: 09ee1e7629a9
Revises: 
Create Date: 2025-10-23 11:21:36.602693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09ee1e7629a9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass




# def upgrade() -> None:
#     op.add_column('users', sa.Column('gender', sa.String(20), nullable=True))
# def downgrade() -> None:
#     op.drop_column('users', 'gender')

















































