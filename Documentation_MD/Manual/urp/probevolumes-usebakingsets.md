[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/probevolumes-usebakingsets.html)
  * [中文](/cn/current/Manual/urp/probevolumes-usebakingsets.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-usebakingsets.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-usebakingsets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/probevolumes-usebakingsets.html)
  * [中文](/cn/current/Manual/urp/probevolumes-usebakingsets.html)
  * [日本語](/ja/current/Manual/urp/probevolumes-usebakingsets.html)
  * [한국어](/kr/current/Manual/urp/probevolumes-usebakingsets.html)

  * [Lighting](../LightingOverview.html)
  * [Lighting in URP](../urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](../urp/probevolumes.html)
  * Bake multiple scenes together with Baking Sets

[](../urp/probevolumes-changedensity.html)

Configure the size and density of Adaptive Probe Volumes

[](../urp/probe-volumes-change-lighting-at-runtime.html)

Changing lighting at runtime

# Bake multiple scenes together with Baking Sets

If you [load multiple scenes
simultaneously](https://docs.unity3d.com/Documentation/Manual/MultiSceneEditing.html)
in your project, for example if you load multiples **scenes** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) at the same time in an open world
game, you can add the scenes to a single Baking Set so you can bake the
lighting for all the scenes together.

Refer to [Understanding probe volumes](probevolumes-concept.html#baking-sets)
for more information about Baking Sets.

## Create a Baking Set

To place multiple scenes in a single Baking Set and bake them together, follow
these steps:

  1. From the main menu, select **Window** > **Rendering** > **Lighting**.
  2. Set **Baking Mode** to **Baking Set**.
  3. In **Current Baking Set** , select an existing Baking Set asset, or select **New** to create a new Baking Set.
  4. Use the **Add** (**+**) button to add scenes.

You can only add each scene to a single Baking Set.

To remove a scene from a Baking Set, select the scene in the **Scenes in
Baking Set** list, then select the **Remove** (**-**) button.

## Bake a Baking Set

Select **Generate Lighting** to bake the lighting in all the scenes in a
baking set.

The Universal **Render Pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](../render-
pipelines.html)  
See in [Glossary](../Glossary.html#Renderpipeline) (URP) uses the settings
from the Baking Set, and serializes the results in the `Assets` folder, in a
subfolder with the same name as the active scene. You can move or rename the
folder.

For faster iteration times, disable **Bake** next to a scene name. This stops
Unity baking lighting data for this scene. This might result in incomplete
data, but it can help reduce baking time when you’re iterating on parts of a
large world.

### Load a scene

Unity doesn’t automatically load the scenes in a Baking Set when you select
the scene in the **Scenes** list. To load a scene, select **Load Baking Set**.

When you load multiple scenes together, the lighting might be too bright
because URP combines light from all the scenes. Refer to [Set up multiple
Scenes](https://docs.unity3d.com/Manual/setupmultiplescenes.html) for more
information on loading and unloading Scenes.

You can load multiple scenes together only if they belong to the same Baking
Set.

## Additional resources

  * [Bake different lighting setups with Lighting Scenarios](probevolumes-bakedifferentlightingsetups.html)

[](../urp/probevolumes-changedensity.html)

Configure the size and density of Adaptive Probe Volumes

[](../urp/probe-volumes-change-lighting-at-runtime.html)

Changing lighting at runtime

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

