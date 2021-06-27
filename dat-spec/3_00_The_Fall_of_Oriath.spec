
type PantheonPanelLayout {
  Id: string @unique
  X: i32
  Y: i32
  IsMajorGod: bool
  CoverImage: string
  GodName2: string
  SelectionImage: string
  Effect1_StatsKeys: [Stats]
  Effect1_Values: [i32]
  Effect2_StatsKeys: [Stats]
  GodName3: string
  Effect3_Values: [i32]
  Effect3_StatsKeys: [Stats]
  GodName4: string
  Effect4_StatsKeys: [Stats]
  Effect4_Values: [i32]
  GodName1: string
  Effect2_Values: [i32]
  QuestState1: i32
  QuestState2: i32
  QuestState3: i32
  QuestState4: i32
  IsDisabled: bool
  _: [rid]
}

type PantheonSouls {
  WorldAreasKey: WorldAreas
  BaseItemTypesKey: BaseItemTypes
  _: i32
  MonsterVarietiesKey: MonsterVarieties
  PantheonPanelLayoutKey: PantheonPanelLayout
}
