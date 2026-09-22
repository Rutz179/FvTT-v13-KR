# sync 리포트

`git diff lang/ko.json` 으로 실제 변경을 함께 확인하세요.

## 키 이동으로 번역을 옮긴 항목 (특히 '추정'은 한 번 훑어보세요)

| 새 키 | 영어 | 가져온 번역 | 옛 키 | 방식 |
|---|---|---|---|---|
| `HOTBAR.Label` | Action Bar | 액션 바 | `HOTBAR.LABEL` | 경로 일치 |
| `HOTBAR.Empty` | Empty Slot | 슬롯 비우기 | `HOTBAR.EMPTY` | 경로 일치 |
| `HOTBAR.ClearConfirm` | Clear all assigned Macros from your hotbar? | 할당된 모든 매크로를 액션 바에서 제거하시겠습니까? | `HOTBAR.CLEAR_CONFIRM` | 경로 일치 |
| `LIGHT.ANIMATION.Torch` | Flickering Light | 깜박이는 빛 | `LIGHT.AnimationTorch` | 경로 일치 |
| `LIGHT.ANIMATION.Pulse` | Pulse | 맥동 | `LIGHT.AnimationPulse` | 경로 일치 |
| `LIGHT.ANIMATION.ReactivePulse` | Sound-Reactive Pulse | 사운드 반응 펄스 | `LIGHT.AnimationReactivePulse` | 경로 일치 |
| `LIGHT.ANIMATION.Chroma` | Chroma | 크로마 | `LIGHT.AnimationChroma` | 경로 일치 |
| `LIGHT.ANIMATION.Wave` | Pulsing Wave | 맥동하는 파동 | `LIGHT.AnimationWave` | 경로 일치 |
| `LIGHT.ANIMATION.Fog` | Swirling Fog | 소용돌이 안개 | `LIGHT.AnimationFog` | 경로 일치 |
| `LIGHT.ANIMATION.Sunburst` | Sunburst | 방사 태양광 | `LIGHT.AnimationSunburst` | 경로 일치 |
| `LIGHT.ANIMATION.LightDome` | Light Dome | 빛 돔 | `LIGHT.AnimationLightDome` | 경로 일치 |
| `LIGHT.ANIMATION.Emanation` | Mysterious Emanation | 신비한 발산 | `LIGHT.AnimationEmanation` | 경로 일치 |
| `LIGHT.ANIMATION.EnergyField` | Energy Field | 에너지 필드 | `LIGHT.AnimationEnergyField` | 경로 일치 |
| `LIGHT.ANIMATION.HexaDome` | Hexa Dome | 육각 돔 | `LIGHT.AnimationHexaDome` | 경로 일치 |
| `LIGHT.ANIMATION.GhostLight` | Ghostly Light | 유령 빛 | `LIGHT.AnimationGhostLight` | 경로 일치 |
| `LIGHT.ANIMATION.RoilingMass` | Roiling Mass | 탁류 덩어리 (어둠) | `LIGHT.AnimationRoilingMass` | 경로 일치 |
| `LIGHT.ANIMATION.BlackHole` | Black Hole | 블랙 홀 (어둠) | `LIGHT.AnimationBlackHole` | 경로 일치 |
| `LIGHT.ANIMATION.Vortex` | Vortex | 소용돌이 | `LIGHT.AnimationVortex` | 경로 일치 |
| `LIGHT.ANIMATION.BewitchingWave` | Bewitching Wave | 요염한 파도 | `LIGHT.AnimationBewitchingWave` | 경로 일치 |
| `LIGHT.ANIMATION.SwirlingRainbow` | Swirling Rainbow | 무지개 회오리 | `LIGHT.AnimationSwirlingRainbow` | 경로 일치 |
| `LIGHT.ANIMATION.RadialRainbow` | Radial Rainbow | 방사형 무지개 | `LIGHT.AnimationRadialRainbow` | 경로 일치 |
| `LIGHT.ANIMATION.FairyLight` | Fairy Light | 요정 빛 | `LIGHT.AnimationFairyLight` | 경로 일치 |
| `LIGHT.ANIMATION.Flame` | Torch | 횃불 | `LIGHT.AnimationFlame` | 경로 일치 |
| `LIGHT.ANIMATION.ForceGrid` | Force Grid | 격자무늬 역장 | `LIGHT.AnimationForceGrid` | 경로 일치 |
| `LIGHT.ANIMATION.StarLight` | Star Light | 별빛 | `LIGHT.AnimationStarLight` | 경로 일치 |
| `LIGHT.ANIMATION.SmokePatch` | Smoke Patch | 연기 장막 | `LIGHT.AnimationSmokePatch` | 경로 일치 |
| `LIGHT.ANIMATION.Revolving` | Revolving Light | 회전하는 빛 | `LIGHT.AnimationRevolving` | 경로 일치 |
| `LIGHT.ANIMATION.Siren` | Siren Light | 사이렌 빛 | `LIGHT.AnimationSiren` | 경로 일치 |
| `LIGHT.ANIMATION.MagicalGloom` | Magical Gloom | 마법의 빛 | `LIGHT.AnimationMagicalGloom` | 경로 일치 |
| `LIGHT.ANIMATION.DenseSmoke` | Dense Smoke | 짙은 연기 | `LIGHT.AnimationDenseSmoke` | 경로 일치 |
| `PLAYLIST_SOUND.Create` | Create Sound | 음원 생성 | `PLAYLIST.SoundCreate` | 경로 일치 |
| `HOTBAR.ACTIONS.Clear` | Clear Hotbar | 액션 바 비우기 | `HOTBAR.CLEAR` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.Mute` | Mute Volume | 볼륨 음소거 | `HOTBAR.MUTE` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.Unmute` | Unmute Volume | 볼륨 음소거 해제 | `HOTBAR.UNMUTE` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.Menu` | Main Menu | 메인 메뉴 | `HOTBAR.MENU` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.Lock` | Lock Hotbar | 액션 바 잠금 | `HOTBAR.LOCK` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.Unlock` | Unlock Hotbar | 액션 바 잠금 해제 | `HOTBAR.UNLOCK` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.PageNext` | Next Page | 다음 페이지 | `HOTBAR.PAGE_NEXT` | 이름 일치(추정) |
| `HOTBAR.ACTIONS.PagePrev` | Previous Page | 이전 페이지 | `HOTBAR.PAGE_PREV` | 이름 일치(추정) |
| `LIGHT.COLORATION.AdaptiveLuminance` | Adaptive Luminance | 휘도 적정화 | `LIGHT.AdaptiveLuminance` | 이름 일치(추정) |
| `LIGHT.COLORATION.InternalHalo` | Internal Halo | 내부 빛무리 | `LIGHT.InternalHalo` | 이름 일치(추정) |
| `LIGHT.COLORATION.ExternalHalo` | External Halo | 외부 빛무리 | `LIGHT.ExternalHalo` | 이름 일치(추정) |
| `LIGHT.COLORATION.ColorBurn` | Color Burn | 색상 번 | `LIGHT.ColorBurn` | 이름 일치(추정) |
| `LIGHT.COLORATION.InternalBurn` | Internal Color Burn | 내부 색상 번 | `LIGHT.InternalBurn` | 이름 일치(추정) |
| `LIGHT.COLORATION.ExternalBurn` | External Color Burn | 외부 색상 번 | `LIGHT.ExternalBurn` | 이름 일치(추정) |
| `LIGHT.COLORATION.LowAbsorption` | Low Absorption | 낮은 흡수 | `LIGHT.LowAbsorption` | 이름 일치(추정) |
| `LIGHT.COLORATION.HighAbsorption` | High Absorption | 높은 흡수 | `LIGHT.HighAbsorption` | 이름 일치(추정) |
| `LIGHT.COLORATION.InvertAbsorption` | Invert Absorption | 흡수 반전 | `LIGHT.InvertAbsorption` | 이름 일치(추정) |
| `LIGHT.COLORATION.NaturalLight` | Natural Light | 자연광 | `LIGHT.NaturalLight` | 이름 일치(추정) |
| `SCENE.Environment.Base` | Base Environment | 베이스 앰비언스 | `SCENE.Ambience.Base` | 이름 일치(추정) |
| `SCENE.Environment.Dark` | Darkness Environment | 어두운 분위기 | `SCENE.Ambience.Dark` | 이름 일치(추정) |
| `SCENE.TABS.SHEET.environment` | Environment | 환경 조명 | `SCENE.TABS.AMBIENCE.environment` | 이름 일치(추정) |

