
type ShrineBuffs {
  Id: string @unique
  BuffStatValues: [i32]
  BuffDefinitionsKey: BuffDefinitions
  _: rid
}

type Shrines {
  Id: string @unique
  TimeoutInSeconds: i32
  Name: string
  ChargesShared: bool
  Player_ShrineBuffsKey: ShrineBuffs
  _: i32
  _: i32
  Description: string
  Monster_ShrineBuffsKey: ShrineBuffs
  SummonMonster_MonsterVarietiesKey: MonsterVarieties
  SummonPlayer_MonsterVarietiesKey: MonsterVarieties
  _: i32
  _: i32
  ShrineSoundsKey: ShrineSounds
  _: bool
  AchievementItemsKeys: [AchievementItems]
  IsPVPOnly: bool
  _: bool
  IsLesserShrine: bool
}

type ShrineSounds {
  Id: string @unique
  StereoSoundFile: string
  MonoSoundFile: string
}
