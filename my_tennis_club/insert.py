from members.models import Member

x = Member.objects.all()[0]
x.phone = 5551234
x.joined_date = '2022-01-05'
x.save()

Member.objects.all().values()