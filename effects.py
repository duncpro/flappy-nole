
effects = []

class EffectEntry:
    def __init__(self, id):
        self.id = id

# Utilitiy for running effectual code in a declarative environment.
# Similar to React.js's useEffect.
# The given effect callback is run when any of the given dependencies changes.
# The caller should take care to assign a unique id to this effect.
# The id should remain stable accross different ticks
def useEffect(effect, id, dependencies):
    entry = None

    # Create a new effect entry if necessary
    for potential_entry in effects:
        if potential_entry.id == id:
            entry = potential_entry
            break
    if entry == None:
        entry = EffectEntry(id)
        entry.dependencies = None
        effects.append(entry)    

    # Run the effect hook if necessary
    if dependencies != entry.dependencies:
        entry.dependencies = dependencies
        effect()
