import logging
import time

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class TimingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # TODO: delete this!!!
        # time.sleep(1)
        request.start_time = time.time()

    def process_response(self, request, response):
        delta_time = time.time() - request.start_time

        logger.info("time took to send the response was {} seconds.".format(
            delta_time
        ))

        return response
