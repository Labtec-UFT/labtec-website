from django.db.models.signals import post_delete
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import NewsImage


@receiver(post_delete, sender=NewsImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=NewsImage)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # objeto novo, nada pra comparar

    try:
        old_instance = NewsImage.objects.get(pk=instance.pk)
    except NewsImage.DoesNotExist:
        return

    old_file = old_instance.image
    new_file = instance.image

    if old_file and old_file != new_file:
        old_file.delete(save=False)