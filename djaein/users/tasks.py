from celery import shared_task


@shared_task
def mark_old_to_do_as_done():
    return True
