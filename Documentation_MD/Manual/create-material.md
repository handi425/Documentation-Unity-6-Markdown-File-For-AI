[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/create-material.html)
  * [中文](/cn/current/Manual/create-material.html)
  * [日本語](/ja/current/Manual/create-material.html)
  * [한국어](/kr/current/Manual/create-material.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/create-material.html)
  * [中文](/cn/current/Manual/create-material.html)
  * [日本語](/ja/current/Manual/create-material.html)
  * [한국어](/kr/current/Manual/create-material.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Materials](Materials.html)
  * Create and assign a material

[](materials-introduction.html)

Introduction to materials

[](MaterialsAccessingViaScript.html)

Access material properties in a script

# Create and assign a material

  1. To create a new material asset in your project, from the main menu or the Project View context menu, select **Assets** > **Create** > **Material**.
  2. To assign a **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) to the material asset, in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window use the **Shader** drop-down
menu.

## Assign a material asset to a GameObject

To render a **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) using a material:

  1. Add a component that inherits from `Renderer`. [MeshRenderer](class-MeshRenderer.html) is the most common and is suitable for most use cases, but [SkinnedMeshRenderer](class-SkinnedMeshRenderer.html), [LineRenderer](class-LineRenderer.html), or [TrailRenderer](class-TrailRenderer.html) might be more suitable if your GameObject has special requirements.
  2. Assign the material asset to the component’s **Material** property.

To render a **particle system** A component that simulates fluid entities such
as liquids, clouds and flames by generating and animating large numbers of
small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) in the [Built-in Particle
System](PartSysUsage.html) using a material:

  1. Add a [Renderer Module](PartSysRendererModule.html) to the Particle System.
  2. Assign the material asset to the Renderer Module’s **Material** property.

[](materials-introduction.html)

Introduction to materials

[](MaterialsAccessingViaScript.html)

Access material properties in a script

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