## 같은 영어 문장의 기존 번역을 재사용한 항목

| 키 | 영어 | 번역 |
|---|---|---|
| `HUD.Hide` | Hide | 숨기기 |
| `HUD.Lock` | Lock | 잠금 |
| `MEASUREMENT.Height` | Height | 높이 |
| `MEASUREMENT.Width` | Width | 너비 |
| `SCENE.GridAppearance` | Appearance | 모양 |
| `SCENE.TABS.SHEET.levels` | Levels | 레벨(층고) |
| `SCENE_LEVEL.FIELDS.background.color.label` | Color | 색상 |
| `SETUP.ACTIONS.Logout` | Log Out | 로그아웃 |
| `SETUP.ACTIONS.Update` | Update | 업데이트 |
| `SETUP.SYSTEM_FILTER.Label` | Systems | 시스템 |
| `PACKAGE.RESULT.Update` | Update | 업데이트 |
| `REGION.TABS.appearance` | Appearance | 모양 |
| `BEHAVIOR.TYPES.teleportToken.PLACEMENTS.center.label` | Center | 중앙 |
| `SIDEBAR.PLACEABLES.ACTIONS.Hide` | Hide | 숨기기 |
| `SIDEBAR.PLACEABLES.ACTIONS.Lock` | Lock | 잠금 |
| `TILE.TABS.video` | Video | 비디오 |
| `TILE.FIELDS.name.label` | Name | 이름 |
| `TIME.Day.two` | Days | 일 |
| `TIME.Day.few` | Days | 일 |
| `TIME.Day.many` | Days | 일 |
| `TIME.Hour.two` | Hours | 시간 |
| `TIME.Hour.few` | Hours | 시간 |
| `TIME.Hour.many` | Hours | 시간 |
| `TIME.Minute.two` | Minutes | 분 |
| `TIME.Minute.few` | Minutes | 분 |
| `TIME.Minute.many` | Minutes | 분 |
| `TIME.Second.two` | Seconds | 초 |
| `TIME.Second.few` | Seconds | 초 |
| `TIME.Second.many` | Seconds | 초 |
| `TIME.Year.two` | Years | 년 |
| `TIME.Year.few` | Years | 년 |
| `TIME.Year.many` | Years | 년 |
| `SHAPE.labelPlural` | Shapes | 모양 |
| `SHAPE.TYPES.cone.CURVATURES.round.label` | Round | 라운드 |
| `SHAPE.TYPES.line.FIELDS.width.label` | Width | 너비 |
| `SHAPE.TYPES.token.FIELDS.width.label` | Width | 너비 |
| `SHAPE.TYPES.token.FIELDS.height.label` | Height | 높이 |
| `SHAPE.TYPES.token.position.label` | Position | 위치 |

