import comtypes.client

def connect_to_etabs():
    """Conectar a la api de etabs"""
    helper = comtypes.client.CreateObject('ETABSv1.Helper')
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    ETABSObject = helper.GetObject("CSI.ETABS.API.ETABSObject")
    SapModel = ETABSObject.SapModel
    return SapModel
