# A list of all the effects which exist within the application.
effects = []

# Represents an imperative effect within a block of declarative code.
# Intended for use internally by useEffect. Should not be used anywhere else.
class EffectEntry:
    def __init__(self, id):
        self.id = id

# Utilitiy for running effectual code in a declarative environment. Similar to React.js's useEffect hook.
# The given effect callback is run when any of the given dependencies changes.
# The caller should take care to assign a unique id which is stable across different ticks.
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
