import unreal
import csv

# User config variables
csv_file_path = "/UEProjects/MagicBox/Content/MB/NPCs/Monsters.csv"
asset_folder = "/Game/MB/NPCs"
prefix = "DA_"

# Helper libraries
EAL = unreal.EditorAssetLibrary
DAF = unreal.DataAssetFactory() # Create instance of the factory
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()


# Load an asset or create it if it doesn't exist. -> Object
def load_or_create_asset(asset_path: str, asset_name: str) -> unreal.Object:

    if(EAL.does_asset_exist(asset_path)):
        print (f"{asset_path} already exists.")
        this_asset = EAL.load_asset(asset_path)
    else:
        print(f"Creating asset for {asset_path}")
        this_asset = asset_tools.create_asset(
            asset_name,
            asset_folder,
            unreal.PDA_NPC.static_class(),
            DAF
            )
    return this_asset


# Load a CSV, create or load a UAsset, and match the CSV to the asset
def import_monsters(csv_file_path: str):

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:

            # Extract data from the CSV
            name = row[0]
            archetype = unreal.NPCArchetype.cast(int(row[1]))
            health = row[2]

            asset_path = asset_folder + "/" + prefix + name
            this_asset = load_or_create_asset(asset_path, prefix + name)
            if not this_asset: continue

            # Set properties on the asset
            this_asset.set_editor_property("Name", name)
            this_asset.set_editor_property("Archetype", archetype)
            this_asset.set_editor_property("MaxHealth", int(health))

            # Set metadata on the asset
            EAL.set_metadata_tag(this_asset, unreal.Name("NPC.Archetype"), str(archetype))
            EAL.set_metadata_tag(this_asset, unreal.Name("NPC.MaxHealth"), health)


        # Save dirty packages
        unreal.EditorAssetLibrary.save_directory(asset_folder)


# Load the CSV file
try:
    import_monsters(csv_file_path)

except Exception as e:
    unreal.log_warning("Failed to load and process the CSV file: {}".format(e))
