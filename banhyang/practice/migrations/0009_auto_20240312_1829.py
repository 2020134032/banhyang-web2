# Generated by Django 3.0.4 on 2024-03-12 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0008_auto_20240312_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceCheck',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arrival_time', models.TimeField(auto_now_add=True)),
                ('timetable_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendancecheck', to='practice.Timetable')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendancecheck', to='practice.PracticeUser')),
            ],
        ),
        migrations.AlterField(
            model_name='session',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session', to='practice.PracticeUser'),
        ),
        migrations.DeleteModel(
            name='ArrivalTime',
        ),
    ]
