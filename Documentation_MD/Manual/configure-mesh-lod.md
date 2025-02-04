[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/configure-mesh-lod.html)
  * [中文](/cn/current/Manual/configure-mesh-lod.html)
  * [日本語](/ja/current/Manual/configure-mesh-lod.html)
  * [한국어](/kr/current/Manual/configure-mesh-lod.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/configure-mesh-lod.html)
  * [中文](/cn/current/Manual/configure-mesh-lod.html)
  * [日本語](/ja/current/Manual/configure-mesh-lod.html)
  * [한국어](/kr/current/Manual/configure-mesh-lod.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Meshes](mesh.html)
  * [Simplifying distant meshes with level of detail (LOD)](simplifying-distant-meshes-with-level-of-detail-lod.html)
  * Configure mesh LOD

[](LevelOfDetail.html)

Mesh LOD

[](importing-lod-meshes.html)

Import a mesh with LOD settings

# Configure mesh LOD

To configure **LOD** The _Level Of Detail_ (LOD) technique is an optimization
that reduces the number of triangles that Unity has to render for a GameObject
when its distance from the Camera increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD), you must have a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with a [LOD Group](class-
LODGroup.html)A component to manage level of detail (LOD) for GameObjects.
[More info](class-LODGroup.html)  
See in [Glossary](Glossary.html#LODGroup) component. The LOD Group component
provides controls to define how LOD behaves on this GameObject, and references
the GameObjects that Unity shows or hides for each LOD level. See [LOD
Group](class-LODGroup.html) for details on the properties in this component.

You can set up LOD in Unity two ways:

  * You can configure LOD levels in your external 3D modeling application, and Unity can automatically create and configure the required GameObjects and components for you. See [Importing LOD Meshes](importing-lod-meshes.html) for details on the correct configuration.
  * You can manually create a GameObject with a LOD Group component, and configure the LOD levels manually.

## Configure LOD levels

To manually configure the distance from the **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) at which Unity displays each LOD
level, use the [LOD Group component’s selection bar](class-
LODGroup.html#LODGroup).

The LOD Group component accepts a maximum of eight LOD levels. **LOD 0** is
the closest to the Camera, and therefore the most detailed LOD level.

## Configure project-wide LOD settings

In the [Quality settings](class-QualitySettings.html) window, you can
configure LOD settings that affect all GameObjects in your Project.

There are two LOD settings you can configure:

  * **Maximum LOD Level** : Exclude meshes above a specified LOD level from your build.
  * **LOD Bias** : Determine whether to favor higher or lower LOD levels at threshold distances.

[](LevelOfDetail.html)

Mesh LOD

[](importing-lod-meshes.html)

Import a mesh with LOD settings

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

