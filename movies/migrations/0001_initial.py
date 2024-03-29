import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                 help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                 max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                 help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(
                    default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hall_type', models.CharField(choices=[
                 ('2D', '2D'), ('3D', '3D'), ('4DX', '4DX'), ('IMAX', 'IMAX')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('poster', models.ImageField(null=True, upload_to='images/posters')),
                ('about', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.JSONField(default={'A': {'1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}, 'B': {'1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}, 'C': {'1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}, 'D': {
                 '1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}, 'E': {'1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}, 'F': {'1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}, 'G': {'1': 'Vacant', '2': 'Vacant', '3': 'Vacant', '4': 'Vacant', '5': 'Vacant', '6': 'Vacant', '7': 'Vacant', '8': 'Vacant'}})),
                ('date', models.DateField()),
                ('time', models.TimeField(choices=[(datetime.time(9, 0), '9:00 AM'), (datetime.time(12, 0), '12:00 PM'), (datetime.time(
                    15, 0), '3:00 PM'), (datetime.time(18, 0), '6:00 PM'), (datetime.time(21, 0), '9:00 PM')])),
                ('rate', models.IntegerField()),
                ('hall', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='movies.hall')),
                ('movie', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'unique_together': {('hall', 'date', 'time')},
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.JSONField()),
                ('cost', models.IntegerField()),
                ('show', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='movies.show')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='movies.city')),
            ],
        ),
        migrations.AddField(
            model_name='hall',
            name='theatre',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='movies.theatre'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                         related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set',
                                         related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
