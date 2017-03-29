__author__ = 'José Luis Valencia Herrera'

from xml.etree import ElementTree as ET

import os
import plivo

auth_id = os.environ.get("PLIVO_AUTH_ID", "")
auth_token = os.environ.get("PLIVO_AUTH_TOKEN", "")

p = plivo.RestAPI(auth_id, auth_token)


def send_call(phone, real_name: str, order: str, payment_method: str):
    params = {
        'to': phone,  # The phone numer to which the call will be placed
        'from': '11111111111',  # The phone number to be used as the caller id

        # answer_url is the URL invoked by Plivo when the outbound call is answered
        # and contains instructions telling Plivo what to do with the call
        'answer_url': os.environ.get("PLIVO_ANSWER_URL", ""),
        'answer_method': "POST",  # The method used to call the answer_url
    }

    root = ET.Element('Response')

    intro = ET.Element('Speak')
    intro.set('language', 'es-US')
    intro.set('voice', 'MAN')
    intro.text = "¡Saludos, Punta del Cielo! Esta es una orden telefónica automatizada. " \
				 "A continuación diré la orden dos veces."

    wait = ET.Element('Wait')
    wait.set('length', '1')

    order_element = ET.Element('Speak')
    order_element.set('language', 'es-US')
    order_element.set('voice', 'MAN')
    order_element.set('loop', '2')
    order_element.text = "{0}, desea ordenar lo siguiente. {1}.".format(real_name, order)

    payment = ET.Element('Speak')
    payment.set('language', 'es-US')
    payment.set('voice', 'MAN')

    if "tarjeta" in payment_method.lower():
        if "visa" in payment_method.lower():
            payment.text = "El pago se hará con tarjeta VISA."
        elif "mastercard" in payment_method.lower():
            payment.text = "El pago se hará con tarjeta MasterCard."
        elif "amex" in payment_method.lower() or "american express" in payment_method.lower():
            payment.text = "El pago se hara con tarjeta American Express."
        else:
            payment.text = "El pago se hará con tarjeta."
    else:
        payment.text = "El pago se realizará con un billete de {0} pesos.".format(payment_method)

    ending = ET.Element('Speak')
    ending.set('language', 'es-US')
    ending.set('voice', 'MAN')
    ending.text = "Muchas gracias y buen día. ¡Hasta luego!"

    root.append(intro)
    root.append(wait)
    root.append(order_element)
    root.append(payment)
    root.append(ending)

    with open('/var/www/order.xml', 'wb') as file:
        ET.ElementTree(root).write(file, xml_declaration=True)

    response = p.make_call(params)

    return response[0] == 201
