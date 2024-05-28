# Generated by Django 5.0.4 on 2024-05-19 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0010_alter_document_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('struct', models.CharField(default=None, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='meta_doc_id',
            field=models.IntegerField(default=0),
        ),
    ]