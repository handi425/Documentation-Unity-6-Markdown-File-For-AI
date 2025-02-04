[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/configure-with-lightmap-parameters-asset.html)
  * [中文](/cn/current/Manual/configure-with-lightmap-parameters-asset.html)
  * [日本語](/ja/current/Manual/configure-with-lightmap-parameters-asset.html)
  * [한국어](/kr/current/Manual/configure-with-lightmap-parameters-asset.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/configure-with-lightmap-parameters-asset.html)
  * [中文](/cn/current/Manual/configure-with-lightmap-parameters-asset.html)
  * [日本語](/ja/current/Manual/configure-with-lightmap-parameters-asset.html)
  * [한국어](/kr/current/Manual/configure-with-lightmap-parameters-asset.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * Save and load lighting settings with Lightmap Parameters Assets

[](LightProbes-Reference.html)

Light Probes reference

[](Shadows.html)

Shadows

# Save and load lighting settings with Lightmap Parameters Assets

A **Lightmap** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) Parameters Asset contains a set of
values for the parameters that control Unity’s lighting features. These Assets
allow you to define and save different sets of values for lighting, for use in
different situations.

Lightmap Parameters Assets allow you to quickly create presets optimized for
different types of **GameObjects** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), or for different platforms and
different Scene types (for example, indoor or outdoor Scenes).

## Creating a Lightmap Parameters Asset

To create a new Lightmap Parameters Asset, right-click in the Project window
and go to **Create** > **Lightmap Parameters**. Unity stores this in your
Project folder.

## Assigning Lightmap Parameters Assets

### Scenes

To assign a Lightmap Parameters Asset to the whole Scene:

  1. Open the [Lighting window](lighting-window.html) (**Window** > **Rendering** > **Lighting**)
  2. Click the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) tab

  3. Navigate to the **Lightingmapping Settings**.
  4. Use the **Lightmap Parameters** drop-down to assign a default Lightmap Parameters Asset. This drop-down lists all available Lightmap Parameters Assets.

### GameObjects

To assign a Lightmap Parameters Asset to a single GameObject, ensure the
GameObject has a **Mesh** The main graphics primitive of Unity. Meshes make up
a large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer or **Terrain** The landscape in
your scene. A Terrain GameObject adds a large flat plane to your scene and you
can use the Terrain’s Inspector window to create a detailed landscape. [More
info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) component attached.

To assign a Lightmap Parameters Asset to a **Mesh Renderer** A mesh component
that takes the geometry from the Mesh Filter and renders it at the position
defined by the object’s Transform component. [More info](class-
MeshRenderer.html)  
See in [Glossary](Glossary.html#MeshRenderer) component:

  1. In the Inspector, go to **Mesh Renderer** > **Lighting**
  2. Enable **Contribute Global Illumination**
  3. In the mesh Renderer component, go to **Lightmapping** > **Lightmap Parameters**.
  4. Select an option from the menu. Select **Scene Default Parameter** to use the same Lightmap Parameters Asset that’s assigned to the whole Scene.

To assign a Lightmap Parameters Asset to a Terrain component:

  1. In the Inspector, go to **Terrain** > **Terrain Settings** > **Lighting**
  2. Enable **Contribute Global Illumination**
  3. In **Terrain Settings** , go to **Lightmapping** > **Lightmap Parameters**.
  4. Select an option from the menu. Select **Scene Default Parameter** to use the same Lightmap Parameters Asset that’s assigned to the whole Scene.

[](LightProbes-Reference.html)

Light Probes reference

[](Shadows.html)

Shadows

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

