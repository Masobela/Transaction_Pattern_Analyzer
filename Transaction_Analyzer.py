transactions = [
    {"sender": "Neo", "receiver": "Trinity", "amount": 100, "type": "debit"},
    {"sender": "Trinity", "receiver": "Morpheus", "amount": 200, "type": "credit"},
    {"sender": "Morpheus", "receiver": "Cypher", "amount": 150, "type": "debit"},
    {"sender": "Cypher", "receiver": "Agent Smith", "amount": 300, "type": "credit"},
    {"sender": "Agent Smith", "receiver": "Architect", "amount": 250, "type": "debit"},
    {"sender": "Architect", "receiver": "Oracle", "amount": 400, "type": "credit"},
    {"sender": "Oracle", "receiver": "Switch", "amount": 350, "type": "debit"},
    {"sender": "Switch", "receiver": "Tank", "amount": 500, "type": "credit"},
    {"sender": "Tank", "receiver": "Dozer", "amount": 450, "type": "debit"},
    {"sender": "Dozer", "receiver": "Neo", "amount": 600, "type": "credit"},
]
transaction_count = {
    "Neo": {"debit": 1, "credit": 1},
    "Trinity": {"debit": 1, "credit": 1},
    "Morpheus": {"debit": 1, "credit": 1},
    "Cypher": {"debit": 1, "credit": 1},
    "Agent Smith": {"debit": 1, "credit": 1},
    "Architect": {"debit": 1, "credit": 1},
    "Oracle": {"debit": 1, "credit": 1},
    "Switch": {"debit": 1, "credit": 1},
    "Tank": {"debit": 1, "credit": 1},
    "Dozer": {"debit": 1, "credit": 1}
}
for t in transactions:
    sender = t["sender"]
    receiver = t["receiver"]
    amount = t["amount"]
    transaction_type = t["type"]
    if sender in transaction_count:
        transaction_count[sender][transaction_type] += 1
        print(f" {sender} made a {transaction_type} of ${amount} to {receiver}.")
    else:
        transaction_count[sender]["sender"] = {"debit": 0, "credit": 0}
        transaction_count[sender][transaction_type] += 1
        print(f" {sender} made a {transaction_type} of ${amount} to {receiver}.")


    if receiver in transaction_count:
        transaction_count[receiver][transaction_type] += 1
        print(f" {receiver} received a {transaction_type} of ${amount} from {sender}.")
    else:
        transaction_count[receiver] = {"debit": 0, "credit": 0}
        transaction_count[receiver][transaction_type] += 1
        print(f" {receiver} received a {transaction_type} of ${amount} from {sender}.")

for user, counts in transaction_count.items():
    if counts['debit'] + counts['credit'] > 3:
        print(f" ⚠️ Suspicious activity detected for {user}: {counts['debit']} debits and {counts['credit']} credits.")
    else:
        print(f" {user} has normal transaction activity: {counts['debit']} debits and {counts['credit']} credits.")