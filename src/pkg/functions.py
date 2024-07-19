

def make_payment():
    return {
        "followupEventInput": {
            "name": "makeApayment",
            "parameters": {
                "parameter-name-1": "parameter-value-1",
                "parameter-name-2": "parameter-value-2"
        },
        "languageCode": "en-US"
    }
}

def make_deposit():
    return {
        "followupEventInput": {
            "name": "makeAdeposit",
            "parameters": {
                "parameter-name-1": "parameter-value-1",
                "parameter-name-2": "parameter-value-2"
        },
        "languageCode": "en-US"
    }
}

def make_transfer():
    return {
        "followupEventInput": {
            "name": "makeAtransfer",
            "parameters": {
                "parameter-name-1": "parameter-value-1",
                "parameter-name-2": "parameter-value-2"
        },
        "languageCode": "en-US"
    }
}
    
def handle_unrecognized_event():
    return {
        "followupEventInput": {
            "name": "unrecognizedEvent",
            "parameters": {
                "parameter-name-1": "parameter-value-1",
                "parameter-name-2": "parameter-value-2"
        },
        "languageCode": "en-US"
    }
}
    
    
def dialogflowFunctions(intent_name: str):
    if intent_name == "Make a Payment":
        return make_payment()
    elif intent_name == "Make a Deposit":
        return make_deposit()
    elif intent_name == "Make a Transfer":
        return make_transfer()
    else:
        return handle_unrecognized_event()