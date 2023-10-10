import unreal

EAL = unreal.EditorAssetLibrary
EUL = unreal.EditorUtilityLibrary

#assets = EUL.get_selected_assets()
assetpaths = EAL.list_assets("/Game/MB")
nrProcessed = 0

for assetpath in assetpaths:
	asset = EAL.find_asset_data(assetpath)
	if isinstance(asset, unreal.PDA_NPC):
		nrProcessed += 1
		print(asset.get_name())
		
		EAL.set_metadata_tag(asset, unreal.Name("NPC.Archetype"), str(asset.archetype))
		EAL.set_metadata_tag(asset, unreal.Name("NPC.Height"), str(asset.height))
		EAL.save_asset(asset.get_path_name())

print(f"Done working with {nrProcessed} assets.")
        