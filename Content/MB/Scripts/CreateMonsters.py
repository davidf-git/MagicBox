import unreal
import csv

# Set the path to your CSV file
csv_file_path = "/MagicBox/Content/MB/NPCs/Monsters.csv"
asset_path = "/Game/MB/NPCs"
prefix = "DA_"
EAL = unreal.EditorAssetLibrary
DAF = unreal.DataAssetFactory() # Create instance of the factory
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()


# Load the CSV file
try:
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row


        for row in csv_reader:
            # Extract data from the CSV
            name = row[0]
            archetypeStr = row[1]
            archetype = unreal.NPCArchetype.cast(int(archetypeStr))
            health = row[2]

            if(EAL.does_asset_exist(asset_path + "/" + prefix + name)):
                print (f"{name} already exists.")
                EAL.delete_asset(asset_path + prefix + name)

            print(f"Creating asset for {name}")
            new_asset = asset_tools.create_asset(f"DA_{name}",
                                        asset_path,
                                        unreal.PDA_NPC.static_class(),
                                        DAF
                                        )
            new_asset.set_editor_property("Name", name)
            new_asset.set_editor_property("Archetype", archetype)
            new_asset.set_editor_property("MaxHealth", int(health))
            EAL.set_metadata_tag(new_asset, unreal.Name("NPC.Archetype"), str(archetype))
            EAL.set_metadata_tag(new_asset, unreal.Name("NPC.MaxHealth"), health)

        # Save dirty packages
        unreal.EditorAssetLibrary.save_directory(asset_path)

except Exception as e:
    unreal.log_warning("Failed to load and process the CSV file: {}".format(e))
