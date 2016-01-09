from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Lisandro Guerra', cpf='12345678901',
                    email='lisandro@mailinator.com', phone='51-9116-8121')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'lisandro.digital@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['lisandro.digital@gmail.com', 'lisandro@mailinator.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Lisandro Guerra',
            '12345678901',
            'lisandro@mailinator.com',
            '51-9116-8121',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)