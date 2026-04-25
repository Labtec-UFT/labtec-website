from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import Project3DFile, ProjectImage


@receiver(post_delete, sender=ProjectImage)
def delete_project_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=ProjectImage)
def delete_old_project_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = ProjectImage.objects.get(pk=instance.pk)
    except ProjectImage.DoesNotExist:
        return

    if old_instance.image and old_instance.image != instance.image:
        old_instance.image.delete(save=False)


@receiver(post_delete, sender=Project3DFile)
def delete_project_3d_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(save=False)


@receiver(pre_save, sender=Project3DFile)
def delete_old_project_3d_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Project3DFile.objects.get(pk=instance.pk)
    except Project3DFile.DoesNotExist:
        return

    if old_instance.file and old_instance.file != instance.file:
        old_instance.file.delete(save=False)

