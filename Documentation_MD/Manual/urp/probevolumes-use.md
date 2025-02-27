[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-use.html)
  * [中文](/cn/current/Manual/urp/probevolumes-use.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-use.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-use.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-use.html)
  * [中文](/cn/current/Manual/urp/probevolumes-use.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-use.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-use.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Use Adaptive Probe Volumes

[](../urp/probevolumes-concept.html)

Introduction to Adaptive Probe Volumes

[](../urp/probevolumes-showandadjust.html)

Display Adaptive Probe Volumes

# Use Adaptive Probe Volumes

This page provides the basic workflow you need to use Adaptive Probe Volumes
in your project.

## Add and bake an Adaptive Probe Volume

### Enable Adaptive Probe Volumes

  1. From the main menu, select **Edit** > **Project Settings** > **Quality**.
  2. In the **Rendering** section, double-click the active ****Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](../render-pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) Asset** to open it in the
**Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window.

  3. In the **Lighting** section, set ****Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](../LightProbes.html)  
See in [Glossary](../Glossary.html#LightProbe) System** to **Adaptive Probe
Volumes**.

### Add an Adaptive Probe Volume to the Scene

  1. From the main menu, select **GameObject** > **Light** > **Adaptive Probe Volumes** > **Adaptive Probe Volume**.
  2. In the Inspector for the Adaptive Probe Volume, set **Mode** to **Global** to make this Adaptive Probe Volume cover your entire **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene).

### Adjust your Light and Mesh Renderer settings

  1. To include a Light in an Adaptive Probe Volume’s baked lighting data, open the Inspector for the Light then set the ****Light Mode** A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](../LightModes.html)  
See in [Glossary](../Glossary.html#LightMode)** to **Mixed** or **Baked**.

  2. To include a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) in an Adaptive Probe Volume’s
baked lighting data, open the Inspector for the GameObject and enable
**Contribute**Global Illumination** A group of techniques that model both
direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](../Glossary.html#globalillumination)**.

  3. To make a GameObject receive baked lighting, open the Inspector for the GameObject, then in the ****Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](../mesh.html)  
See in [Glossary](../Glossary.html#Mesh) Renderer** component set **Receive
Global Illumination** to **Light Probes**.

### Bake your lighting

  1. From the main menu, select **Window** > **Rendering** > **Lighting**.
  2. Select the **Adaptive Probe Volumes** panel.
  3. Set **Baking Mode** to **Single Scene**.
  4. Select **Generate Lighting**.

If no scene in the Baking Set contains an Adaptive Probe Volume, Unity asks if
you want to create an Adaptive Probe Volume automatically.

You can change baking settings in the Lighting window’s [Lightmapping
Settings](https://docs.unity3d.com/Documentation/Manual/class-
LightingSettings.html#LightmappingSettings).

Refer to [Bake different lighting setups with Baking Sets](probevolumes-
usebakingsets.html) for more information about Baking Sets.

If there are visual artefacts in baked lighting, such as dark blotches or
light leaks, refer to [Fix issues with Adaptive Probe Volumes](probevolumes-
fixissues.html).

## Configure an Adaptive Probe Volume

You can use the following to configure an Adaptive Probe Volume:

  * Use the [Adaptive Probe Volumes panel](probevolumes-lighting-panel-reference.html) in the Lighting window to change the probe spacing and behaviour in all the Adaptive Probe Volumes in a Baking Set.
  * Use the settings in the [Adaptive Probe Volume Inspector window](probevolumes-inspector-reference.html) to change the Adaptive Probe Volume size and probe density.
  * Add a [Probe Adjustment Volume component](probevolumes-adjustment-volume-component-reference.html) to the Adaptive Probe Volume, to make probes invalid in a small area or fix other lighting issues.
  * Add a [Volume](set-up-a-volume.html) to your scene with a [Probe Volumes Options Override](probevolumes-options-override-reference.html), to change the way URP samples Adaptive Probe Volume data when the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) is inside the volume. This doesn’t
affect baking.

## Additional resources

  * [Bake multiple scenes together with Baking Sets](probevolumes-usebakingsets.html)
  * [Change lighting at runtime](probe-volumes-change-lighting-at-runtime.html)
  * [Fix issues with Adaptive Probe Volumes](probevolumes-fixissues.html)
  * [Work with multiple Scenes in Unity](https://docs.unity3d.com/Documentation/Manual/MultiSceneEditing.html)

[](../urp/probevolumes-concept.html)

Introduction to Adaptive Probe Volumes

[](../urp/probevolumes-showandadjust.html)

Display Adaptive Probe Volumes

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

