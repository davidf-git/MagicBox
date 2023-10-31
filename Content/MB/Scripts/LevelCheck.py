import unreal

#
#  Level design script finds all actors at the same location as each other
#  and prints them to the output log, one line per set of duplicates
#

# Print the actors in a list that are at duplicate locations
def get_duplicate_actors(actors: list):
    location_dict = {}
    for actor in actors:
        # Don't check child actors, as they often have the same location, which can be fine
        if actor.get_attach_parent_actor() is not None: continue
        actor_location = (   # Round the vector and convert to hashable tuple
            int(actor.get_actor_location().x),
            int(actor.get_actor_location().y),
            int(actor.get_actor_location().z)
            )
        if actor_location in location_dict:
            location_dict[actor_location].append(actor)
        else:
            location_dict[actor_location] = [actor]

    dupes = []
    for this_location in location_dict:
        if len(location_dict[this_location]) > 1:
            dupes.append(location_dict[this_location])
    return dupes

# Return the folder and display name of an actor
def get_actor_folder_path(actor: unreal.Actor):
    path = ""
    if not actor.get_folder_path().is_none(): path = str(actor.get_folder_path())
    return f"[{path}/{actor.get_actor_label()}]"

# Get pretty actor location, ready for output to the log
def get_formatted_actor_location(actor: unreal.Actor):
    l = actor.get_actor_location()
    return f"TeleportTo {int(l.x)} {int(l.y)} {int(l.z)}".ljust(40)

# Get pretty actor label from list of actors, ready for output to the log
def get_formatted_actor_list(actors: list):
    list = []
    for this_actor in actors:
        list.append(get_actor_folder_path(this_actor))
    return ":".join(list)


# Output all the dupe actors to the output log
def print_actor_list_info (duplicate_entries: list):
    print("Checking level for actors at the same location")
    if len(duplicate_entries) == 0:
        print("No duplicates found. 🎉")
        return
    
    for this_list in duplicate_entries:
        tp = get_formatted_actor_location(this_list[0])
        actor_str = get_formatted_actor_list(this_list)
        unreal.log_warning(f"{tp} {actor_str}")
    print("--- List End 🎉---")


def main():
    EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    all_actors = EAS.get_all_level_actors()
    dupes = get_duplicate_actors(all_actors)
    print_actor_list_info(dupes)

if __name__ == '__main__':
    main()
