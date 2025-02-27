[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ClassIDReference.html)
  * [中文](/cn/current/Manual/ClassIDReference.html)
  * [日本語](/ja/current/Manual/ClassIDReference.html)
  * [한국어](/kr/current/Manual/ClassIDReference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ClassIDReference.html)
  * [中文](/cn/current/Manual/ClassIDReference.html)
  * [日本語](/ja/current/Manual/ClassIDReference.html)
  * [한국어](/kr/current/Manual/ClassIDReference.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Text-Based Scene Files](TextSceneFormat.html)
  * YAML Class ID Reference

[](YAMLSceneExample.html)

An Example of a YAML Scene File

[](TroubleShootingEditor.html)

Troubleshoot the Editor

# YAML Class ID Reference

A reference of common class ID numbers used by the YAML file format is given
below, both in numerical order of class IDs and alphabetical order of class
names. Note that some ranges of numbers are intentionally omitted from the
sequence - these may represent classes that have been removed from the API or
may be reserved for future use. Classes defined from **scripts** A piece of
code that allows you to create your own Components, trigger game events,
modify Component properties over time and respond to user input in any way you
like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) will always have class ID 114
(MonoBehaviour).

  * Numerical order
  * Alphabetical order
  * Unused IDs

## Classes ordered by ID number

