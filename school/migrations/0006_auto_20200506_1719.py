

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200505_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='fee',
            field=models.PositiveIntegerField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='mobile',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
