# Generated by Django 2.1 on 2018-08-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_merge_20180817_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescuecamp',
            name='clothing_req',
            field=models.TextField(blank=True, null=True, verbose_name='Clothing - വസ്ത്രം'),
        ),
        migrations.AddField(
            model_name='rescuecamp',
            name='food_req',
            field=models.TextField(blank=True, null=True, verbose_name='Food - ഭക്ഷണം'),
        ),
        migrations.AddField(
            model_name='rescuecamp',
            name='medical_req',
            field=models.TextField(blank=True, null=True, verbose_name='Medical - മെഡിക്കൽ'),
        ),
        migrations.AddField(
            model_name='rescuecamp',
            name='other_req',
            field=models.TextField(blank=True, null=True, verbose_name='Other - മറ്റുള്ളവ'),
        ),
        migrations.AddField(
            model_name='rescuecamp',
            name='sanitary_req',
            field=models.TextField(blank=True, null=True, verbose_name='Sanitary - സാനിറ്ററി'),
        ),
        migrations.AlterField(
            model_name='person',
            name='district',
            field=models.CharField(blank=True, choices=[('alp', 'Alappuzha - ആലപ്പുഴ'), ('ekm', 'Ernakulam - എറണാകുളം'), ('idk', 'Idukki - ഇടുക്കി'), ('knr', 'Kannur - കണ്ണൂർ'), ('ksr', 'Kasaragod - കാസർഗോഡ്'), ('kol', 'Kollam - കൊല്ലം'), ('ktm', 'Kottayam - കോട്ടയം'), ('koz', 'Kozhikode - കോഴിക്കോട്'), ('mpm', 'Malappuram - മലപ്പുറം'), ('pkd', 'Palakkad - പാലക്കാട്'), ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'), ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'), ('tcr', 'Thrissur - തൃശ്ശൂർ'), ('wnd', 'Wayanad - വയനാട്')], max_length=15, null=True, verbose_name='Residence District - താമസിക്കുന്ന ജില്ല'),
        ),
        migrations.AlterField(
            model_name='rescuecamp',
            name='contacts',
            field=models.TextField(blank=True, null=True, verbose_name='Phone Numbers - ഫോൺ നമ്പറുകൾ'),
        ),
        migrations.AlterField(
            model_name='rescuecamp',
            name='location',
            field=models.TextField(blank=True, null=True, verbose_name='Address - അഡ്രസ്'),
        ),
        migrations.AlterField(
            model_name='rescuecamp',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Camp Name - ക്യാമ്പിന്റെ പേര്'),
        ),
        migrations.AlterField(
            model_name='rescuecamp',
            name='taluk',
            field=models.CharField(max_length=50, verbose_name='Taluk - താലൂക്ക്'),
        ),
        migrations.AlterField(
            model_name='rescuecamp',
            name='village',
            field=models.CharField(max_length=50, verbose_name='Village - വില്ലജ്'),
        ),
    ]