ID | Class  
---|---  
**0** | Object  
**1** | **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)  
**2** | Component  
**3** | LevelGameManager  
**4** | Transform  
**5** | TimeManager  
**6** | GlobalGameManager  
**8** | Behaviour  
**9** | GameManager  
**11** | AudioManager  
**13** | InputManager  
**18** | EditorExtension  
**19** | Physics2DSettings  
**20** | **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)  
**21** | Material  
**23** | MeshRenderer  
**25** | Renderer  
**27** | Texture  
**28** | Texture2D  
**29** | OcclusionCullingSettings  
**30** | GraphicsSettings  
**33** | MeshFilter  
**41** | OcclusionPortal  
**43** | **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh)  
**45** | **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox)  
**47** | QualitySettings  
**48** | **Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader)  
**49** | TextAsset  
**50** | Rigidbody2D  
**53** | Collider2D  
**54** | **Rigidbody** A component that allows a GameObject to be affected by simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody)  
**55** | PhysicsManager  
**56** | **Collider** An invisible shape that is used to handle physical collisions for an object. A collider doesn’t need to be exactly the same shape as the object’s mesh - a rough approximation is often more efficient and indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider)  
**57** | **Joint** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint)  
**58** | CircleCollider2D  
**59** | HingeJoint  
**60** | PolygonCollider2D  
**61** | BoxCollider2D  
**62** | PhysicsMaterial2D  
**64** | MeshCollider  
**65** | BoxCollider  
**66** | CompositeCollider2D  
**68** | EdgeCollider2D  
**70** | CapsuleCollider2D  
**72** | ComputeShader  
**74** | AnimationClip  
**75** | ConstantForce  
**78** | TagManager  
**81** | AudioListener  
**82** | AudioSource  
**83** | AudioClip  
**84** | RenderTexture  
**86** | CustomRenderTexture  
**89** | **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap)  
**90** | **Avatar** An interface for retargeting animation from one rig to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar)  
**91** | AnimatorController  
**93** | RuntimeAnimatorController  
**94** | ShaderNameRegistry  
**95** | Animator  
**96** | TrailRenderer  
**98** | DelayedCallManager  
**102** | TextMesh  
**104** | RenderSettings  
**108** | Light  
**109** | ShaderInclude  
**110** | BaseAnimationTrack  
**111** | Animation  
**114** | MonoBehaviour  
**115** | MonoScript  
**116** | MonoManager  
**117** | Texture3D  
**118** | NewAnimationTrack  
**119** | Projector  
**120** | LineRenderer  
**121** | Flare  
**122** | Halo  
**123** | LensFlare  
**124** | FlareLayer  
**126** | NavMeshProjectSettings  
**128** | Font  
**129** | PlayerSettings  
**130** | NamedObject  
**134** | PhysicsMaterial  
**135** | SphereCollider  
**136** | CapsuleCollider  
**137** | SkinnedMeshRenderer  
**138** | FixedJoint  
**141** | BuildSettings  
**142** | AssetBundle  
**143** | CharacterController  
**144** | CharacterJoint  
**145** | SpringJoint  
**146** | WheelCollider  
**147** | ResourceManager  
**150** | PreloadData  
**152** | MovieTexture  
**153** | ConfigurableJoint  
**154** | TerrainCollider  
**156** | TerrainData  
**157** | LightmapSettings  
**158** | WebCamTexture  
**159** | EditorSettings  
**162** | EditorUserSettings  
**164** | AudioReverbFilter  
**165** | AudioHighPassFilter  
**166** | AudioChorusFilter  
**167** | AudioReverbZone  
**168** | AudioEchoFilter  
**169** | AudioLowPassFilter  
**170** | AudioDistortionFilter  
**171** | SparseTexture  
**180** | AudioBehaviour  
**181** | AudioFilter  
**182** | WindZone  
**183** | Cloth  
**184** | SubstanceArchive  
**185** | ProceduralMaterial  
**186** | ProceduralTexture  
**187** | Texture2DArray  
**188** | CubemapArray  
**191** | OffMeshLink  
**192** | OcclusionArea  
**193** | Tree  
**195** | NavMeshAgent  
**196** | NavMeshSettings  
**198** | ParticleSystem  
**199** | ParticleSystemRenderer  
**200** | ShaderVariantCollection  
**205** | LODGroup  
**206** | BlendTree  
**207** | Motion  
**208** | NavMeshObstacle  
**210** | SortingGroup  
**212** | SpriteRenderer  
**213** | **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite)  
**214** | CachedSpriteAtlas  
**215** | ReflectionProbe  
**218** | **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain)  
**220** | LightProbeGroup  
**221** | AnimatorOverrideController  
**222** | CanvasRenderer  
**223** | Canvas  
**224** | RectTransform  
**225** | CanvasGroup  
**226** | BillboardAsset  
**227** | BillboardRenderer  
**228** | SpeedTreeWindAsset  
**229** | AnchoredJoint2D  
**230** | Joint2D  
**231** | SpringJoint2D  
**232** | DistanceJoint2D  
**233** | HingeJoint2D  
**234** | SliderJoint2D  
**235** | WheelJoint2D  
**236** | ClusterInputManager  
**237** | BaseVideoTexture  
**238** | NavMeshData  
**240** | AudioMixer  
**241** | AudioMixerController  
**243** | AudioMixerGroupController  
**244** | AudioMixerEffectController  
**245** | AudioMixerSnapshotController  
**246** | PhysicsUpdateBehaviour2D  
**247** | ConstantForce2D  
**248** | Effector2D  
**249** | AreaEffector2D  
**250** | PointEffector2D  
**251** | PlatformEffector2D  
**252** | SurfaceEffector2D  
**253** | BuoyancyEffector2D  
**254** | RelativeJoint2D  
**255** | FixedJoint2D  
**256** | FrictionJoint2D  
**257** | TargetJoint2D  
**258** | LightProbes  
**259** | LightProbeProxyVolume  
**271** | SampleClip  
**272** | AudioMixerSnapshot  
**273** | AudioMixerGroup  
**290** | AssetBundleManifest  
**300** | RuntimeInitializeOnLoadManager  
**310** | UnityConnectSettings  
**319** | AvatarMask  
**320** | PlayableDirector  
**328** | VideoPlayer  
**329** | VideoClip  
**330** | ParticleSystemForceField  
**331** | SpriteMask  
**363** | OcclusionCullingData  
**1001** | PrefabInstance  
**1002** | EditorExtensionImpl  
**1003** | AssetImporter  
**1005** | Mesh3DSImporter  
**1006** | TextureImporter  
**1007** | ShaderImporter  
**1008** | ComputeShaderImporter  
**1020** | AudioImporter  
**1026** | HierarchyState  
**1028** | AssetMetaData  
**1029** | DefaultAsset  
**1030** | DefaultImporter  
**1031** | TextScriptImporter  
**1032** | SceneAsset  
**1034** | NativeFormatImporter  
**1035** | MonoImporter  
**1038** | LibraryAssetImporter  
**1040** | ModelImporter  
**1041** | FBXImporter  
**1042** | TrueTypeFontImporter  
**1045** | EditorBuildSettings  
**1048** | InspectorExpandedState  
**1049** | AnnotationManager  
**1050** | PluginImporter  
**1051** | EditorUserBuildSettings  
**1055** | IHVImageFormatImporter  
**1101** | AnimatorStateTransition  
**1102** | AnimatorState  
**1105** | HumanTemplate  
**1107** | AnimatorStateMachine  
**1108** | PreviewAnimationClip  
**1109** | AnimatorTransition  
**1110** | SpeedTreeImporter  
**1111** | AnimatorTransitionBase  
**1112** | SubstanceImporter  
**1113** | LightmapParameters  
**1120** | LightingDataAsset  
**1124** | SketchUpImporter  
**1125** | BuildReport  
**1126** | PackedAssets  
**1127** | VideoClipImporter  
**100000** | int  
**100001** | bool  
**100002** | float  
**100003** | MonoObject  
**100004** | **Collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision)  
**100005** | Vector3f  
**100006** | RootMotionData  
**100007** | Collision2D  
**100008** | AudioMixerLiveUpdateFloat  
**100009** | AudioMixerLiveUpdateBool  
**100010** | Polygon2D  
**100011** | void  
**19719996** | TilemapCollider2D  
**41386430** | ImportLog  
**55640938** | GraphicsStateCollection  
**73398921** | VFXRenderer  
**156049354** | Grid  
**156483287** | ScenesUsingAssets  
**171741748** | ArticulationBody  
**181963792** | Preset  
**285090594** | IConstraint  
**294290339** | AssemblyDefinitionReferenceImporter  
**355983997** | AudioResource  
**369655926** | AssetImportInProgressProxy  
**382020655** | PluginBuildInfo  
**387306366** | MemorySettings  
**403037116** | BuildMetaDataImporter  
**403037117** | BuildInstructionImporter  
**426301858** | EditorProjectAccess  
**468431735** | PrefabImporter  
**483693784** | TilemapRenderer  
**612988286** | SpriteAtlasAsset  
**638013454** | SpriteAtlasDatabase  
**641289076** | AudioBuildInfo  
**644342135** | CachedSpriteAtlasRuntimeData  
**655991488** | MultiplayerManager  
**662584278** | AssemblyDefinitionReferenceAsset  
**668709126** | BuiltAssetBundleInfoSet  
**687078895** | SpriteAtlas  
**747330370** | RayTracingShaderImporter  
**780535461** | BuildArchiveImporter  
**815301076** | PreviewImporter  
**825902497** | RayTracingShader  
**850595691** | LightingSettings  
**877146078** | PlatformModuleSetup  
**890905787** | VersionControlSettings  
**893571522** | CustomCollider2D  
**895512359** | AimConstraint  
**937362698** | VFXManager  
**947337230** | RoslynAnalyzerConfigAsset  
**954905827** | RuleSetFileAsset  
**994735392** | VisualEffectSubgraph  
**994735403** | VisualEffectSubgraphOperator  
**994735404** | VisualEffectSubgraphBlock  
**1001480554** | **Prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab)  
**1027052791** | LocalizationImporter  
**1114811875** | ReferencesArtifactGenerator  
**1152215463** | AssemblyDefinitionAsset  
**1154873562** | SceneVisibilityState  
**1183024399** | LookAtConstraint  
**1210832254** | SpriteAtlasImporter  
**1233149941** | AudioContainerElement  
**1268269756** | GameObjectRecorder  
**1307931743** | AudioRandomContainer  
**1325145578** | LightingDataAssetParent  
**1386491679** | PresetManager  
**1403656975** | StreamingManager  
**1480428607** | LowerResBlitTexture  
**1521398425** | VideoBuildInfo  
**1541671625** | C4DImporter  
**1542919678** | StreamingController  
**1557264870** | ShaderContainer  
**1597193336** | RoslynAdditionalFileAsset  
**1642787288** | RoslynAdditionalFileImporter  
**1652712579** | MultiplayerRolesData  
**1660057539** | SceneRoots  
**1731078267** | BrokenPrefabAsset  
**1736697216** | AndroidAssetPackImporter  
**1742807556** | GridLayout  
**1766753193** | AssemblyDefinitionImporter  
**1773428102** | ParentConstraint  
**1777034230** | RuleSetFileImporter  
**1818360608** | PositionConstraint  
**1818360609** | RotationConstraint  
**1818360610** | ScaleConstraint  
**1839735485** | **Tilemap** A GameObject that allows you to quickly create 2D levels using tiles and a grid overlay. [More info](tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](Glossary.html#Tilemap)  
**1896753125** | PackageManifest  
**1896753126** | PackageManifestImporter  
**1903396204** | RoslynAnalyzerConfigImporter  
**1931382933** | UIRenderer  
**1953259897** | TerrainLayer  
**1971053207** | SpriteShapeRenderer  
**2058629509** | VisualEffectAsset  
**2058629510** | VisualEffectImporter  
**2058629511** | VisualEffectResource  
**2059678085** | VisualEffectObject  
**2083052967** | VisualEffect  
**2083778819** | LocalizationAsset  
**2089858483** | ScriptedImporter  
**2103361453** | ShaderIncludeImporter  
  
## Classes ordered alphabetically

ID | Class  
---|---  
**AimConstraint** | 895512359  
**AnchoredJoint2D** | 229  
**AndroidAssetPackImporter** | 1736697216  
**Animation** | 111  
**AnimationClip** | 74  
**Animator** | 95  
**AnimatorController** | 91  
**AnimatorOverrideController** | 221  
**AnimatorState** | 1102  
**AnimatorStateMachine** | 1107  
**AnimatorStateTransition** | 1101  
**AnimatorTransition** | 1109  
**AnimatorTransitionBase** | 1111  
**AnnotationManager** | 1049  
**AreaEffector2D** | 249  
**ArticulationBody** | 171741748  
**AssemblyDefinitionAsset** | 1152215463  
**AssemblyDefinitionImporter** | 1766753193  
**AssemblyDefinitionReferenceAsset** | 662584278  
**AssemblyDefinitionReferenceImporter** | 294290339  
**AssetBundle** | 142  
**AssetBundleManifest** | 290  
**AssetImporter** | 1003  
**AssetImportInProgressProxy** | 369655926  
**AssetMetaData** | 1028  
**AudioBehaviour** | 180  
**AudioBuildInfo** | 641289076  
**AudioChorusFilter** | 166  
**AudioClip** | 83  
**AudioContainerElement** | 1233149941  
**AudioDistortionFilter** | 170  
**AudioEchoFilter** | 168  
**AudioFilter** | 181  
**AudioHighPassFilter** | 165  
**AudioImporter** | 1020  
**AudioListener** | 81  
**AudioLowPassFilter** | 169  
**AudioManager** | 11  
**AudioMixer** | 240  
**AudioMixerController** | 241  
**AudioMixerEffectController** | 244  
**AudioMixerGroup** | 273  
**AudioMixerGroupController** | 243  
**AudioMixerLiveUpdateBool** | 100009  
**AudioMixerLiveUpdateFloat** | 100008  
**AudioMixerSnapshot** | 272  
**AudioMixerSnapshotController** | 245  
**AudioRandomContainer** | 1307931743  
**AudioResource** | 355983997  
**AudioReverbFilter** | 164  
**AudioReverbZone** | 167  
**AudioSource** | 82  
**Avatar** | 90  
**AvatarMask** | 319  
**BaseAnimationTrack** | 110  
**BaseVideoTexture** | 237  
**Behaviour** | 8  
**BillboardAsset** | 226  
**BillboardRenderer** | 227  
**BlendTree** | 206  
**bool** | 100001  
**BoxCollider** | 65  
**BoxCollider2D** | 61  
**BrokenPrefabAsset** | 1731078267  
**BuildArchiveImporter** | 780535461  
**BuildInstructionImporter** | 403037117  
**BuildMetaDataImporter** | 403037116  
**BuildReport** | 1125  
**BuildSettings** | 141  
**BuiltAssetBundleInfoSet** | 668709126  
**BuoyancyEffector2D** | 253  
**C4DImporter** | 1541671625  
**CachedSpriteAtlas** | 214  
**CachedSpriteAtlasRuntimeData** | 644342135  
**Camera** | 20  
**Canvas** | 223  
**CanvasGroup** | 225  
**CanvasRenderer** | 222  
**CapsuleCollider** | 136  
**CapsuleCollider2D** | 70  
**CharacterController** | 143  
**CharacterJoint** | 144  
**CircleCollider2D** | 58  
**Cloth** | 183  
**ClusterInputManager** | 236  
**Collider** | 56  
**Collider2D** | 53  
**Collision** | 100004  
**Collision2D** | 100007  
**Component** | 2  
**CompositeCollider2D** | 66  
**ComputeShader** | 72  
**ComputeShaderImporter** | 1008  
**ConfigurableJoint** | 153  
**ConstantForce** | 75  
**ConstantForce2D** | 247  
**Cubemap** | 89  
**CubemapArray** | 188  
**CustomCollider2D** | 893571522  
**CustomRenderTexture** | 86  
**DefaultAsset** | 1029  
**DefaultImporter** | 1030  
**DelayedCallManager** | 98  
**DistanceJoint2D** | 232  
**EdgeCollider2D** | 68  
**EditorBuildSettings** | 1045  
**EditorExtension** | 18  
**EditorExtensionImpl** | 1002  
**EditorProjectAccess** | 426301858  
**EditorSettings** | 159  
**EditorUserBuildSettings** | 1051  
**EditorUserSettings** | 162  
**Effector2D** | 248  
**FBXImporter** | 1041  
**FixedJoint** | 138  
**FixedJoint2D** | 255  
**Flare** | 121  
**FlareLayer** | 124  
**float** | 100002  
**Font** | 128  
**FrictionJoint2D** | 256  
**GameManager** | 9  
**GameObject** | 1  
**GameObjectRecorder** | 1268269756  
**GlobalGameManager** | 6  
**GraphicsSettings** | 30  
**GraphicsStateCollection** | 55640938  
**Grid** | 156049354  
**GridLayout** | 1742807556  
**Halo** | 122  
**HierarchyState** | 1026  
**HingeJoint** | 59  
**HingeJoint2D** | 233  
**HumanTemplate** | 1105  
**IConstraint** | 285090594  
**IHVImageFormatImporter** | 1055  
**ImportLog** | 41386430  
**InputManager** | 13  
**InspectorExpandedState** | 1048  
**int** | 100000  
**Joint** | 57  
**Joint2D** | 230  
**LensFlare** | 123  
**LevelGameManager** | 3  
**LibraryAssetImporter** | 1038  
**Light** | 108  
**LightingDataAsset** | 1120  
**LightingDataAssetParent** | 1325145578  
**LightingSettings** | 850595691  
**LightmapParameters** | 1113  
**LightmapSettings** | 157  
**LightProbeGroup** | 220  
**LightProbeProxyVolume** | 259  
**LightProbes** | 258  
**LineRenderer** | 120  
**LocalizationAsset** | 2083778819  
**LocalizationImporter** | 1027052791  
**LODGroup** | 205  
**LookAtConstraint** | 1183024399  
**LowerResBlitTexture** | 1480428607  
**Material** | 21  
**MemorySettings** | 387306366  
**Mesh** | 43  
**Mesh3DSImporter** | 1005  
**MeshCollider** | 64  
**MeshFilter** | 33  
**MeshRenderer** | 23  
**ModelImporter** | 1040  
**MonoBehaviour** | 114  
**MonoImporter** | 1035  
**MonoManager** | 116  
**MonoObject** | 100003  
**MonoScript** | 115  
**Motion** | 207  
**MovieTexture** | 152  
**MultiplayerManager** | 655991488  
**MultiplayerRolesData** | 1652712579  
**NamedObject** | 130  
**NativeFormatImporter** | 1034  
**NavMeshAgent** | 195  
**NavMeshData** | 238  
**NavMeshObstacle** | 208  
**NavMeshProjectSettings** | 126  
**NavMeshSettings** | 196  
**NewAnimationTrack** | 118  
**Object** | 0  
**OcclusionArea** | 192  
**OcclusionCullingData** | 363  
**OcclusionCullingSettings** | 29  
**OcclusionPortal** | 41  
**OffMeshLink** | 191  
**PackageManifest** | 1896753125  
**PackageManifestImporter** | 1896753126  
**PackedAssets** | 1126  
**ParentConstraint** | 1773428102  
**ParticleSystem** | 198  
**ParticleSystemForceField** | 330  
**ParticleSystemRenderer** | 199  
**Physics2DSettings** | 19  
**PhysicsManager** | 55  
**PhysicsMaterial** | 134  
**PhysicsMaterial2D** | 62  
**PhysicsUpdateBehaviour2D** | 246  
**PlatformEffector2D** | 251  
**PlatformModuleSetup** | 877146078  
**PlayableDirector** | 320  
**PlayerSettings** | 129  
**PluginBuildInfo** | 382020655  
**PluginImporter** | 1050  
**PointEffector2D** | 250  
**Polygon2D** | 100010  
**PolygonCollider2D** | 60  
**PositionConstraint** | 1818360608  
**Prefab** | 1001480554  
**PrefabImporter** | 468431735  
**PrefabInstance** | 1001  
**PreloadData** | 150  
**Preset** | 181963792  
**PresetManager** | 1386491679  
**PreviewAnimationClip** | 1108  
**PreviewImporter** | 815301076  
**ProceduralMaterial** | 185  
**ProceduralTexture** | 186  
**Projector** | 119  
**QualitySettings** | 47  
**RayTracingShader** | 825902497  
**RayTracingShaderImporter** | 747330370  
**RectTransform** | 224  
**ReferencesArtifactGenerator** | 1114811875  
**ReflectionProbe** | 215  
**RelativeJoint2D** | 254  
**Renderer** | 25  
**RenderSettings** | 104  
**RenderTexture** | 84  
**ResourceManager** | 147  
**Rigidbody** | 54  
**Rigidbody2D** | 50  
**RootMotionData** | 100006  
**RoslynAdditionalFileAsset** | 1597193336  
**RoslynAdditionalFileImporter** | 1642787288  
**RoslynAnalyzerConfigAsset** | 947337230  
**RoslynAnalyzerConfigImporter** | 1903396204  
**RotationConstraint** | 1818360609  
**RuleSetFileAsset** | 954905827  
**RuleSetFileImporter** | 1777034230  
**RuntimeAnimatorController** | 93  
**RuntimeInitializeOnLoadManager** | 300  
**SampleClip** | 271  
**ScaleConstraint** | 1818360610  
**SceneAsset** | 1032  
**SceneRoots** | 1660057539  
**ScenesUsingAssets** | 156483287  
**SceneVisibilityState** | 1154873562  
**ScriptedImporter** | 2089858483  
**Shader** | 48  
**ShaderContainer** | 1557264870  
**ShaderImporter** | 1007  
**ShaderInclude** | 109  
**ShaderIncludeImporter** | 2103361453  
**ShaderNameRegistry** | 94  
**ShaderVariantCollection** | 200  
**SketchUpImporter** | 1124  
**SkinnedMeshRenderer** | 137  
**Skybox** | 45  
**SliderJoint2D** | 234  
**SortingGroup** | 210  
**SparseTexture** | 171  
**SpeedTreeImporter** | 1110  
**SpeedTreeWindAsset** | 228  
**SphereCollider** | 135  
**SpringJoint** | 145  
**SpringJoint2D** | 231  
**Sprite** | 213  
**SpriteAtlas** | 687078895  
**SpriteAtlasAsset** | 612988286  
**SpriteAtlasDatabase** | 638013454  
**SpriteAtlasImporter** | 1210832254  
**SpriteMask** | 331  
**SpriteRenderer** | 212  
**SpriteShapeRenderer** | 1971053207  
**StreamingController** | 1542919678  
**StreamingManager** | 1403656975  
**SubstanceArchive** | 184  
**SubstanceImporter** | 1112  
**SurfaceEffector2D** | 252  
**TagManager** | 78  
**TargetJoint2D** | 257  
**Terrain** | 218  
**TerrainCollider** | 154  
**TerrainData** | 156  
**TerrainLayer** | 1953259897  
**TextAsset** | 49  
**TextMesh** | 102  
**TextScriptImporter** | 1031  
**Texture** | 27  
**Texture2D** | 28  
**Texture2DArray** | 187  
**Texture3D** | 117  
**TextureImporter** | 1006  
**Tilemap** | 1839735485  
**TilemapCollider2D** | 19719996  
**TilemapRenderer** | 483693784  
**TimeManager** | 5  
**TrailRenderer** | 96  
**Transform** | 4  
**Tree** | 193  
**TrueTypeFontImporter** | 1042  
**UIRenderer** | 1931382933  
**UnityConnectSettings** | 310  
**Vector3f** | 100005  
**VersionControlSettings** | 890905787  
**VFXManager** | 937362698  
**VFXRenderer** | 73398921  
**VideoBuildInfo** | 1521398425  
**VideoClip** | 329  
**VideoClipImporter** | 1127  
**VideoPlayer** | 328  
**VisualEffect** | 2083052967  
**VisualEffectAsset** | 2058629509  
**VisualEffectImporter** | 2058629510  
**VisualEffectObject** | 2059678085  
**VisualEffectResource** | 2058629511  
**VisualEffectSubgraph** | 994735392  
**VisualEffectSubgraphBlock** | 994735404  
**VisualEffectSubgraphOperator** | 994735403  
**void** | 100011  
**WebCamTexture** | 158  
**WheelCollider** | 146  
**WheelJoint2D** | 235  
**WindZone** | 182  
  
## Unused IDs

Unused IDs: 7, 10, 12, 14 - 17, 22, 24, 26, 31 - 32, 34 - 40, 42, 44, 46, 51 -
52, 63, 67, 69, 71, 73, 76 - 77, 79 - 80, 85, 87 - 88, 92, 97, 99 - 101, 103,
105 - 107, 112 - 113, 125, 127, 131 - 133, 139 - 140, 148 - 149, 151, 155, 160
- 161, 163, 172 - 179, 189 - 190, 194, 197, 201 - 204, 209, 211, 216 - 217,
219, 239, 242, 260 - 270, 274 - 289, 291 - 299, 301 - 309, 311 - 318, 321 -
327, 332 - 362, 364 - 899, 901 - 1000, 1004, 1009 - 1019, 1021 - 1025, 1027,
1033, 1036 - 1037, 1039, 1043 - 1044, 1046 - 1047, 1052 - 1054, 1056 - 1100,
1103 - 1104, 1106, 1114 - 1119, 1121 - 1123, 1128 - 99999, 100012 - 19719995,
19719997 - 41386429, 41386431 - 55640937, 55640939 - 73398920, 73398922 -
156049353, 156049355 - 156483286, 156483288 - 171741747, 171741749 -
181963791, 181963793 - 285090593, 285090595 - 294290338, 294290340 -
355983996, 355983998 - 369655925, 369655927 - 382020654, 382020656 -
387306365, 387306367 - 403037115, 403037118 - 426301857, 426301859 -
468431734, 468431736 - 483693783, 483693785 - 612988285, 612988287 -
638013453, 638013455 - 641289075, 641289077 - 644342134, 644342136 -
655991487, 655991489 - 662584277, 662584279 - 668709125, 668709127 -
687078894, 687078896 - 702665668, 702665670 - 747330369, 747330371 -
780535460, 780535462 - 815301075, 815301077 - 825902496, 825902498 -
850595690, 850595692 - 877146077, 877146079 - 890905786, 890905788 -
893571521, 893571523 - 895512358, 895512360 - 937362697, 937362699 -
947337229, 947337231 - 954905826, 954905828 - 994735391, 994735393 -
994735402, 994735405 - 1001480553, 1001480555 - 1027052790, 1027052792 -
1114811874, 1114811876 - 1152215462, 1152215464 - 1154873561, 1154873563 -
1183024398, 1183024400 - 1210832253, 1210832255 - 1223240403, 1223240405 -
1233149940, 1233149942 - 1268269755, 1268269757 - 1307931742, 1307931744 -
1325145577, 1325145579 - 1386491678, 1386491680 - 1403656974, 1403656976 -
1480428606, 1480428608 - 1521398424, 1521398426 - 1541671624, 1541671626 -
1542919677, 1542919679 - 1557264869, 1557264871 - 1597193335, 1597193337 -
1642787287, 1642787289 - 1652712578, 1652712580 - 1660057538, 1660057540 -
1731078266, 1731078268 - 1736697215, 1736697217 - 1742807555, 1742807557 -
1766753192, 1766753194 - 1773428101, 1773428103 - 1777034229, 1777034231 -
1818360607, 1818360611 - 1839735484, 1839735486 - 1896753124, 1896753127 -
1903396203, 1903396205 - 1931382932, 1931382934 - 1953259896, 1953259898 -
1971053206, 1971053208 - 2058629508, 2058629512 - 2059678084, 2059678086 -
2083052966, 2083052968 - 2083778818, 2083778820 - 2089858482, 2089858484 -
2103361452, 2103361454 - 2147483647

[](YAMLSceneExample.html)

An Example of a YAML Scene File

[](TroubleShootingEditor.html)

Troubleshoot the Editor

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