## 치환자/태그가 영어 원문과 안 맞는 기존 번역 (stale 로 표시, export 에 포함됨)

영어 원문이 바뀌었거나 DeepL 이 `{count}` → `{개수}` 처럼 치환자를 번역해 버린 경우입니다.

- `COMBATANT.UpdateNamed`: 치환자 누락 {name}, 중괄호 짝 안 맞음  
  EN: Update Combatant: {name}  
  KO: 전투원 업데이트: {name
- `FILES.ErrorDisallowedExtension`: 치환자 누락 {allowed}, 원문에 없는 치환자 {허용됨}  
  EN: File "{name}" has an invalid extension "{ext}" which is not allowed for this …  
  KO: 파일 "{name}"의 확장자 "{ext}"가 이 FilePicker 유형에 허용되지 않는 잘못된 확장자입니다. 허용되는 확장명은 다음과 …
- `KEYBINDINGS.ErrorProtectedKey`: 치환자 누락 {key}, 원문에 없는 치환자 {키}  
  EN: Cannot set the Protected Key "{key}" as a binding.  
  KO: 보호된 키 "{키}"는 바인딩으로 사용할 수 없습니다.
- `KEYBINDINGS.ErrorIllegalModifier`: 치환자 누락 {key}, 원문에 없는 치환자 {키}  
  EN: The requested modifier key "{key}" is not a valid value in KeyboardManager.MO…  
  KO: 지정된 조합 키 "{키}"는 유효한 수정 키가 아닙니다 (KeyboardManager.MODIFIER_KEYS 참조).
- `KEYBINDINGS.ErrorReservedModifier`: 치환자 누락 {key}, 원문에 없는 치환자 {키}  
  EN: Cannot set "{key}" as a Binding, as it is a reserved modifier for this Keybin…  
  KO: "{키}"는 이 동작에 예약된 조합 키이므로 사용할 수 없습니다.
- `MACRO.EmptySlot`: 치환자 누락 {slot}, 원문에 없는 치환자 {슬롯}  
  EN: Empty Slot {slot}  
  KO: 빈 슬롯 {슬롯}
- `SETUP.NoSystemsMessage`: HTML 태그 불일치  
  EN: In order to create your first World, you must first install a <a class="syste…  
  KO: 첫 번째 월드를 생성하려면 먼저 <a class="system-install" data-query="" title="게임 시스템">게임 시…
- `SETUP.SeeTutorial`: HTML 태그 불일치  
  EN: For a more in-depth guide to getting started with Foundry Virtual Tabletop, y…  
  KO: Foundry Virtual Tabletop을 시작하는 방법에 대한 자세한 가이드는 <a href="https://foundryvtt.co…
- `SETUP.ErrorTimeout`: 치환자 누락 {timeout}  
  EN: The request to {url} timed out after {timeout}s  
  KO: {url}에 대한 요청이 {시간 초과}초 후에 시간 초과되었습니다.
- `SETUP.InstallSuccess`: 치환자 누락 {id}, 원문에 없는 치환자 {ID}  
  EN: {type} {id} was installed successfully  
  KO: {type} {ID}가 성공적으로 설치되었습니다.
- `SETUP.PackageDependenciesCouldNotInstallPlural`: 치환자 누락 {number}, 원문에 없는 치환자 {숫자}  
  EN: {number} dependencies need to be manually installed.  
  KO: {숫자} 종속성을 수동으로 설치해야 합니다.
- `SETUP.PackageDependenciesCouldInstallPlural`: 치환자 누락 {number}, 원문에 없는 치환자 {숫자}  
  EN: {number} dependencies can be automatically installed.  
  KO: {숫자} 종속성을 자동으로 설치할 수 있습니다.
- `SETUP.PackageDependenciesDecline`: 치환자 누락 {title}, 중괄호 짝 안 맞음  
  EN: You have chosen not to install the required dependency packages for {title}. …  
  KO: title}에 필요한 종속성 패키지를 설치하지 않기로 선택했습니다. 수동으로 설치해야 합니다.
- `SETUP.PackageUpdateCoreUpdateNeeded`: 치환자 누락 {title}, 중괄호 짝 안 맞음  
  EN: An update is available for {title} but cannot be installed because it require…  
  KO: title}에 대한 업데이트를 사용할 수 있지만 에 대한 업데이트를 사용할 수 있지만 코어 소프트웨어를 {vmin} 이상으로 업데이트해야 …
