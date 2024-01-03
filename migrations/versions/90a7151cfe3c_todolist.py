"""ToDoList

Revision ID: 90a7151cfe3c
Revises:
Create Date: 2024-01-03 12:40:18.297915
"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '90a7151cfe3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    tbl_status = op.create_table(
        'to_do_status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(50), nullable=False),
    )

    op.bulk_insert(
        tbl_status,
        [
            {'description': 'Pending'},
            {'description': 'Done'},
            {'description': 'Canceled'},
        ],
    )

    tbl_list = op.create_table(
        'to_do_list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(50), nullable=False),
        sa.Column(
            'to_do_status_id',
            sa.Integer,
            sa.ForeignKey('to_do_status.id'),
            nullable=False,
            default=1,
        ),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )

    op.bulk_insert(
        tbl_list,
        [
            {
                'description': 'Develop my amazing Flask App!',
                'created_at': datetime.now(),
            },
        ],
    )


def downgrade():
    op.drop_table('to_do_list')
    op.drop_table('to_do_status')
