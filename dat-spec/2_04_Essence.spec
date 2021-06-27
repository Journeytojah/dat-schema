
type Essences {
  BaseItemTypesKey: BaseItemTypes @unique
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  _: u64
  Display_Wand_ModsKey: Mods
  Display_Bow_ModsKey: Mods
  Display_Quiver_ModsKey: Mods
  Display_Amulet_ModsKey: Mods
  Display_Ring_ModsKey: Mods
  Display_Belt_ModsKey: Mods
  Display_Gloves_ModsKey: Mods
  Display_Boots_ModsKey: Mods
  Display_BodyArmour_ModsKey: Mods
  Display_Helmet_ModsKey: Mods
  Display_Shield_ModsKey: Mods
  _: i32
  DropLevelMinimum: i32
  DropLevelMaximum: i32
  Monster_ModsKeys: [Mods]
  EssenceTypeKey: EssenceType
  Level: i32
  _: i32
  Display_Weapon_ModsKey: Mods
  Display_MeleeWeapon_ModsKey: Mods
  Display_OneHandWeapon_ModsKey: Mods
  Display_TwoHandWeapon_ModsKey: Mods
  Display_TwoHandMeleeWeapon_ModsKey: Mods
  Display_Armour_ModsKey: Mods
  Display_RangedWeapon_ModsKey: Mods
  Helmet_ModsKey: Mods
  BodyArmour_ModsKey: Mods
  Boots_ModsKey: Mods
  Gloves_ModsKey: Mods
  Bow_ModsKey: Mods
  Wand_ModsKey: Mods
  Staff_ModsKey: Mods
  TwoHandSword_ModsKey: Mods
  TwoHandAxe_ModsKey: Mods
  TwoHandMace_ModsKey: Mods
  Claw_ModsKey: Mods
  Dagger_ModsKey: Mods
  OneHandSword_ModsKey: Mods
  OneHandThrustingSword_ModsKey: Mods
  OneHandAxe_ModsKey: Mods
  OneHandMace_ModsKey: Mods
  Sceptre_ModsKey: Mods
  Display_Monster_ModsKey: Mods
  ItemLevelRestriction: i32
  Belt_ModsKey: Mods
  Amulet_ModsKey: Mods
  Ring_ModsKey: Mods
  Display_Jewellery_ModsKey: Mods
  Shield_ModsKey: Mods
  Display_Items_ModsKey: Mods
  IsScreamingEssence: bool
}

type EssenceType {
  Id: string
  EssenceType: i32
  IsCorruptedEssence: bool
  WordsKey: Words
}
