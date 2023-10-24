def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

    
    

def assign_rooms(names):
    room = 1
    assignments = []
    for name in names:
        assignment = f"Hello, {name}! You'll be assigned to room {room}!"
        assignments.append(assignment)
        room += 1
    return assignments


def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)
    messages = badges + assignments  # Combine badge messages and room assignment messages
    for message in messages:
        print(message)
    return messages

