[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/YAMLSceneExample.html)
  * [中文](/cn/current/Manual/YAMLSceneExample.html)
  * [日本語](/ja/current/Manual/YAMLSceneExample.html)
  * [한국어](/kr/current/Manual/YAMLSceneExample.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/YAMLSceneExample.html)
  * [中文](/cn/current/Manual/YAMLSceneExample.html)
  * [日本語](/ja/current/Manual/YAMLSceneExample.html)
  * [한국어](/kr/current/Manual/YAMLSceneExample.html)

  * [The Unity Editor](unity-editor.html)
  * [Editor Features](EditorFeatures.html)
  * [Text-Based Scene Files](TextSceneFormat.html)
  * An Example of a YAML Scene File

[](UnityYAML.html)

UnityYAML

[](ClassIDReference.html)

YAML Class ID Reference

# An Example of a YAML Scene File

An example of a simple but complete **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) is given below. The scene contains just
a **camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) and a cube object. Note that the file
**must** start with the two lines

    
    
    %YAML 1.1
    %TAG !u! tag:unity3d.com,2011:
    
    

…in order to be accepted by Unity. Otherwise, the import process is designed
to be tolerant of omissions - default values will be supplied for missing
property data as far as possible.

    
    
    %YAML 1.1
    %TAG !u! tag:unity3d.com,2011:
    --- !u!header
    SerializedFile:
      m_TargetPlatform: 4294967294
      m_UserInformation: 
    --- !u!29 &1
    Scene:
      m_ObjectHideFlags: 0
      m_PVSData: 
      m_QueryMode: 1
      m_PVSObjectsArray: []
      m_PVSPortalsArray: []
      m_ViewCellSize: 1.000000
    --- !u!104 &2
    RenderSettings:
      m_Fog: 0
      m_FogColor: {r: 0.500000, g: 0.500000, b: 0.500000, a: 1.000000}
      m_FogMode: 3
      m_FogDensity: 0.010000
      m_LinearFogStart: 0.000000
      m_LinearFogEnd: 300.000000
      m_AmbientLight: {r: 0.200000, g: 0.200000, b: 0.200000, a: 1.000000}
      m_SkyboxMaterial: {fileID: 0}
      m_HaloStrength: 0.500000
      m_FlareStrength: 1.000000
      m_HaloTexture: {fileID: 0}
      m_SpotCookie: {fileID: 0}
      m_ObjectHideFlags: 0
    --- !u!127 &3
    GameManager:
      m_ObjectHideFlags: 0
    --- !u!157 &4
    LightmapSettings:
      m_ObjectHideFlags: 0
      m_LightProbeCloud: {fileID: 0}
      m_Lightmaps: []
      m_LightmapsMode: 1
      m_BakedColorSpace: 0
      m_UseDualLightmapsInForward: 0
      m_LightmapEditorSettings:
        m_Resolution: 50.000000
        m_LastUsedResolution: 0.000000
        m_TextureWidth: 1024
        m_TextureHeight: 1024
        m_BounceBoost: 1.000000
        m_BounceIntensity: 1.000000
        m_SkyLightColor: {r: 0.860000, g: 0.930000, b: 1.000000, a: 1.000000}
        m_SkyLightIntensity: 0.000000
        m_Quality: 0
        m_Bounces: 1
        m_FinalGatherRays: 1000
        m_FinalGatherContrastThreshold: 0.050000
        m_FinalGatherGradientThreshold: 0.000000
        m_FinalGatherInterpolationPoints: 15
        m_AOAmount: 0.000000
        m_AOMaxDistance: 0.100000
        m_AOContrast: 1.000000
        m_TextureCompression: 0
        m_LockAtlas: 0
    --- !u!196 &5
    NavMeshSettings:
      m_ObjectHideFlags: 0
      m_BuildSettings:
        cellSize: 0.200000
        cellHeight: 0.100000
        agentSlope: 45.000000
        agentClimb: 0.900000
        ledgeDropHeight: 0.000000
        maxJumpAcrossDistance: 0.000000
        agentRadius: 0.400000
        agentHeight: 1.800000
        maxEdgeLength: 12
        maxSimplificationError: 1.300000
        regionMinSize: 8
        regionMergeSize: 20
        tileSize: 500
        detailSampleDistance: 6.000000
        detailSampleMaxError: 1.000000
        accuratePlacement: 0
      m_NavMesh: {fileID: 0}
    --- !u!1 &6
    GameObject:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      importerVersion: 3
      m_Component:
      - 4: {fileID: 8}
      - 33: {fileID: 12}
      - 65: {fileID: 13}
      - 23: {fileID: 11}
      m_Layer: 0
      m_Name: Cube
      m_TagString: Untagged
      m_Icon: {fileID: 0}
      m_NavMeshLayer: 0
      m_StaticEditorFlags: 0
      m_IsActive: 1
    --- !u!1 &7
    GameObject:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      importerVersion: 3
      m_Component:
      - 4: {fileID: 9}
      - 20: {fileID: 10}
      - 92: {fileID: 15}
      - 124: {fileID: 16}
      - 81: {fileID: 14}
      m_Layer: 0
      m_Name: Main Camera
      m_TagString: MainCamera
      m_Icon: {fileID: 0}
      m_NavMeshLayer: 0
      m_StaticEditorFlags: 0
      m_IsActive: 1
    --- !u!4 &8
    Transform:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 6}
      m_LocalRotation: {x: 0.000000, y: 0.000000, z: 0.000000, w: 1.000000}
      m_LocalPosition: {x: -2.618721, y: 1.028581, z: 1.131627}
      m_LocalScale: {x: 1.000000, y: 1.000000, z: 1.000000}
      m_Children: []
      m_Father: {fileID: 0}
    --- !u!4 &9
    Transform:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 7}
      m_LocalRotation: {x: 0.000000, y: 0.000000, z: 0.000000, w: 1.000000}
      m_LocalPosition: {x: 0.000000, y: 1.000000, z: -10.000000}
      m_LocalScale: {x: 1.000000, y: 1.000000, z: 1.000000}
      m_Children: []
      m_Father: {fileID: 0}
    --- !u!20 &10
    Camera:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 7}
      m_Enabled: 1
      importerVersion: 2
      m_ClearFlags: 1
      m_BackGroundColor: {r: 0.192157, g: 0.301961, b: 0.474510, a: 0.019608}
      m_NormalizedViewPortRect:
        importerVersion: 2
        x: 0.000000
        y: 0.000000
        width: 1.000000
        height: 1.000000
      near clip plane: 0.300000
      far clip plane: 1000.000000
      field of view: 60.000000
      orthographic: 0
      orthographic size: 100.000000
      m_Depth: -1.000000
      m_CullingMask:
        importerVersion: 2
        m_Bits: 4294967295
      m_RenderingPath: -1
      m_TargetTexture: {fileID: 0}
      m_HDR: 0
    --- !u!23 &11
    Renderer:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 6}
      m_Enabled: 1
      m_CastShadows: 1
      m_ReceiveShadows: 1
      m_LightmapIndex: 255
      m_LightmapTilingOffset: {x: 1.000000, y: 1.000000, z: 0.000000, w: 0.000000}
      m_Materials:
      - {fileID: 10302, guid: 0000000000000000e000000000000000, type: 0}
      m_SubsetIndices: 
      m_StaticBatchRoot: {fileID: 0}
      m_LightProbeAnchor: {fileID: 0}
      m_UseLightProbes: 0
      m_ScaleInLightmap: 1.000000
    --- !u!33 &12
    MeshFilter:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 6}
      m_Mesh: {fileID: 10202, guid: 0000000000000000e000000000000000, type: 0}
    --- !u!65 &13
    BoxCollider:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 6}
      m_Material: {fileID: 0}
      m_IsTrigger: 0
      m_Enabled: 1
      importerVersion: 2
      m_Size: {x: 1.000000, y: 1.000000, z: 1.000000}
      m_Center: {x: 0.000000, y: 0.000000, z: 0.000000}
    --- !u!81 &14
    AudioListener:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 7}
      m_Enabled: 1
    --- !u!92 &15
    Behaviour:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 7}
      m_Enabled: 1
    --- !u!124 &16
    Behaviour:
      m_ObjectHideFlags: 0
      m_PrefabParentObject: {fileID: 0}
      m_PrefabInternal: {fileID: 0}
      m_GameObject: {fileID: 7}
      m_Enabled: 1
    --- !u!1026 &17
    HierarchyState:
      m_ObjectHideFlags: 0
      expanded: []
      selection: []
      scrollposition_x: 0.000000
      scrollposition_y: 0.000000
    
    

[](UnityYAML.html)

UnityYAML

[](ClassIDReference.html)

YAML Class ID Reference

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

