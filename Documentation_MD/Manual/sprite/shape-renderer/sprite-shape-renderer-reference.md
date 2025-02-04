[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)
  * [中文](/cn/current/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)
  * [日本語](/ja/current/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)
  * [한국어](/kr/current/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)
  * [中文](/cn/current/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)
  * [日本語](/ja/current/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)
  * [한국어](/kr/current/Manual/sprite/shape-renderer/sprite-shape-renderer-reference.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sprite shape renderer](../../sprite/shape-renderer/shape-renderer-landing.html)
  * Sprite shape renderer reference

[](../../sprite/shape-renderer/mask-interaction.html)

Mask interaction

[](../../tilemaps/tilemaps-landing.html)

Tilemaps in Unity

# Sprite shape renderer reference

Property | Function |   
---|---|---  
**Color** | Define the vertex color of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) Shape geometry, which tints or
recolors the Sprite Shape. Use the color picker to set the vertex. See the
[Color](color.html) section below this table for examples.  
**Mask Interaction** | Set how the **Sprite Renderer** A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](../../sprite/renderer/renderer-landing.html)  
See in [Glossary](../../Glossary.html#SpriteRenderer) behaves when it
interacts with a [Sprite Mask](../mask/mask-landing.html)A texture which
defines which areas of an underlying image to reveal or hide. [More
info](../../sprite/mask/mask-landing.html)  
See in [Glossary](../../Glossary.html#SpriteMask) . Refer to examples of the
different options in the [Mask Interaction](mask-interaction.html) section
below.  
| **None** | The Sprite Shape Renderer does not interact with any Sprite Masks in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene). This is the default option.  
| **Visible Inside Mask** | The Sprite Shape is visible where the Sprite Mask overlays it, but not outside of it.  
| **Visible Outside Mask** | The Sprite Shape is visible outside of the Sprite Mask, but not inside it. The Sprite Mask hides the sections of the Sprite Shape it overlays.  
**Sorting Layer** | Set the [Sorting Layer](../../class-TagManager.html) of the Sprite Shape geometry, which controls its priority during rendering. Select an existing Sorting Layer from the drop-down box, or create a new Sorting Layer.  
**Order In Layer** | Set the render priority of the Sprite Shape within its [Sorting Layer](../../class-TagManager.html). Lower numbered Sprite Shapes are rendered first, with higher numbered Sprite Shapes overlapping those below.  
  
SpriteShapeRenderer

[](../../sprite/shape-renderer/mask-interaction.html)

Mask interaction

[](../../tilemaps/tilemaps-landing.html)

Tilemaps in Unity

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

