

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20200506_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
