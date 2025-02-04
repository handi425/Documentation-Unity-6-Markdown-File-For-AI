[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/StaticObjects.html)
  * [中文](/cn/current/Manual/StaticObjects.html)
  * [日本語](/ja/current/Manual/StaticObjects.html)
  * [한국어](/kr/current/Manual/StaticObjects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/StaticObjects.html)
  * [中文](/cn/current/Manual/StaticObjects.html)
  * [日本語](/ja/current/Manual/StaticObjects.html)
  * [한국어](/kr/current/Manual/StaticObjects.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [GameObject fundamentals](gameobject-fundamentals.html)
  * Static GameObjects

[](QuaternionAndEulerRotationsInUnity.html)

Rotation and orientation in Unity

[](DeactivatingGameObjects.html)

Deactivate GameObjects

# Static GameObjects

If a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) does not move at runtime, it is
known as a **static GameObject**. If a GameObject moves at runtime, it is
known as a **dynamic GameObject**.

Many systems in Unity can precompute information about static GameObjects in
the Editor. Because the GameObjects do not move, the results of these
calculations are still valid at runtime. This means that Unity can save on
runtime calculations, and potentially improve performance.

## The Static Editor Flags property

![The Static Editor Flags checkbox and drop-down menu, as seen when viewing a
GameObject in the
Inspector](../uploads/Main/GameObjectStaticDropDownMenu1.png) The Static
Editor Flags checkbox and drop-down menu, as seen when viewing a GameObject in
the Inspector

The **Static Editor Flags** property lists a number of Unity systems which can
include a static GameObject in their precomputations. Use the drop-down to
define which systems include the GameObject in their precomputations. Setting
Static Editor Flags at runtime has no effect on these systems.

Only include a GameObject in the precomputations for systems that need to know
about that GameObject. Including a GameObject in the precomputations for a
system that does not need to know about that GameObject can result in wasted
calculations, unnecessarily large data files, or unexpected behavior.

The **Static Editor Flags** property is located in the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) for a GameObject, in the extreme
top-right. It includes a checkbox, which sets the value to **Everything** or
**Nothing** , and a dropdown menu that lets you choose which values to
include.

To set the Static Editor Flags property in code, use the
[GameObjectUtility.SetStaticEditorFlags](../ScriptReference/GameObjectUtility.SetStaticEditorFlags.html)
API and the [GameObject.isStatic](../ScriptReference/GameObject-
isStatic.html). To get the status of the Static Editor Flags property in code,
use the
[GameObjectUtility.GetStaticEditorFlags](../ScriptReference/GameObjectUtility.GetStaticEditorFlags.html)
API.

The following values are available:

**Property** | **Description**  
---|---  
**Nothing** | Do not include the GameObject in precomputations for any systems.  
**Everything** | Include the GameObject in precomputations for all systems below.  
**Contribute GI** | When you enable this property, Unity includes the target [Mesh Renderer](class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](class-MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) in **global illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) calculations. These
calculations take place while precomputing lighting data at bake time. The
ContributeGI property exposes the
[ReceiveGI](../ScriptReference/ReceiveGI.html) property. The ContributeGI
property only takes effect if you enable a global illumination setting such as
[Baked Global Illumination](class-LightingSettings.html#MixedLighting) or
[Enlighten Realtime Global Illumination](class-
LightingSettings.html#RealtimeLighting) for the target **Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). For additional context, refer to [this
tutorial for setting up the Built-in Render Pipeline and lighting](choose-a-
lighting-setup.html) in Unity.  
**Occluder Static** | Mark the GameObject as a Static Occluder in the occlusion culling system. For more information, refer to [the Occlusion Culling system](OcclusionCulling.html).  
**Occludee Static** | Mark the GameObject as a Static Occludee in the occlusion culling system. For more information, refer to [the Occlusion Culling system](OcclusionCulling.html).  
**Batching Static** | Combine the GameObject’s **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) with other eligible Meshes, to
potentially reduce runtime rendering costs. For more information, refer to the
documentation on [Static Batching](DrawCallBatching.html)A technique Unity
uses to draw GameObjects on the screen that combines static (non-moving)
GameObjects into big Meshes, and renders them in a faster way. [More
info](DrawCallBatching.html)  
See in [Glossary](Glossary.html#StaticBatching).  
**Navigation Static** | Include the GameObject when precomputing navigation data. This workflow is deprecated and you cannot set **Navigation Static** here. However, you can still set this option in code with [`StaticEditorFlags.NavigationStatic`](../ScriptReference/StaticEditorFlags.NavigationStatic.html).   
Instead of **Navigation Static** flags, use the [**NavMesh
Modifier**](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavMeshModifier.html)
component together with [**NavMesh
Surfaces**](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavMeshSurface.html).  
**Off Mesh Link Generation** | Attempt to generate an OffMesh Link that starts from this GameObject when precomputing navigation data. This workflow is deprecated and you cannot set **Off Mesh Link Generation** from this menu. However, you can still set this option in code with [`StaticEditorFlags.OffMeshLinkGeneration`](../ScriptReference/StaticEditorFlags.OffMeshLinkGeneration.html).   
Instead of **Off Mesh Link Generation** flags, use the [**NavMesh
Modifier**](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavMeshModifier.html)
component together with [**NavMesh
Surfaces**](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavMeshSurface.html).  
**Reflection Probe** | Include this GameObject when precomputing data for **Reflection Probes** whose **Type** property is set to **Baked**. For more information, refer to [Reflection Probes](ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe).  
  
## Additional resources

  * [GameObjectUtility.SetStaticEditorFlags](../ScriptReference/GameObjectUtility.SetStaticEditorFlags.html)
  * [GameObjectUtility.GetStaticEditorFlags](../ScriptReference/GameObjectUtility.GetStaticEditorFlags.html)
  * [StaticEditorFlags.NavigationStatic](../ScriptReference/StaticEditorFlags.NavigationStatic.html)
  * [StaticEditorFlags.OffMeshLinkGeneration](../ScriptReference/StaticEditorFlags.OffMeshLinkGeneration.html)
  * [StaticEditorFlags](../ScriptReference/StaticEditorFlags.html)
  * [Draw call batching](DrawCallBatching.html)
  * [Occlusion Culling](OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling)

  * [NavMesh Modifier component](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/NavMeshModifier.html)
  * [NavMesh Surface component](https://docs.unity3d.com/Packages/com.unity.ai.navigation@2.0/manual/NavMeshSurface.html)
  * [Reflection Probes](ReflectionProbes.html)

[](QuaternionAndEulerRotationsInUnity.html)

Rotation and orientation in Unity

[](DeactivatingGameObjects.html)

Deactivate GameObjects

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

