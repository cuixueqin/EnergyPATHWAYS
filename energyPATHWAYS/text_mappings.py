MappedCols = {
    "CO2PriceMeasures" : ['interpolation_method', 'geography', 'geography_map_key', 'extrapolation_method'],
    "DemandDriversData" : ['oth_2', 'parent', 'gau', 'oth_1'],
    "BlendNodeInputsData" : ['blend_node', 'supply_node'],
    "CurrenciesConversion" : ['currency'],
    "GeographiesData" : ['geography'],
    "FinalEnergy" : ['shape'],
    "DemandTechsFixedMaintenanceCostData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "OtherIndexesData" : ['other_index'],
    "DemandTechsFuelSwitchCostData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "DemandTechsFuelSwitchCost" : ['definition', 'extrapolation_method', 'other_index_1', 'currency', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "DemandTechsFixedMaintenanceCost" : ['definition', 'age_growth_or_decay_type', 'extrapolation_method', 'other_index_1', 'currency', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "DemandTechsInstallationCost" : ['definition', 'extrapolation_method', 'other_index_1', 'currency', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "DemandTechsMainEfficiency" : ['other_index_1', 'age_growth_or_decay_type', 'extrapolation_method', 'demand_tech_efficiency_types', 'definition', 'interpolation_method', 'geography', 'geography_map_key', 'other_index_2', 'demand_technology', 'final_energy'],
    "DemandEnergyDemandsData" : ['oth_2', 'gau', 'subsector', 'demand_technology', 'oth_1', 'final_energy'],
    "DemandTechsParasiticEnergyData" : ['oth_2', 'oth_1', 'final_energy', 'demand_technology', 'gau'],
    "DemandEnergyDemands" : ['other_index_1', 'driver_denominator_1', 'extrapolation_method', 'interpolation_method', 'driver_2', 'subsector', 'input_type', 'geography', 'geography_map_key', 'other_index_2', 'driver_1', 'driver_denominator_2'],
    "DemandEnergyEfficiencyMeasures" : ['other_index_1', 'stock_decay_function', 'extrapolation_method', 'input_type', 'subsector', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandTechsParasiticEnergy" : ['other_index_1', 'age_growth_or_decay_type', 'extrapolation_method', 'definition', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "DemandEnergyEfficiencyMeasuresData" : ['oth_2', 'parent', 'gau', 'final_energy', 'oth_1'],
    "DemandFuelSwitchingMeasures" : ['subsector', 'final_energy_to', 'final_energy_from', 'stock_decay_function'],
    "DemandSalesShareMeasures" : ['replaced_demand_tech', 'other_index_1', 'extrapolation_method', 'input_type', 'subsector', 'interpolation_method', 'geography', 'demand_technology'],
    "DemandSales" : ['other_index_1', 'extrapolation_method', 'input_type', 'subsector', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandServiceDemandMeasures" : ['other_index_1', 'stock_decay_function', 'extrapolation_method', 'input_type', 'subsector', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandSalesData" : ['oth_2', 'subsector', 'gau', 'demand_technology', 'oth_1'],
    "DemandFlexibleLoadMeasures" : ['subsector', 'interpolation_method', 'geography', 'extrapolation_method', 'other_index_1'],
    "DemandFuelSwitchingMeasuresImpact" : ['other_index_1', 'extrapolation_method', 'parent', 'input_type', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandFuelSwitchingMeasuresEnergyIntensity" : ['other_index_1', 'extrapolation_method', 'parent', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandFuelSwitchingMeasuresEnergyIntensityData" : ['oth_2', 'parent', 'gau', 'oth_1'],
    "DemandFuelSwitchingMeasuresImpactData" : ['oth_2', 'parent', 'gau', 'oth_1'],
    "DemandServiceDemandMeasuresCost" : ['other_index_1', 'extrapolation_method', 'parent', 'currency', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandSalesShareMeasuresData" : ['parent', 'gau', 'oth_1'],
    "DemandServiceDemandMeasuresCostData" : ['oth_2', 'parent', 'gau', 'oth_1'],
    "DemandServiceDemandMeasuresData" : ['oth_2', 'parent', 'gau', 'oth_1'],
    "DemandServiceLink" : ['subsector', 'linked_subsector'],
    "DemandStockMeasures" : ['other_index_1', 'extrapolation_method', 'subsector', 'interpolation_method', 'geography', 'demand_technology'],
    "DemandStock" : ['other_index_1', 'driver_denominator_1', 'extrapolation_method', 'interpolation_method', 'driver_2', 'demand_stock_unit_type', 'subsector', 'input_type', 'geography', 'geography_map_key', 'other_index_2', 'driver_1', 'driver_denominator_2'],
    "DemandServiceDemands" : ['other_index_1', 'driver_denominator_1', 'extrapolation_method', 'interpolation_method', 'driver_2', 'subsector', 'input_type', 'geography', 'geography_map_key', 'other_index_2', 'driver_1', 'driver_denominator_2'],
    "DemandServiceEfficiencyData" : ['oth_2', 'subsector', 'gau', 'final_energy', 'oth_1'],
    "DemandServiceEfficiency" : ['other_index_1', 'extrapolation_method', 'subsector', 'interpolation_method', 'geography', 'geography_map_key', 'other_index_2'],
    "DemandTechsCapitalCostReplacementData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "DemandTechsInstallationCostReplacementData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "DispatchTransmissionConstraint" : ['interpolation_method', 'extrapolation_method'],
    "DispatchFeedersAllocation" : ['input_type', 'interpolation_method', 'geography', 'geography_map_key', 'extrapolation_method'],
    "DemandTechsServiceLink" : ['other_index_1', 'age_growth_or_decay_type', 'service_link', 'extrapolation_method', 'definition', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "DemandTechsServiceDemandModifier" : ['other_index_1', 'age_growth_or_decay_type', 'extrapolation_method', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "DispatchFeedersAllocationData" : ['demand_sector', 'dispatch_feeder', 'gau'],
    "DispatchNodeConfig" : ['geography', 'dispatch_window', 'supply_node'],
    "DispatchTransmissionHurdleRate" : ['gau_to', 'parent', 'day_type', 'gau_from'],
    "DispatchTransmissionConstraintData" : ['gau_to', 'parent', 'day_type', 'gau_from'],
    "ImportCostData" : ['import_node', 'demand_sector', 'gau'],
    "ImportCost" : ['currency', 'import_node', 'geography', 'extrapolation_method', 'interpolation_method'],
    "OtherIndexesData_copy" : ['other_index'],
    "SupplyPotentialConversionData" : ['gau', 'supply_node', 'oth_1'],
    "ShapesData" : ['dispatch_constraint', 'dispatch_feeder', 'gau', 'parent', 'timeshift_type', 'day_type'],
    "SupplyEmissionsData" : ['supply_node', 'gau', 'ghg', 'oth_1', 'ghg_type', 'demand_sector'],
    "InflationConversion" : ['currency'],
    "SupplyTechs" : ['shape', 'stock_decay_function', 'supply_node'],
    "SupplyCost" : ['currency', 'interpolation_method', 'geography', 'extrapolation_method', 'supply_node'],
    "StorageTechsEnergyCapitalCost" : ['definition', 'supply_tech', 'extrapolation_method', 'reference_tech', 'currency', 'interpolation_method', 'geography'],
    "SupplyTechsFixedMaintenanceCostData" : ['demand_sector', 'gau', 'supply_tech'],
    "SupplyTechsCapitalCost" : ['definition', 'supply_tech', 'extrapolation_method', 'currency', 'interpolation_method', 'geography', 'geography_map_key'],
    "SupplyCostData" : ['parent', 'demand_sector', 'gau'],
    "SupplyTechsFixedMaintenanceCost" : ['definition', 'age_growth_or_decay_type', 'extrapolation_method', 'supply_tech', 'currency', 'interpolation_method', 'geography'],
    "StorageTechsEnergyCapitalCostNewData" : ['oth_2', 'supply_tech', 'gau', 'oth_1'],
    "StorageTechsEnergyCapitalCostReplacementData" : ['oth_2', 'supply_tech', 'gau', 'oth_1'],
    "SupplyTechsInstallationCost" : ['definition', 'supply_tech', 'extrapolation_method', 'currency', 'interpolation_method', 'geography'],
    "SupplyTechsCapitalCostNewData" : ['demand_sector', 'gau', 'supply_tech'],
    "SupplyTechsVariableMaintenanceCost" : ['definition', 'supply_tech', 'extrapolation_method', 'age_growth_or_decay_type', 'currency', 'interpolation_method', 'geography'],
    "SupplyTechsInstallationCostNewData" : ['demand_sector', 'gau', 'supply_tech'],
    "SupplyTechsVariableMaintenanceCostData" : ['demand_sector', 'gau', 'supply_tech'],
    "SupplyTechsEfficiency" : ['age_growth_or_decay_type', 'extrapolation_method', 'supply_tech', 'reference_tech', 'definition', 'interpolation_method', 'geography'],
    "SupplyEfficiency" : ['interpolation_method', 'geography', 'extrapolation_method', 'name'],
    "SupplyEmissions" : ['interpolation_method', 'geography', 'extrapolation_method', 'supply_node', 'other_index_1'],
    "SupplyCapacityFactor" : ['supply_node', 'interpolation_method', 'age_growth_or_decay_type', 'extrapolation_method', 'geography'],
    "SupplySalesData" : ['demand_sector', 'supply_technology', 'gau', 'supply_node'],
    "SupplyPotentialConversion" : ['interpolation_method', 'geography', 'extrapolation_method', 'supply_node', 'other_index_1'],
    "SupplyPotential" : ['other_index_1', 'extrapolation_method', 'supply_node', 'interpolation_method', 'geography', 'geography_map_key'],
    "SupplySalesShareData" : ['demand_sector', 'supply_technology', 'gau', 'supply_node'],
    "SupplySalesMeasures" : ['other_index_1', 'extrapolation_method', 'supply_node', 'supply_technology', 'interpolation_method', 'geography', 'geography_map_key'],
    "SupplySalesShareMeasures" : ['other_index_1', 'extrapolation_method', 'supply_node', 'supply_technology', 'interpolation_method', 'geography', 'replaced_supply_technology'],
    "SupplyStock" : ['interpolation_method', 'geography', 'geography_map_key', 'extrapolation_method', 'supply_node'],
    "SupplyExportMeasures" : ['interpolation_method', 'geography', 'extrapolation_method', 'supply_node', 'other_index_1'],
    "SupplySalesShare" : ['interpolation_method', 'geography', 'extrapolation_method', 'supply_node'],
    "SupplyExport" : ['interpolation_method', 'geography', 'extrapolation_method', 'supply_node', 'other_index_1'],
    "SupplySales" : ['interpolation_method', 'geography', 'geography_map_key', 'extrapolation_method', 'supply_node'],
    "SupplySalesMeasuresData" : ['parent', 'demand_sector', 'gau', 'oth_1'],
    "SupplySalesShareMeasuresData" : ['parent', 'demand_sector', 'gau', 'oth_1'],
    "SupplyStockData" : ['demand_sector', 'supply_technology', 'gau', 'supply_node'],
    "SupplyStockMeasures" : ['other_index_1', 'extrapolation_method', 'supply_node', 'supply_technology', 'interpolation_method', 'geography', 'geography_map_key'],
    "SupplyTechsCO2Capture" : ['age_growth_or_decay_type', 'extrapolation_method', 'supply_tech', 'definition', 'interpolation_method', 'geography'],
    "SupplyTechsCapacityFactorData" : ['supply_tech', 'gau', 'oth_1'],
    "SupplyTechsCapacityFactor" : ['age_growth_or_decay_type', 'extrapolation_method', 'supply_tech', 'definition', 'interpolation_method', 'geography'],
    "SupplyTechsInstallationCostReplacementData" : ['demand_sector', 'gau', 'supply_tech'],
    "SupplyTechsCapitalCostReplacementData" : ['demand_sector', 'gau', 'supply_tech'],
    "DemandFuelSwitchingMeasuresCostData" : ['oth_2', 'parent', 'gau', 'oth_1'],
    "BlendNodeBlendMeasuresData" : ['parent', 'demand_sector', 'gau'],
    "DemandFuelSwitchingMeasuresCost" : ['other_index_1', 'extrapolation_method', 'parent', 'currency', 'interpolation_method', 'geography', 'other_index_2'],
    "DemandCO2CaptureMeasures" : ['other_index_1', 'stock_decay_function', 'extrapolation_method', 'input_type', 'subsector', 'interpolation_method', 'geography', 'other_index_2'],
    "StorageTechsCapacityCapitalCostNewData" : ['oth_2', 'supply_tech', 'gau', 'oth_1'],
    "DemandStockMeasuresData" : ['parent', 'gau', 'oth_1'],
    "StorageTechsCapacityCapitalCostReplacementData" : ['oth_2', 'supply_tech', 'gau', 'oth_1'],
    "DemandTechsCapitalCost" : ['definition', 'extrapolation_method', 'other_index_1', 'currency', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology'],
    "BlendNodeBlendMeasures" : ['other_index_1', 'extrapolation_method', 'supply_node', 'interpolation_method', 'geography', 'blend_node'],
    "DemandEnergyEfficiencyMeasuresCostData" : ['oth_2', 'parent', 'gau', 'final_energy', 'oth_1'],
    "CO2PriceMeasuresData" : ['parent', 'gau'],
    "DemandEnergyEfficiencyMeasuresCost" : ['other_index_1', 'extrapolation_method', 'parent', 'currency', 'interpolation_method', 'geography', 'other_index_2'],
    "PrimaryCostData" : ['demand_sector', 'primary_node', 'gau', 'oth_1'],
    "SupplyCapacityFactorData" : ['demand_sector', 'gau', 'supply_node'],
    "DemandDrivers" : ['other_index_1', 'extrapolation_method', 'base_driver', 'input_type', 'interpolation_method', 'geography', 'geography_map_key', 'other_index_2'],
    "DemandTechsAuxEfficiency" : ['other_index_1', 'age_growth_or_decay_type', 'extrapolation_method', 'definition', 'interpolation_method', 'geography', 'other_index_2', 'demand_technology', 'shape', 'demand_tech_efficiency_types', 'final_energy'],
    "DemandFlexibleLoadMeasuresData" : ['parent', 'gau', 'demand_technology', 'oth_1'],
    "DemandTechs" : ['subsector', 'linked', 'stock_decay_function', 'demand_tech_unit_type', 'shape'],
    "SupplyEfficiencyData" : ['parent', 'demand_sector', 'efficiency_type', 'gau', 'supply_node'],
    "DemandTechsInstallationCostNewData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "DemandTechsServiceDemandModifierData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "SupplyExportData" : ['gau', 'supply_node', 'oth_1'],
    "SupplyExportMeasuresData" : ['parent', 'gau', 'oth_1'],
    "DemandTechsMainEfficiencyData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "PrimaryCost" : ['other_index_1', 'extrapolation_method', 'primary_node', 'currency', 'interpolation_method', 'geography'],
    "DemandTechsServiceLinkData" : ['oth_2', 'gau', 'oth_1'],
    "DemandTechsCapitalCostNewData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "DemandSubsectors" : ['shape', 'sector'],
    "Shapes" : ['other_index_1', 'extrapolation_method', 'shape_type', 'input_type', 'interpolation_method', 'geography', 'geography_map_key', 'other_index_2', 'shape_unit_type'],
    "StorageTechsCapacityCapitalCost" : ['definition', 'supply_tech', 'extrapolation_method', 'reference_tech', 'currency', 'interpolation_method', 'geography'],
    "DemandSectors" : ['shape'],
    "DemandStockData" : ['oth_2', 'subsector', 'gau', 'demand_technology', 'oth_1'],
    "DemandTechsAuxEfficiencyData" : ['oth_2', 'gau', 'demand_technology', 'oth_1'],
    "SupplyPotentialData" : ['demand_sector', 'gau', 'supply_node', 'oth_1'],
    "SupplyTechsCO2CaptureData" : ['supply_tech', 'gau'],
    "SupplyTechsEfficiencyData" : ['demand_sector', 'efficiency_type', 'gau', 'supply_node', 'supply_tech'],
    "SupplyStockMeasuresData" : ['parent', 'demand_sector', 'gau', 'oth_1'],
    "SupplyNodes" : ['stock_decay_function', 'tradable_geography', 'supply_type', 'geography_map_key', 'residual_supply_node', 'final_energy_link', 'shape'],
    "DemandServiceDemandsData" : ['oth_2', 'gau', 'subsector', 'demand_technology', 'oth_1', 'final_energy'],
}
