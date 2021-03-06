# Generated by Django 3.1 on 2021-01-19 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rider', '0001_initial'),
        ('store', '0001_initial'),
        ('userForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('basecoremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='associates.basecoremodel')),
            ],
            bases=('associates.basecoremodel',),
        ),
        migrations.CreateModel(
            name='StoreSeller',
            fields=[
                ('basecoremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='associates.basecoremodel')),
            ],
            bases=('associates.basecoremodel',),
        ),
        migrations.CreateModel(
            name='UserProduct',
            fields=[
                ('basecoremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='associates.basecoremodel')),
            ],
            bases=('associates.basecoremodel',),
        ),
        migrations.CreateModel(
            name='UserStore',
            fields=[
                ('basecoremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='associates.basecoremodel')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rider.rider')),
            ],
            bases=('associates.basecoremodel',),
        ),
        migrations.CreateModel(
            name='UserRider',
            fields=[
                ('basecoremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='associates.basecoremodel')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rider.rider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userForm.users')),
            ],
            bases=('associates.basecoremodel',),
        ),
    ]