- `SETUP.PackageUpdateCoreUnstable`: 치환자 누락 {title}, 중괄호 짝 안 맞음  
  EN: An update is available for {title} but it may not be installed because it req…  
  KO: title}에 대한 업데이트를 사용할 수 있지만 에 대한 업데이트를 사용할 수 있지만 아직 안정적이지 않은 핵심 소프트웨어 버전 {vmin…
- `SETUP.PackageIncompatibleWithSystems`: 치환자 누락 {systems}, 원문에 없는 치환자 {system}  
  EN: {module} <em>incompatible with</em> {systems}  
  KO: {module} <em>호환되지 않음</em> {system}
- `SETUP.BACKUPS.DeleteBackupCompletePl`: 치환자 누락 {count}, 원문에 없는 치환자 {개수}  
  EN: Deleted {count} backups for {title}.  
  KO: {title}에 대한 {개수} 백업을 삭제했습니다.
- `SETUP.COMPAT.RISK.Latest`: 치환자 누락 {verified}, 원문에 없는 치환자 {확인됨}  
  EN: The latest version of this package was last verified for core software versio…  
  KO: 이 패키지의 최신 버전은 마지막으로 핵심 소프트웨어 버전 {확인됨}과의 호환성이 확인되었습니다.
- `SETUP.COMPAT.RISK.World`: 치환자 누락 {verified}, 원문에 없는 치환자 {확인됨}  
  EN: This world's system was last verified for core software version {verified}  
  KO: 이 월드의 시스템은 마지막으로 핵심 소프트웨어 버전 {확인됨}과의 호환성이 확인되었습니다.
- `FOLDER.DeleteWarning`: HTML 태그 불일치  
  EN: This folder and its contents will be permanently deleted and cannot be recove…  
  KO: <h3>정말 삭제하시겠습니까?</h3><p>이 폴더 및 모든 내용물이 <strong>영구적으로 삭제되며</strong> 복원할 수 없습니다…
- `FOLDER.RemoveWarning`: HTML 태그 불일치  
  EN: This folder will be permanently deleted and its contents will be moved to its…  
  KO: <h3>정말로 제거하시겠습니까?</h3><p>이 폴더가 삭제되며 내용물은 상위 폴더로 이동됩니다.</p>
- `FOLDER.Exporting`: 원문에 없는 치환자 {n}  
  EN: Exporting {type} to Compendium {compendium}.  
  KO: {n} {type} 문서를 {compendium} 컴펜디엄으로 내보내기합니다.
- `SUPPORT.Dimensions`: 중괄호 짝 안 맞음  
  EN: {width} × {height}  
  KO: {width} 높이} × {height}
- `SUPPORT.ModuleSubTypesUnavailableName`: 치환자 누락 {count}, HTML 태그 불일치  
  EN: <strong>{count}</strong> {document} are unavailable because the '{name}' modu…  
  KO: <'{name}' 모듈이 비활성 상태이므로 {document}를 사용할 수 없습니다.
- `SUPPORT.ModuleSubTypesUnavailableNoName`: 치환자 누락 {count}, HTML 태그 불일치  
  EN: <strong>{count}</strong> {document} are unavailable because a module with the…  
  KO: <ID가 '{name}'인 모듈이 비활성 상태이므로 {document}를 사용할 수 없습니다.
- `TOURS.InProgress`: 치환자 누락 {current} {total}, 원문에 없는 치환자 {총계} {현재}  
  EN: In Progress - {current}/{total}  
  KO: 진행 중 - {현재}/{총계}

## 영어가 그대로 들어 있던 값 (제거 → 미번역으로 export 됨)

- `CONTROLS.RegionTemplateMode`: Measured Template Mode
- `CONTROLS.RegionTemplateModeP`: When enabled, the palette is ignored and each shape you draw creates a new Re…
- `EDITOR.ImageDimensionsHint`: Leaving these blank will use the image's intrinsic size.
- `EDITOR.LinkURL`: Link URL
- `EDITOR.LinkText`: Link Text
- `EDITOR.LinkTitle`: Link Title
- `EDITOR.LinkInsert`: Insert Link
- `EDITOR.ProseMirrorBadArguments`: Both a document and a name must be supplied to create a ProseMirror instance.
- `EDITOR.TableDeleteColumn`: Delete Column
- `EDITOR.TableAddRowAfter`: Add Row After
- `EDITOR.TableAddRowBefore`: Add Row Before
- `EDITOR.TableDeleteRow`: Delete Row
- `EDITOR.TableMergeCells`: Merge Cells
- `EDITOR.TableSplitCell`: Split Cell
- `ELEMENTS.TAGS.ErrorBlank`: Tags in an HTMLStringTagsElement may not be blank.
- `ELEMENTS.TAGS.ErrorNonUnique`: Tag "{tag}" is already set.
- `FILES.DirectoryName.Placeholder`: my-folder
- `FONTS.File`: Font File
- `MODMANAGE.OptionalDependencies`: Optional Dependencies
- `NOTE.FIELDS.texture.tint.label`: Icon Tint
- `SCENE.FIELDS.environment.base.intensity.label`: Hue Intensity
- `SETUP.RequiredPackageNote`: This dependency is required for the package to function.
- `SETUP.BACKUPS.DeleteSnapshotTitle`: Deleting Snapshots
- `SETUP.BACKUPS.DiskSpaceChecking`: Checking Space
- `SETUP.UPDATE_NOTES.FullList`: See the <a href="{url}" target="_blank">full list</a> of Release Notes.
- `PACKAGE.NewModuleTitle`: My New Module
- `SOUND.PathPlaceholder`: path/to/audio.mp3
- `FOLDER.DeleteName`: Delete All: {name}
- `FOLDER.RemoveName`: Remove Folder: {name}
- `PERMISSION.QueryUser`: Query Users
- `SUPPORT.Viewport`: Viewport Dimensions
- `TILE.ACTIONS.CREATE`: Create Tile
- `TILE.ACTIONS.UPDATE`: Update Tile
- `TILE.FIELDS.texture.tint.label`: Tint Color
- `TILE.FIELDS.video.volume.label`: Video Volume

