#POST_Node-Red

URL = "https://note.convergedigital.com.br/post"
USUARIO ="carlos"
SENHA = "261297"

import requests
import time
import logging
import random
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.slu.entityresolution.resolution import Resolution
from ask_sdk_model.slu.entityresolution import StatusCode
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)
        
    def handle(self, handler_input):
        speak_output = random.choice([
            "Deseja algo?",
            "Pois não?",
            "Posso ajudar?",
            "Como posso ajudar?",
            "O que precisa?",
            "Estou ouvindo.",
            "Posso auxiliar?",
            "Estou à disposição.",
            "Como posso ser útil?",
            "O que deseja?",
            "Estou aqui."
        ])
        
        return (handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class IntencaoDeContinuidadeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("intencao_de_continuidade")(handler_input)
        
    def handle(self, handler_input):
        slot = ask_utils.get_slot(handler_input=handler_input, slot_name="comandos_de_continuidade")
        
        if slot and slot.resolutions and slot.resolutions.resolutions_per_authority:
            for resolution in slot.resolutions.resolutions_per_authority:
                if resolution.status.code == StatusCode.ER_SUCCESS_MATCH:
                    
                    requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': resolution.values[0].value.name, 'dispositivo': handler_input.request_envelope.context.system.device.device_id}) 
                    
                    speak_output = random.choice([
                        "Algo mais?",
                        "Deseja algo mais?",
                        "Mais alguma coisa?",
                        "Deseja mais alguma coisa?",
                        "Algum outro desejo?",
                        "Alguma outra solicitação?",
                        "Algo adicional?",
                        "Tem mais algum pedido?"
                    ])
                else:
                    raise
                
        return (handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class IntencaoDiretaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("intencao_direta")(handler_input)
        
    def handle(self, handler_input):
        slot = ask_utils.get_slot(handler_input=handler_input, slot_name="comandos_diretos")
        
        if slot and slot.resolutions and slot.resolutions.resolutions_per_authority:
            for resolution in slot.resolutions.resolutions_per_authority:
                if resolution.status.code == StatusCode.ER_SUCCESS_MATCH:
                    
                    requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': resolution.values[0].value.name, 'dispositivo': handler_input.request_envelope.context.system.device.device_id}) 
                    
                else:
                    raise
                
        return (handler_input.response_builder
                .speak("Certo.")
                .response
        )

class IntencaoDeEsperaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("intencao_de_espera")(handler_input)
        
    def handle(self, handler_input):
        slot = ask_utils.get_slot(handler_input=handler_input, slot_name="comandos_de_espera")
        
        if slot and slot.resolutions and slot.resolutions.resolutions_per_authority:
            for resolution in slot.resolutions.resolutions_per_authority:
                if resolution.status.code == StatusCode.ER_SUCCESS_MATCH:
                    
                    requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Solicitação de Espera", 'dispositivo': handler_input.request_envelope.context.system.device.device_id}) 
                    
                else:
                    raise
                
        time.sleep(7)
        
        speak_output = random.choice([
            "Podemos continuar?",
            "Podemos seguir?",
            "Continuando.",
            "Podemos dar continuidade?",
            "Pronto."
        ])
        
        return (handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class IntencaoDeFinalizacaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("intencao_de_finalizacao")(handler_input)

    def handle(self, handler_input):
        slot = ask_utils.get_slot(handler_input=handler_input, slot_name="comandos_de_finalizacao")
        
        if slot and slot.resolutions and slot.resolutions.resolutions_per_authority:
            for resolution in slot.resolutions.resolutions_per_authority:
                if resolution.status.code == StatusCode.ER_SUCCESS_MATCH:
                    
                    requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Solicitação de finalização", 'dispositivo': handler_input.request_envelope.context.system.device.device_id}) 
                    
                else:
                    raise
                
        return (handler_input.response_builder
                .speak("Valeu.")
                .response
        )
    
class CancelIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input)
        
    def handle(self, handler_input):
        
        requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Solicitação de cancelamento", 'dispositivo': handler_input.request_envelope.context.system.device.device_id})
        
        return (handler_input.response_builder
                .speak("Valeu.")
                .response
        )
    
class StopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input)
        
    def handle(self, handler_input):
        
        requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Solicitação de parada", 'dispositivo': handler_input.request_envelope.context.system.device.device_id})
        
        return (handler_input.response_builder
                .speak("Valeu.")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)
        
    def handle(self, handler_input):
        
        requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Solicitação de ajuda", 'dispositivo': handler_input.request_envelope.context.system.device.device_id})
        
        return (handler_input.response_builder
                .speak("Não posso fornecer ajuda. Tente outra vez.")
                .ask("Não tenho instruções para suporte. Tente outra vez.")
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In FallbackIntentHandler")
        
        requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Não compreendido", 'dispositivo': handler_input.request_envelope.context.system.device.device_id})
        
        return (handler_input.response_builder
                .speak("Não entendi corretamente. Pode repetir?")
                .ask("Realmente não entendi. Tente outra vez.")
                .response
        )

class EndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        
        requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Não houve resposta", 'dispositivo': handler_input.request_envelope.context.system.device.device_id})
        
        return (handler_input.response_builder
                .response
        )
    
class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True
            
    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        
        requests.post(URL, auth=(USUARIO, SENHA), json = {'comando': "Resposta não cadastrada", 'dispositivo': handler_input.request_envelope.context.system.device.device_id})
        
        return (handler_input.response_builder
                .speak("Resposta sem cadastro.")
                .ask("Resposta não cadastrada.")
                .response
        )

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(IntencaoDeContinuidadeIntentHandler())
sb.add_request_handler(IntencaoDiretaIntentHandler())
sb.add_request_handler(IntencaoDeEsperaIntentHandler())
sb.add_request_handler(IntencaoDeFinalizacaoIntentHandler())
sb.add_request_handler(CancelIntentHandler())
sb.add_request_handler(StopIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(EndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())
lambda_handler = sb.lambda_handler()