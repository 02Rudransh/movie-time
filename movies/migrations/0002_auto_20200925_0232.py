from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='seats',
            field=models.JSONField(default={'A': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant', 4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}, 'B': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant', 4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}, 'C': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant', 4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}, 'D': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant',
                                   4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}, 'E': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant', 4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}, 'F': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant', 4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}, 'G': {1: 'Vacant', 2: 'Vacant', 3: 'Vacant', 4: 'Vacant', 5: 'Vacant', 6: 'Vacant', 7: 'Vacant', 8: 'Vacant'}}),
        ),
    ]
