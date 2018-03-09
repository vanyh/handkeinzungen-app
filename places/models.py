from django.db import models
from django.core.urlresolvers import reverse
from idprovider.models import IdProvider
from django.utils.translation import ugettext_lazy


class AlternativeName(IdProvider):
    name = models.CharField(max_length=250, blank=True, help_text=ugettext_lazy('Alternative Ortsbezeichnung'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('places:alternativename_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_altnames')

    def get_next(self):
        next = AlternativeName.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = AlternativeName.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('places:alternativename_detail', kwargs={'pk': self.id})

    def __str__(self):
        return "{}".format(self.name)

    def get_classname(self):
        """Returns the name of the class. Needed to fetch the class name in templates"""
        class_name = "{}".format(self.__class__.__name__)
        return class_name

    @classmethod
    def get_alternative_classname(self):
        """Returns the alternative name of the class.
        Needed to present the human readable name of class"""
        return ugettext_lazy('Alternative Ortsbezeichnungen')

    @classmethod
    def get_createview_url(self):
        return reverse('places:alternativename_create')


class Place(IdProvider):
    PLACE_TYPES = (
        ("city", "city"),
        ("country", "country")
    )

    """Holds information about places."""
    name = models.CharField(
        max_length=250, blank=True, help_text=ugettext_lazy('Standardname')
    )
    alternative_name = models.ManyToManyField(
        AlternativeName,
        max_length=250, blank=True,
        help_text=ugettext_lazy('Alternative Ortsbezeichnung'),
        related_name="related_places", verbose_name=ugettext_lazy('Alternative Ortsbezeichnung')
    )
    geonames_id = models.CharField(
        max_length=50, blank=True,
        help_text="GND-ID"
    )
    lat = models.DecimalField(
        max_digits=20, decimal_places=12,
        blank=True, null=True
    )
    lng = models.DecimalField(
        max_digits=20, decimal_places=12, blank=True, null=True
    )
    part_of = models.ForeignKey(
        "Place", null=True, blank=True, help_text=ugettext_lazy('Ein Ort, von dem dieser Ort ein Teil ist.'),
        verbose_name=ugettext_lazy('Teil von')
    )
    place_type = models.CharField(choices=PLACE_TYPES, null=True, blank=True, max_length=50, verbose_name=ugettext_lazy('Art des Ortes')
    )

    @classmethod
    def get_listview_url(self):
        return reverse('places:place_list')

    def get_absolute_url(self):
        return reverse('places:place_detail', kwargs={'pk': self.id})

    def get_classname(self):
        """Returns the name of the class. Needed to fetch the class name in templates"""
        class_name = "{}".format(self.__class__.__name__)
        return class_name

    def __str__(self):
        return "{}".format(self.name)

    def get_next(self):
        next = Place.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Place.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    @classmethod
    def get_alternative_classname(self):
        """Returns the alternative name of the class.
        Needed to present the human readable name of class"""
        return ugettext_lazy('Orte')

    @classmethod
    def get_createview_url(self):
        return reverse('places:create_place')
