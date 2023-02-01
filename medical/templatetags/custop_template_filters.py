from django import template
from ..models import Work

register = template.Library()

@register.filter
def prosent(n):
    works = Work.objects.filter(staff=n)
    success_work = 0
    for w in works:
        if w.checked:
            success_work += 1
    return 100 * success_work // len(works)


