
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


"""A simple python wrapper for Google's `Firebase`_ REST API Auth.

.. _Firebase: https://firebase.google.com/
"""

from .auth import Auth
from ._custom_requests import _custom_request
from ._service_account_credentials import _service_account_creds_from_secret


def initialize_app(config):
	"""Initializes and returns a new Firebase instance.

	:type config: dict
	:param config: Firebase configuration

	:return: A newly initialized instance of Firebase.
	:rtype: Firebase
	"""

	return Firebase(config)


class Firebase:
	""" Firebase Interface

	:type config: dict
	:param config: Firebase configuration
	"""

	def __init__(self, config):
		""" Constructor """

		self.api_key = config["apiKey"]
		self.auth_domain = config["authDomain"]
		self.database_url = config["databaseURL"]
		self.project_id = config["projectId"]
		self.storage_bucket = config["storageBucket"]

		self.credentials = None
		self.requests = _custom_request()

		if config.get("serviceAccount"):
			self.credentials = _service_account_creds_from_secret(config['serviceAccount'])

	def auth(self, client_secret=None):
		"""Initializes and returns a new Firebase Authentication
		instance.

		:type client_secret: str or dict
		:param client_secret: (Optional) File path to or the dict
			object from social client secret file, defaults to
			:data:`None`.


		:return: A newly initialized instance of Auth.
		:rtype: Auth
		"""

		return Auth(self.api_key, self.credentials, self.requests, client_secret=client_secret)
