from django.core.mail import send_mail
from multiprocessing import Process, Manager

from newsapplication.settings import EMAIL_HOST


def sending(queue):                                                                                                                                 # pragma: no cover
    while True:
        if not queue.empty():
            subject, message, address = queue.get()
            send_mail(subject, message, EMAIL_HOST, [address], False)


queue_ = Manager().Queue()


def send_email(subject, message, address, st=False):                                                                                            # pragma: no cover
    # send_email.queue = Manager().Queue()

    queue_.put((subject, message, address))
    if st is True:
        p = Process(target=sending, args=(queue_,))
        # p.daemon = True
        p.start()


