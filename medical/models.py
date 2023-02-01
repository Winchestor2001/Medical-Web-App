from django.db import models
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    slug = models.SlugField(help_text="Buerga xechnarsa yozmang")
    name = models.CharField(max_length=255, verbose_name="MFY nomi")
    population = models.BigIntegerField(verbose_name='Aholi soni')

    def __str__(self):
        return "{} - {}".format(self.name, self.population)
    
    class Meta:
        verbose_name = 'Mahalla'
        verbose_name_plural = 'Mahallalar'
        


class Street(models.Model):
    slug = models.SlugField(help_text="Buerga xechnarsa yozmang")
    name = models.CharField(max_length=255, verbose_name='Ko\'cha nomi')
    population = models.BigIntegerField(verbose_name='Aholi soni')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, verbose_name='MFY')

    def __str__(self):
        return "{} - {}".format(self.name, self.population)
    
    class Meta:
        verbose_name = 'Ko\'cha'
        verbose_name_plural = 'Ko\'chalar'


class Staff(models.Model):
    CHOISES = (
        ("Врач", "Врач"),
        ("Оилавий хамшира", "Оилавий хамшира"),
        ("Умумий амалий хамшира", "Умумий амалий хамшира"),
        ("Доя", "Доя"),
        ("Болалар хамшира", "Болалар хамшира"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Ishchi username')
    full_name = models.CharField(max_length=255, verbose_name='Ism sharifi')
    rank = models.CharField(max_length=255, choices=CHOISES, verbose_name='Lavozimi')

    def __str__(self):
        return "{} - {}".format(self.full_name, self.rank)
    
    class Meta:
        verbose_name = 'Ishchi'
        verbose_name_plural = 'Ishchilar ro\'yxati'


class Address(models.Model):
    addres_name = models.CharField(max_length=200, verbose_name='Manzil')
    full_name = models.CharField(max_length=200, verbose_name='Ism sharifi')
    phone_number = models.CharField(max_length=200, verbose_name='Telefon raqami +998')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name='Ko\'cha')
    

    def __str__(self):
        return "{} - {}".format(self.full_name, self.phone_number)
    
    class Meta:
        verbose_name = 'Manzil'
        verbose_name_plural = 'Manzillar'


class Work(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Ishchi')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Manzil')
    checked = models.BooleanField(default=False, verbose_name='Tekshirildi?')
    img = models.ImageField(upload_to='work_imgs/', verbose_name='Rasim', blank=True, null=True)
    date = models.DateField(verbose_name='Sana')

    def __str__(self):
        return "{}".format(self.staff)
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Kunlik ish reja'
        verbose_name_plural = 'Kunlik ish rejalar'


class SmsCode(models.Model):
    number = models.CharField(max_length=50, unique=True, verbose_name='Telefon raqam')
    code = models.IntegerField(blank=True, null=True, unique=True, verbose_name='Tastiqlash ko\'di')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.number)
    
    class Meta:
        verbose_name = 'Sms ko\'d'
        verbose_name_plural = 'Sms ko\'dlar'