[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/add-post-processing.html)
  * [中文](/cn/current/Manual/urp/add-post-processing.html)
  * [日本語](/ja/current/Manual/urp/add-post-processing.html)
  * [한국어](/kr/current/Manual/urp/add-post-processing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/add-post-processing.html)
  * [中文](/cn/current/Manual/urp/add-post-processing.html)
  * [日本語](/ja/current/Manual/urp/add-post-processing.html)
  * [한국어](/kr/current/Manual/urp/add-post-processing.html)

  * [Rendering](../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../urp/post-processing-in-urp.html)
  * Add post-processing in URP

[](../urp/integration-with-post-processing.html)

Introduction to post-processing in URP

[](../urp/volumes-landing-page.html)

Volumes in URP

# Add post-processing in URP

New scenes in URP do not use **post-processing** A process that improves
product visuals by applying filters and effects before the image appears on
screen. You can use post-processing effects to simulate physical camera and
film properties, for example Bloom and Depth of Field. [More
info](../PostProcessingOverview.html) post processing, postprocessing,
postprocess  
See in [Glossary](../Glossary.html#post-processing) by default. Instead you
must manually add post-processing to any new **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) which you create. You can then
configure each effect individually to create the visual effect you want.

**Note** : Some examples and scene templates in URP use post-processing by
default. If you use these to create a new scene, you might not need to make
any changes.

## Add post-processing to a scene

To add post-processing to a scene:

  1. Select a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera), then in the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window enable **Post
Processing**.

  2. Add a GameObject with a [Volume](Volumes.html) component in the scene. For example, select **GameObject** > **Volume** > **Global Volume**.
  3. Select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject), then in the **Volume**
component select **New** to create a new [Volume Profile](Volume-
Profile.html).

  4. Select **Add Override** , then select a post-processing effect [Volume Override](VolumeOverrides.html), for example **Bloom**.

Now you can use the Volume Override to enable and adjust the settings for the
post-processing effect.

**Note** : The GameObject which contains the volume and the camera you wish to
apply post-processing to must be on the same Layer.

## Configure individual post-processing effects

Each post-processing effect in URP has individual settings you can adjust to
tune the visual impact they have on your scene. For more information on the
post-processing effect settings, refer to the reference pages in the [Effect
List](EffectList.html).

[](../urp/integration-with-post-processing.html)

Introduction to post-processing in URP

[](../urp/volumes-landing-page.html)

Volumes in URP

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

