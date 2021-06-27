
type PerandusBosses {
  MonsterVarietiesKey: MonsterVarieties
  MinLevel: i32
  MaxLevel: i32
  SpawnWeight: i32
}

type PerandusChests {
  ChestsKey: Chests
  _: i32
  _: i32
  MinLevel: i32
  MaxLevel: i32
}

type PerandusDaemons {
  MonsterVarietiesKey: MonsterVarieties
  _: i32
  _: i32
  _: i32
  _: i32
  _: [u64]
  _: bool
  _: [u64]
}

type PerandusGuards {
  Id: string
  _: i32
  MinLevel: i32
  MaxLevel: i32
  MonsterPacksKeys: [MonsterPacks]
  _: i32
  _: [u32]
  _: i32
}
