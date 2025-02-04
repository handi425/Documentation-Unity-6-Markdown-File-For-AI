[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/occlusion-culling-dynamic-gameobjects.html)
  * [中文](/cn/current/Manual/occlusion-culling-dynamic-gameobjects.html)
  * [日本語](/ja/current/Manual/occlusion-culling-dynamic-gameobjects.html)
  * [한국어](/kr/current/Manual/occlusion-culling-dynamic-gameobjects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/occlusion-culling-dynamic-gameobjects.html)
  * [中文](/cn/current/Manual/occlusion-culling-dynamic-gameobjects.html)
  * [日本語](/ja/current/Manual/occlusion-culling-dynamic-gameobjects.html)
  * [한국어](/kr/current/Manual/occlusion-culling-dynamic-gameobjects.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
  * Cull moving GameObjects

[](occlusion-culling-scene-loading.html)

Set up multiple scenes for occlusion culling

[](class-OcclusionArea.html)

Create high-precision occlusion areas

# Cull moving GameObjects

GameObjects can be [static](StaticObjects.html), or dynamic (not static).
Static **GameObjects** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and dynamic GameObjects behave
differently in Unity’s **occlusion culling** A process that disables rendering
GameObjects that are hidden (occluded) from the view of the camera. [More
info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) system:

  * Unity can bake static GameObjects into the occlusion culling data as a Static Occluder and/or a Static Occludee.
  * Unity cannot bake dynamic GameObjects into the occlusion culling data. A dynamic GameObject can be an occludee at runtime, but it cannot be an occluder.

To determine whether a dynamic GameObject acts as a occludee, you can set the
Dynamic Occlusion property on any type of Renderer component. When Dynamic
Occlusion is enabled, Unity culls the Renderer when a Static Occluder blocks
it from a **Camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s view. When Dynamic Occlusion is
disabled, Unity does not cull the Renderer when a Static Occluder blocks it
from a Camera’s view.

Dynamic Occlusion is enabled by default. You might want to disable Dynamic
Occlusion to achieve specific effects, such as drawing an outline around a
character who is behind a wall.

If you are certain that Unity should never apply occlusion culling to a
particular GameObject, you can disable Dynamic Occlusion to save on runtime
calculations and reduce CPU usage. The per-GameObject impact of these
calculations is very small, but at sufficient scale this might benefit
performance.

[](occlusion-culling-scene-loading.html)

Set up multiple scenes for occlusion culling

[](class-OcclusionArea.html)

Create high-precision occlusion areas

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

