from portal.models import FAQ


def get_faqs():
    return [(x, x) for x in list(FAQ.objects.all().values_list('question', flat=True))]
