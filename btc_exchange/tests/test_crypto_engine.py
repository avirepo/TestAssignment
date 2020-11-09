# Create your tests here.
from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIClient

from btc_exchange.btc_engine.common import (BaseCrptoEngine, get_register_crpto_engine)

client = APIClient()


class CryptoEngineTestCases(TestCase):
    def test_valid_create_crypto_engine(self):
        engine = get_register_crpto_engine()
        self.assertIsNotNone(engine, 'Function should return a valid engine')

    def test_valid_create_crypto_engine_instance_type(self):
        engine = get_register_crpto_engine()
        self.assertTrue(isinstance(engine, BaseCrptoEngine))

    def test_no_create_crypto_engine_define(self):
        crypto_engine = settings.CRPTO_ENGINE
        settings.CRPTO_ENGINE = 'CRPTO_ENGINE'
        with self.assertRaises(ValueError):
            get_register_crpto_engine()
            print('Function should raise the exception but provided engine reference')
        settings.CRPTO_ENGINE = crypto_engine

    def test_invalid_crypto_engine_define(self):
        crypto_engine = settings.CRPTO_ENGINE
        settings.CRPTO_ENGINE = 'btc_exchange.tests.mock_data.DummyCrptoEngine'
        with self.assertRaises(ValueError):
            get_register_crpto_engine()
            print(
                'Function should raise the exception as crypto engine is not derived from '
                'BaseCrptoEngine'
            )
        settings.CRPTO_ENGINE = crypto_engine
