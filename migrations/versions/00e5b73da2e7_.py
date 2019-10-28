"""empty message

Revision ID: 00e5b73da2e7
Revises: c65ff24923a6
Create Date: 2019-10-24 22:15:14.369197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e5b73da2e7'
down_revision = 'c65ff24923a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_skills_skill_id_fkey', 'users_skills', type_='foreignkey')
    op.drop_constraint('users_skills_user_id_fkey', 'users_skills', type_='foreignkey')
    op.create_foreign_key(None, 'users_skills', 'skill', ['skill_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'users_skills', 'person', ['user_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users_skills', type_='foreignkey')
    op.drop_constraint(None, 'users_skills', type_='foreignkey')
    op.create_foreign_key('users_skills_user_id_fkey', 'users_skills', 'person', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('users_skills_skill_id_fkey', 'users_skills', 'skill', ['skill_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