## en.json 에서 사라져 ko.json 에서도 삭제된 키

<details><summary>펼치기</summary>

- `CONTROLS.DrawingRole`: 정보 도면 토글
- `CONTROLS.WallBasic`: 기본 벽
- `CONTROLS.WallBasicBlocks`: 움직임, 시각, 청각
- `CONTROLS.WallDoors`: 문 그리기
- `CONTROLS.DoorBlocks`: 열지 않으면 움직임, 시각 및 청각
- `CONTROLS.WallClone`: 벽 복제
- `ERROR.InvalidAdminKey`: 제공한 서버 관리자 비밀번호가 유효하지 않습니다. 구성된 비밀번호를 잊어버린 경우 사용자 데이터 위치에서 <strong>Config/adm…
- `HUD.ToggleTargetState`: 목표 상태 활성화
- `HUD.ToggleCombatState`: 전투 상태 전환
- `HUD.ToggleVis`: 공개/비공개 전환
- `HUD.ToggleLock`: 잠금/해제 전환
- `HUD.ToFront`: 앞으로 가져오기
- `HUD.ToBack`: 뒤로 보내기
- `JOURNAL.EntryTitle`: 엔트리 제목
- `JOURNALENTRYPAGE.Format`: 형식
- `JOURNALENTRYPAGE.PageTitle`: 페이지 이름
- `JOURNALENTRYPAGE.Source`: 경로
- `JOURNALENTRYPAGE.Type`: 유형
- `JOURNALENTRYPAGE.TypeImage`: 이미지
- `JOURNALENTRYPAGE.TypePDF`: PDF
- `JOURNALENTRYPAGE.TypeText`: 텍스트
- `JOURNALENTRYPAGE.TypeVideo`: 비디오
- `JOURNALENTRYPAGE.ImageSource`: 이미지 경로
- `JOURNALENTRYPAGE.ImageCaption`: 이미지 캡션
- `JOURNALENTRYPAGE.VideoAutoplay`: Autoplay Video
- `JOURNALENTRYPAGE.VideoControls`: 비디오 조작 표시
- `JOURNALENTRYPAGE.VideoLoop`: Loop Video
- `JOURNALENTRYPAGE.VideoSource`: 비디오 경로
- `JOURNALENTRYPAGE.VideoVolume`: Video Volume
- `JOURNALENTRYPAGE.PDFSource`: PDF 경로
- `JOURNALENTRYPAGE.ShowTitle`: 이미지 제목 표시
- `JOURNALENTRYPAGE.HeadingLevel`: 제목 계층 레벨
- `JOURNALENTRYPAGE.Category`: Page Category
- `LIGHT.LegacyColoration`: 레거시 색상화
- `PLAYLIST.Delete`: 재생목록 삭제
- `PLAYLIST.Edit`: 재생목록 편집
- `SCENE.Configure`: 구성
- `SCENE.GridScale`: 그리드 스케일
- `SCENE.Pixels`: 픽셀
- `SCENE.Ambience.ResetEnvironment`: 기본 옵션으로 재설정
- `SCENE.FIELDS.foreground.label`: 전경 이미지
- `SCENE.FIELDS.foreground.hint`: 장면의 다른 오브젝트 위에 그려지는 선택적 전경 이미지입니다.
- `SCENE.FIELDS.foregroundElevation.label`: 전경 고도
- `SCENE.FIELDS.foregroundElevation.hint`: 전경 이미지와 오버헤드 타일의 높이를 구성하는 거리 단위의 고도입니다.
- `SCENE.FIELDS.fog.exploration.label`: 전장의 안개 탐색
- `SCENE.FIELDS.fog.exploration.hint`: 이 설정을 활성화하면 장면을 탐색할 때 사용자별로 전장의 안개 탐색이 추적되어 데이터베이스에 저장됩니다. 그렇지 않으면 전장의 안개 탐색이…
- `SCENE.TABS.SHEET.lighting`: 조명
- `SCENE.TABS.SHEET.ambience`: 분위기
- `SCENE.TABS.AMBIENCE.basic`: 기본 옵션
- `SETTINGS.CombatConfigN`: 전투 트래커
- `SETUP.ManifestUpdate`: Updated version available at new installation URL
- `SETUP.ManifestUpdateAvailable`: A newer version of "{package}" is available at a different installation URL. …
- `SETUP.PriorManifestUrl`: 이전 매니페스트 URL(버전 {version})
- `SETUP.UpdatedManifestUrl`: 업데이트된 창작물 URL(버전 {version})
- `SETUP.SwapToTheUpdatedManifest`: 새 창작물 URL로 전환하시겠습니까? (권장)
- `SETUP.UpdateWarningWillDisable`: 이 업데이트는 Foundry Virtual Tabletop 소프트웨어의 새로운 주요 버전입니다. 이 업데이트를 설치하면 아직 호환되지 않을…
- `SETUP.AdminPasswordForgot`: 관리자 비밀번호를 잊어버린 경우 서버 관리자가 <a href='https://foundryvtt.com/article/reset-admin…
- `SHEETS.CopyUuid`: 문서 UUID 복사
- `PERMISSION.TemplateCreate`: 측정 템플릿 생성
- `PERMISSION.TemplateCreateHint`: 이 역할의 플레이어가 범위 측정을 위한 템플릿을 생성할 수 있도록 허용합니다.
- `REGION.TABS.identity`: 정체성
- `REGION.ACTIONS.shapeCreateFromWalls`: 선택 중인 벽의 모양대로 모양 생성
- `REGION.ACTIONS.shapeMakeHole`: 구멍 만들기
- `REGION.ACTIONS.shapeFillHole`: 구멍 채우기
- `REGION.ACTIONS.shapeMoveUp`: 모양 위로 이동하기
- `REGION.ACTIONS.shapeMoveDown`: 모양 아래로 이동하기
- `REGION.ACTIONS.shapeRemove`: 모양 삭제
- `REGION.ACTIONS.behaviorCreate`: 행동 생성
- `REGION.SHAPES.rectangle`: 직사각형
- `REGION.SHAPES.circle`: 원
- `REGION.SHAPES.ellipse`: 타원
- `REGION.SHAPES.polygon`: 다각형
- `REGION.Shape`: 모양
- `REGION.NOTIFICATIONS.ControlWalls`: 벽을 조정해 구역의 경계선을 원하는 모양으로 만듭니다.
- `REGION.NOTIFICATIONS.DrawingMultipleRegionsControlled`: 모양을 그리려면 구역을 1개만 선택하거나, 구역을 선택하지 않은 상태여야 합니다!
- `REGION.NOTIFICATIONS.EmptyEnclosedArea`: 벽으로 둘러싸인 공간이 없습니다! 벽의 끝점끼리 서로 연결되어 닫힌 공간을 만들고 있는지 확인하세요.
- `REGION.NOTIFICATIONS.NoControlledWalls`: 선택 중인 벽이 없습니다!
- `BEHAVIOR.TYPES.teleportToken.FIELDS.destination.label`: 목적지
- `BEHAVIOR.TYPES.teleportToken.FIELDS.destination.hint`: 구역에 들어온 토큰을 이 구역으로 순간이동시킵니다.
- `BEHAVIOR.TYPES.teleportToken.ConfirmGM`: {scene} 장면의 {region} 영역으로 {token}을(를) 텔레포트하시겠습니까?
- `TEMPLATE.ConeTypeSetting`: 부채꼴형 템플릿 모양
- `TEMPLATE.ConeTypeSettingHint`: 부채꼴형 템플릿에 어떤 효과를 적용할지 선택합니다. 격자 기반 템플릿 모양 옵션이 활성화되어있으면 이 설정은 무효화됩니다.
- `TEMPLATE.ConeTypeFlat`: 평평한 호
- `TEMPLATE.ConeTypeRound`: 둥근 호
- `TEMPLATE.SubmitCreate`: 측정 템플릿 생성
- `TEMPLATE.SubmitUpdate`: 측정 템플릿 업데이트
- `TEMPLATE.GridTemplatesSetting`: 격자 기반 템플릿 모양
- `TEMPLATE.GridTemplatesSettingHint`: 유클리드형 모양 대신 격자 기반으로 템플릿을 적용할지 여부를 설정합니다.
- `TEMPLATE.TYPES.circle`: 원형
- `TEMPLATE.TYPES.cone`: 원뿔형
- `TEMPLATE.TYPES.ray`: 광선형
- `TEMPLATE.TYPES.rect`: 직사각형
- `TEMPLATE.FIELDS.sort.label`: 정렬
- `TEMPLATE.FIELDS.t.label`: 유형
- `TEMPLATE.FIELDS.direction.label`: 방향
- `TEMPLATE.FIELDS.angle.label`: 각도
- `TEMPLATE.FIELDS.distance.label`: 거리
- `TEMPLATE.FIELDS.borderColor.label`: 테두리 색상
- `TEMPLATE.FIELDS.fillColor.label`: 채우기 색상
- `TEMPLATE.FIELDS.texture.label`: 채우기 텍스처
- `TILE.OcclusionModeRoof`: 천장 (시야 및 조명 차단)
- `TILE.FIELDS.occlusion.mode.label`: 오클루전 모드
- `TOKEN.Dimensions`: 크기
- `TOKEN.DetectionAdd`: 탐지 모드 추가
- `Activate`: 활성화
- `all`: 모두
- `Anchor`: 중심축
- `Angle`: 각도
- `Author`: 만든 이
- `AuthorPl`: 만든 이
- `AreYouSure`: <strong>정말로 실행하시겠습니까?</strong>
- `and`:  그리고
- `authorized`: 인증됨
- `Between`: 사이
- `Cancel`: 취소
- `Character`: 캐릭터
- `Configure`: 설정
- `Confirm`: 확인
- `Command`: 커맨드
- `Collapse`: 접기
- `Coordinates`: 좌표
- `Close`: 닫기
- `Deactivate`: 비활성화
- `Degrees`: °
- `Default`: 기본값
- `Delete`: 삭제
- `DeleteSelected`: 선택 삭제
- `Description`: 설명
- `Distance`: 거리 단위
- `Display`: 표시
- `Direction`: 방향
- `Documentation`: 문서
- `Duplicate`: 복제
- `Error`: 오류
- `Errors`: 오류
- `Expand`: 펼치기
- `GridUnits`: 격자 칸
- `GridSpaces`: 격자 크기
- `Install`: 설치
- `Elevation`: 고도
- `Sort`: 정렬
- `Foundry Virtual Tabletop`: Foundry Virtual Tabletop
- `File Path`: 파일 경로
- `Height`: 높이
- `Hidden`: 숨겨짐
- `Hold`: 계속 누르기
- `Information`: 정보
- `Light`: 빛
- `Name`: 이름
- `Next`: 다음
- `No`: 아니오
- `Notes`: 노트
- `Preload`: 미리 불러오기
- `Previous`: 이전
- `Token`: 토큰
- `Minimum`: 최소
- `Maximum`: 최대
- `Image`: 이미지
- `Invalid`: 유효하지 않음
- `None`: 없음
- `Path`: 경로
- `Packs`: 팩
- `Permissions`: 권한
- `Position`: 위치
- `Pixels`: 픽셀
- `Preview`: 미리보기
- `Ratio`: 비율
- `Reset`: 초기화
- `Resources`: 자원
- `Result`: 결과
- `Resize`: 크기조정
- `Rotation`: 회전
- `Roll Formula`: 굴림 수식
- `Commit Change`: 변경 내용 확인
- `Reset Changes`: 변경 내용 초기화
- `Save`: 저장
- `Save Changes`: 변경 내용 저장
- `Scale`: 배율
- `Scope`: 범위
- `Seconds`: 초
- `selected`: 선택됨
- `SelectAll`: 모두 선택
- `Sight`: 시야
- `Sheet`: 시트
- `System`: 시스템
- `Software`: 소프트웨어
- `Sound`: 소리
- `spaces`: 칸
- `Template`: 템플릿
- `Type`: 타입
- `Uninstall`: 제거
- `units`: 단위
- `Unknown`: 미지
- `Update`: 업데이트
- `URL`: URL
- `Vision`: 시야
- `Warning`: 경고
- `Warnings`: 경고
- `Width`: 너비
- `XCoord`: X 좌표
- `YCoord`: Y 좌표
- `Yes`: 예
- `APP.NavigateBackConfirm`: 정말로 Foundry Virtual Tabletop을 종료하시겠습니까?
- `AMBIENT_LIGHT.FIELDS.x.label`: X
- `AMBIENT_LIGHT.FIELDS.y.label`: Y
- `AMBIENT_LIGHT.FIELDS.elevation.label`: 높이
- `AMBIENT_SOUND.FIELDS.elevation.label`: 높이
- `CHAT.RollBlind`: 결과 숨김 굴림 (GM만)
- `CHAT.RollDefault`: 기본 굴림 모드
- `CHAT.RollPublic`: 공개 굴림
- `CHAT.RollPrivate`: 비공개 굴림 (나와 GM만)
- `CHAT.RollSelf`: 혼잣말 굴림 (나만)
- `COMBAT.Delete`: 인카운터 삭제
- `COMBAT.Encounter`: 인카운터
- `COMBAT.InitiativeScore`: 이니셔티브 점수
- `COMBAT.PanToCombatant`: 전투원 쪽으로 화면 이동
- `COMBAT.PingCombatant`: 전투원 핑
- `COMBAT.WarnNonVisibleToken`: 이 전투원은 당신에게 보이지 않습니다.
- `COMBAT.ToggleVis`: 숨기기/보이기 전환
- `COMBAT.ToggleDead`: 쓰러짐으로 표시
- `COMBAT.UnknownCombatant`: 미지의 전투원
- `COMBAT.CombatantActor`: 연결된 액터
- `COMBAT.CombatantCreate`: 전투원 생성
- `COMBAT.CombatantDefeated`: 쓰러짐
- `COMBAT.CombatantHidden`: 숨겨짐
- `COMBAT.CombatantImage`: 섬네일 이미지
- `COMBAT.CombatantInitiative`: 우선권 값
- `COMBAT.CombatantStatus`: 전투원 상태
- `COMBAT.CombatantUpdate`: 전투원 업데이트
- `COMBAT.CombatantUpdateNamed`: 전투원 업데이트: {name}
- `COMBAT.CombatantName`: 표시된 이름
- `COMBAT.CombatantRemove`: 전투원 제거
- `COMBAT.CombatantClear`: 우선권 초기화
- `COMBAT.CombatantReroll`: 우선권 재굴림
- `COMBAT.CombatantClearMovementHistory`: 이동 기록 지우기
- `COMBAT.CombatantMovementHistoryCleared`: 토큰 "{name}"의 이동 기록을 지웠습니다.
- `COMBAT.CombatantToken`: 연결된 토큰
- `COMBAT.CombatantScene`: 전투원 장면
- `COMBAT.CombatantNotInScene`: 현재 장면에 {name} 전투원이 없습니다.
- `COMBAT.DURATION.ROUNDS.one`: 라운드
- `COMBAT.DURATION.ROUNDS.two`: 라운드
- `COMBAT.DURATION.ROUNDS.few`: 라운드
- `COMBAT.DURATION.ROUNDS.many`: 라운드
- `COMBAT.DURATION.ROUNDS.other`: 라운드
- `COMBAT.DURATION.TURNS.one`: 차례
- `COMBAT.DURATION.TURNS.two`: 차례
- `COMBAT.DURATION.TURNS.few`: 차례
- `COMBAT.DURATION.TURNS.many`: 차례
- `COMBAT.DURATION.TURNS.other`: 차례
- `COMBAT.DURATION.None`: 없음
- `COMBAT.PingInvisibleToken`: 당신은 이 전투원의 토큰을 볼 수 없습니다.
- `COMBAT.ResourceHint`: 각 전투원마다 추적할 속성을 선택합니다.
- `COMBAT.SkipDefeatedHint`: 쓰러진 전투원을 자동으로 건너뛰시겠습니까?
- `COMBAT.TargetedBy`: {list}에게 지정됨
- `COMBAT.ToggleTargeting`: 지정 전환
- `COMPENDIUM.ToggleLocked.Option`: 편집 잠금 전환
- `CONTROLS.GroupMeasure`: 측정 제어
- `CONTROLS.MeasureType`: 템플릿 유형
- `CONTROLS.MeasureConfigHint`: 측정 템플릿의 배치 및 표시를 구성합니다.
- `CONTROLS.MeasureCircle`: 원 템플릿
- `CONTROLS.MeasureCone`: 콘 템플릿
- `CONTROLS.MeasureRect`: 직사각형 템플릿
- `CONTROLS.MeasureRay`: 레이 템플릿
- `CONTROLS.MeasureClear`: 템플릿 지우기
- `CONTROLS.TileForeground`: 전경 레이어
- `CONTROLS.WallChain`: 체인 월 생성
- `DOCUMENT.MeasuredTemplate`: 측정 템플릿
- `DOCUMENT.MeasuredTemplates`: 측정 템플릿
- `DRAWING.SubmitCreate`: 그림 생성
- `DRAWING.SubmitUpdate`: 그림 업데이트
- `DRAWING.SubmitReset`: 기본값 초기화
- `DRAWING.Rotation`: 회전
- `DRAWING.LineWidth`: 선 폭
- `DRAWING.StrokeColor`: 외곽선 색상
- `DRAWING.LineOpacity`: 선 불투명도
- `DRAWING.SmoothingFactor`: 매끄러움 보정도
- `DRAWING.SmoothingFactorHint`: 매끄러움 보정도는 자유형 그리기의 곡률을 조절합니다.
- `DRAWING.FillTypes`: 채우기 유형
- `DRAWING.FillTypeNone`: 없음
- `DRAWING.FillTypeSolid`: 단색
- `DRAWING.FillTypePattern`: 패턴
- `DRAWING.FillColor`: 채우기 색상
- `DRAWING.FillOpacity`: 채우기 불투명도
- `DRAWING.FillTexture`: 채우기 텍스처
- `DRAWING.TextLabel`: 텍스트 제목
- `DRAWING.FontFamily`: 글꼴
- `DRAWING.FontSize`: 글자 크기
- `DRAWING.TextColor`: 글자 색상
- `DRAWING.TextOpacity`: 글자 불투명도
- `DRAWING.Role`: 그리기 역할
- `DRAWING.RoleHint`: "오브젝트" 그리기는 캔버스 그룹으로 묶여서 빛이나 전장의 안개 탐색도에 의해 가려질 수 있습니다. "정보" 그리기는 인터페이스 그룹으로 …
- `EFFECT.MODE_CUSTOM`: 커스텀
- `EFFECT.MODE_MULTIPLY`: 곱하기
- `EFFECT.MODE_ADD`: 추가
- `EFFECT.MODE_DOWNGRADE`: 다운그레이드
- `EFFECT.MODE_UPGRADE`: 업그레이드
- `EFFECT.MODE_OVERRIDE`: 덮어쓰기
- `EFFECT.TransferLegacy`: 액터에 이펙트를 옮기기
- `EFFECT.TransferHintLegacy`: 활성화 시, 이 이펙트의 부모 아이템이 액터에 생성될 때 이 이펙트도 같이 복사됩니다. 부모 아이템이 삭제되면 이펙트도 같이 삭제됩니다.
- `EFFECT.DurationTurns`: 효과 지속시간 (턴)
- `EFFECT.StartTurns`: 효과 시작 턴
- `EFFECT.ChangeKey`: 어트리뷰트 키
- `EFFECT.ChangeMode`: 모드 변경
- `EFFECT.ChangeValue`: 효과값
- `EFFECT.ChangePriority`: 우선순위
- `EFFECT.FIELDS.duration.seconds.label`: 효과 지속 시간 (초)
- `EFFECT.FIELDS.duration.rounds.label`: 지속 라운드
- `EFFECT.FIELDS.duration.turns.label`: 지속 턴
- `EFFECT.FIELDS.duration.startTime.label`: 효과 시작 시각
- `EFFECT.FIELDS.duration.startRound.label`: 시작 라운드
- `EFFECT.FIELDS.duration.startTurn.label`: 시작 턴
- `EFFECT.FIELDS.duration.combat.label`: 연결된 전투 인카운터
- `EDITOR.Font`: 폰트
- `EDITOR.TinyMCE`: TinyMCE

</details>

## 미번역 537개 → `python tools/l10n.py export`
