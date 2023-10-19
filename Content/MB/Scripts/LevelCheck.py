import unreal

EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
all_actors = EAS.get_all_level_actors()

def get_folder_path(actor):
    path = "/"
    if str(actor.get_folder_path()) != "None":
        path = str(actor.get_folder_path()) + "/"
    return path + unreal.SystemLibrary.get_display_name(actor)

def get_duplicate_actors(actors: unreal.Actor):
    seen = set()
    dupes = []

    for actor in actors:
        actor_location = (   # Convert the vector to a hashable tuple
            round(actor.get_actor_location().x, 1),
            round(actor.get_actor_location().y, 1),
            round(actor.get_actor_location().z, 1),
            )
        
        if actor_location in seen:
            dupes.append(actor)
        else:
            seen.add(actor_location)

    return dupes

def print_actor_info(actors: unreal.Actor):
    for actor in actors:
        print(get_folder_path(actor))


dupes = get_duplicate_actors(all_actors)
if len(dupes) > 0:
    unreal.log_warning("Actors at same location as other actors:")
    print_actor_info(dupes)
else:
    print("No duplicates found.")