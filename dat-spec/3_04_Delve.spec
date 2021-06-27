
type DelveAzuriteShop {
  BaseItemTypesKey: BaseItemTypes
  SpawnWeight: i32
  Cost: i32
  MinDepth: i32
  IsEnabled: bool
}

type DelveBiomes {
  Id: string @unique
  Name: string
  WorldAreasKeys: [WorldAreas]
  UIImage: string
  SpawnWeight_Depth: [i32]
  SpawnWeight_Values: [i32]
  _: [i32]
  _: [i32]
  Art2D: string
  AchievementItemsKeys: [AchievementItems]
  _: bool
  _: [i32]
}

type DelveCatchupDepths {
  _: i32
  _: i32
}

type DelveCraftingModifierDescriptions {
  Id: string @unique
  Description: string
}

type DelveCraftingModifiers {
  BaseItemTypesKey: BaseItemTypes
  AddedModsKeys: [Mods]
  NegativeWeight_TagsKeys: [Tags]
  NegativeWeight_Values: [i32]
  ForcedAddModsKeys: [Mods]
  ForbiddenDelveCraftingTagsKeys: [DelveCraftingTags]
  AllowedDelveCraftingTagsKeys: [DelveCraftingTags]
  CanMirrorItem: bool
  CorruptedEssenceChance: i32
  CanImproveQuality: bool
  CanRollEnchant: bool
  HasLuckyRolls: bool
  SellPrice_ModsKeys: [Mods]
  CanRollWhiteSockets: bool
  Weight_TagsKeys: [Tags]
  Weight_Values: [i32]
  DelveCraftingModifierDescriptionsKeys: [DelveCraftingModifierDescriptions]
  BlockedDelveCraftingModifierDescriptionsKeys: [DelveCraftingModifierDescriptions]
}

type DelveCraftingTags {
  TagsKey: Tags
  ItemClass: string
}

type DelveDynamite {
  _: i32
  Flare_MiscObjectsKey: MiscObjects
  _: rid
  Dynamite_MiscObjectsKey: MiscObjects
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  MiscAnimatedKey: MiscAnimated
  _: i32
}

type DelveFeatures {
  Id: string @unique
  Name: string
  SpawnWeight: [i32]
  WorldAreasKey: WorldAreas
  Image: string
  AchievementItemsKeys: [AchievementItems]
  MinTier: i32
  Type: string
  MinDepth: [i32]
  Description: string
  _: i32
  _: [i32]
  _: [i32]
  _: [i32]
}

type DelveFlares {
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type DelveLevelScaling {
  Depth: i32
  MonsterLevel: i32
  _: i32
  SulphiteCost: i32
  MonsterLevel2: i32
  MoreMonsterLife: i32
  MoreMonsterDamage: i32
  DarknessResistance: i32
  LightRadius: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
}

type DelveMonsterSpawners {
  BaseMetadata: string
  _: i32
  _: [u64]
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i8
  _: i32
  _: i32
  _: i32
  _: i32
  _: i32
  _: i8
  _: i8
  _: i32
  Script: string
  _: i8
}

type DelveResourcePerLevel {
  AreaLevel: i32
  Sulphite: i32
}

type DelveRooms {
  DelveBiomesKey: DelveBiomes
  DelveFeaturesKey: DelveFeatures
  ARMFile: string
}

type DelveUpgrades {
  DelveUpgradeTypeKey: i32
  UpgradeLevel: i32
  StatsKeys: [Stats]
  StatValues: [i32]
  Cost: i32
  _: i32
  AchievementItemsKey: AchievementItems
  _: i32
}

# enum?
type DelveUpgradeType { TODO_REMOVE_THIS: u8 }
