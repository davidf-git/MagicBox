// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "PDA_Character.generated.h"

/**
 * 
 */
UCLASS()
class MAGICBOX_API UPDA_Character : public UPrimaryDataAsset
{
	GENERATED_BODY()
	
public:
	/** Player-facing name of this NPC */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, AssetRegistrySearchable, Category="Character")
	FText DisplayName;

	/** Max health */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, AssetRegistrySearchable, Category="Character|Body")
	double MaxHealth = 100;

	/** Max Mana */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category="Character|Body")
	double MaxMana = 200;

	/** Height (cm) */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category="Character|Body")
	double Height = 170;

	/** Run speed (cm/s) */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category="Character|Speed")
	double RunSpeed = 400;

	/** Walk speed (cm/s) */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category="Character|Speed")
	double WalkSpeed = 200;
};
