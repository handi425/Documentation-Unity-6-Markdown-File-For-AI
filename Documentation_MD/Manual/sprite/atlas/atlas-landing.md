[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/atlas/atlas-landing.html)
  * [中文](/cn/current/Manual/sprite/atlas/atlas-landing.html)
  * [日本語](/ja/current/Manual/sprite/atlas/atlas-landing.html)
  * [한국어](/kr/current/Manual/sprite/atlas/atlas-landing.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/atlas/atlas-landing.html)
  * [中文](/cn/current/Manual/sprite/atlas/atlas-landing.html)
  * [日本語](/ja/current/Manual/sprite/atlas/atlas-landing.html)
  * [한국어](/kr/current/Manual/sprite/atlas/atlas-landing.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * Sprite atlas

[](../../sprite/mask/sprite-mask-reference.html)

Sprite mask reference

[](../../sprite/atlas/create-sprite-atlas.html)

Create a Sprite Atlas

# Sprite atlas

A 2D project uses **sprites** A 2D graphic objects. If you are used to working
in 3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) and other graphics to create the
visuals of its **scenes** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene). This means a single project can
contain many texture files. Unity typically issues a [draw
call](../../DrawCallBatching.html) for each texture in the scene; however, in
a project with many textures, multiple draw calls become resource-intensive
and can negatively impact the performance of your project.

A **Sprite Atlas** A utility that packs several sprite textures tightly
together within a single texture known as an atlas. [More
info](../../sprite/atlas/v2/v2-landing.html)  
See in [Glossary](../../Glossary.html#SpriteAtlas) is an asset that
consolidates several textures into a single combined texture. Unity can call
this single texture to issue a single draw call instead of multiple draw calls
to access the packed textures all at once at a smaller performance overhead.
You can use the [Sprite Atlas
API](../../../ScriptReference/U2D.SpriteAtlas.html) to control loading the
Sprite Atlases at your project’s runtime.

**Topic** | **Description**  
---|---  
[**Create a Sprite Atlas**](create-sprite-atlas.html) | Create a `.spriteatlas` file in the Assets folder.  
[**Master and Variant Sprite Atlases**](master-variant/master-variant-landing.html) | Choose the Type property for a Sprite Atlas.  
[**Sprite Atlas Workflow**](workflow/workflow-landing.html) | Follow the general workflow to create a Sprite Atlas.  
[**Prepare Sprite Atlases for distribution**](distribution/distribution-landing.html) | Distribute Sprite Atlases.  
[**Sprite Atlas V2**](v2/v2-landing.html) | Use the Sprite Atlas V2 mode.  
[**Sprite Packer Modes**](packer-mode/packer-mode-landing.html) | Choose the default packing behavior for a Sprite Atlas.  
[**Sprite Atlas reference**](sprite-atlas-reference.html) | Refer to the properties of the Sprite Atlas.  
  
[](../../sprite/mask/sprite-mask-reference.html)

Sprite mask reference

[](../../sprite/atlas/create-sprite-atlas.html)

Create a Sprite Atlas

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

