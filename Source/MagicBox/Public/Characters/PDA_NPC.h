// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Characters/PDA_Character.h"
#include "GameplayTagContainer.h"
#include "PDA_NPC.generated.h"

UENUM(BlueprintType)
enum class ENPCArchetype : uint8
{
	/** Main ranged combat class. */
	Assault,
	/** Heavy weapons class. */
	Heavy,
	/** Close quarters expert. */
	Rusher,	
	/** Technician or medic. */
	Suport,
};

/**
 * Data for an NPC Character
 */
UCLASS()
class MAGICBOX_API UPDA_NPC : public UPDA_Character
{
	GENERATED_BODY()
	
public:

	/** NPC Tags that define things about this NPC. */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category="NPC")
	FGameplayTagContainer NPCTags;

	/** Class of NPC */
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category="NPC")
	ENPCArchetype Archetype;
};
