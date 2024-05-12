"""empty message

Revision ID: b49789db3e2b
Revises: 
Create Date: 2024-05-06 17:20:18.325450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b49789db3e2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.String(length=255), nullable=False),
    sa.Column('appointment_date', sa.DateTime(), nullable=False),
    sa.Column('room_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('surname', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('identification', sa.Integer(), nullable=True),
    sa.Column('social_security', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('alergic', sa.Boolean(), nullable=True),
    sa.Column('medicated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('identification'),
    sa.UniqueConstraint('social_security')
    )
    op.create_table('speciality',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('alergic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('alergic_name', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id')
    )
    op.create_table('doctor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('surname', sa.String(length=120), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=True),
    sa.Column('identification', sa.Integer(), nullable=True),
    sa.Column('medical_license', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('speciality_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['speciality_id'], ['speciality.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('medicated',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('medicated_name', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patient_id')
    )
    op.create_table('attachment_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_file', sa.String(length=255), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctor_availability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('day_of_week', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medical_appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('speciality_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('appointment_date', sa.DateTime(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.ForeignKeyConstraint(['speciality_id'], ['speciality.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles_pictures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_picture', sa.String(length=255), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('doctor_id'),
    sa.UniqueConstraint('patient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles_pictures')
    op.drop_table('medical_appointment')
    op.drop_table('doctor_availability')
    op.drop_table('attachment_file')
    op.drop_table('medicated')
    op.drop_table('doctor')
    op.drop_table('alergic')
    op.drop_table('user')
    op.drop_table('speciality')
    op.drop_table('patient')
    op.drop_table('meetings')
    # ### end Alembic commands ###
