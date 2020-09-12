from djchoices import DjangoChoices, ChoiceItem


class LocationTypeChoices(DjangoChoices):
    COUNTRY = ChoiceItem("COUNTRY")
    CITY = ChoiceItem("CITY")
    ZIP = ChoiceItem("ZIP")


class StatusTypeChoices(DjangoChoices):
    Created = ChoiceItem('Created')
    Contacted = ChoiceItem('Contacted')