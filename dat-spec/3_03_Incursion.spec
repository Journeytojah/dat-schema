
type ArchitectLifeScalingPerLevel {
  Level: i32
  MoreLife: i32
}

type IncursionArchitect {
  MonsterVarietiesKey: MonsterVarieties
  MinLevel: i32
}

type IncursionBrackets {
  MinLevel: i32
  Incursion_WorldAreasKey: WorldAreas
  Template_WorldAreasKey: WorldAreas
  _: [f32]
  _: f32
  _: i32
}

type IncursionChestRewards {
  IncursionRoomsKey: IncursionRooms
  IncursionChestsKeys: [IncursionChests]
  _: string
  _: u32
  _: i32
  _: i32
}

type IncursionChests {
  Id: string @unique
  ChestsKey: Chests
  _: rid
  MinLevel: i32
  MaxLevel: i32
  Weight: i32
  _: i32
}

type IncursionRoomBossFightEvents {
  _: i32
  _: [i32]
  _: string
  _: string
  _: string
  _: string
  _: rid
}

type IncursionRooms {
  Id: string @unique
  Name: string
  Tier: i32
  MinLevel: i32
  RoomUpgrade_IncursionRoomsKey: IncursionRooms
  ModsKey: Mods
  PresentARMFile: string
  IntId: i32 @unique
  IncursionArchitectKey: IncursionArchitect
  PastARMFile: string
  TSIFile: string
  UIIcon: string
  FlavourText: string
  Description: string
  AchievementItemsKeys: [AchievementItems]
  _: i32
  _: i32
  RoomUpgradeFrom_IncursionRoomsKey: IncursionRooms
}

type IncursionUniqueUpgradeComponents {
  UniqueItemsKey: u64
  BaseItemTypesKey: BaseItemTypes
}
