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
	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditDefaultsOnly, Category="Character")
	FText Name;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditDefaultsOnly, Category="Character|Body")
	double MaxHealth = 100;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditDefaultsOnly, Category="Character|Body")
	double MaxMana = 200;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditDefaultsOnly, Category="Character|Body")
	double Height = 170;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditDefaultsOnly, Category="Character|Speed")
	double RunSpeed = 400;

	/** Please add a variable description */
	UPROPERTY(BlueprintReadWrite, EditDefaultsOnly, Category="Character|Speed")
	double WalkSpeed = 200;
};
