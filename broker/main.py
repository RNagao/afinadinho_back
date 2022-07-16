from beebotte import *

bclient = BBT("Jwk23dE5HcJPSjPaWwbnlOwf", "ZqQmaMxMupIScTWt1jgAiij4AegCh0XF")

teste_res = Resource(bclient, 'Afinadinho', 'teste')
freq_res = Resource(bclient, 'Afinadinho', 'frequencia')

def publish_teste_resource(mensagem):
    return bclient.writeBulk('Afinadinho', [
        {"resource": "teste", "data": mensagem}
    ])

def publish_freq_resource(mensagem):
    return bclient.writeBulk('Afinadinho', [
        {"resource": "frequencia", "data": mensagem}
    ])

def read_teste_resource():
    return teste_res.read(limit=1)

def read_freq_resource():
    return freq_res.read(limit=1)

def write_broker(resource, mens):
    res = Resource(bclient, 'Afinadinho', str(resource))
    return bclient.writeBulk('Afinadinho', [
        {"resource": str(resource), "data": mens}
    ])


# publish_teste_resource("Vamooooo")
# publish_freq_resource(443)

# print(read_teste_resource())
# print(read_freq_resource())