[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-sprite-asset-properties.html)
  * [中文](/cn/current/Manual/UIE-sprite-asset-properties.html)
  * [日本語](/ja/current/Manual/UIE-sprite-asset-properties.html)
  * [한국어](/kr/current/Manual/UIE-sprite-asset-properties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-sprite-asset-properties.html)
  * [中文](/cn/current/Manual/UIE-sprite-asset-properties.html)
  * [日本語](/ja/current/Manual/UIE-sprite-asset-properties.html)
  * [한국어](/kr/current/Manual/UIE-sprite-asset-properties.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * [Include sprites in text](UIE-sprite.html)
  * Sprite Asset properties reference

[](UIE-sprite.html)

Include sprites in text

[](UIE-color-gradient.html)

Color gradients

# Sprite Asset properties reference

The following table describes the **sprite** A 2D graphic objects. If you are
used to working in 3D, Sprites are essentially just standard textures but
there are special techniques for combining and managing sprite textures for
efficiency and convenience during development. [More info](sprite/sprite-
landing.html)  
See in [Glossary](Glossary.html#Sprite) asset properties:

**Property** | **Description**  
---|---  
**Update Sprite Asset** | Sync the sprite asset with the latest [Sprite Editor](sprite/sprite-editor/sprite-editor-landing.html) changes.  
****Sprite Atlas** A utility that packs several sprite textures tightly
together within a single texture known as an atlas. [More
info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas)** | A reference to the sprite asset’s source texture.  
**Default Material** | A reference to the sprite asset’s material, which it uses to render sprites.  
**Fallback Sprite Asset List** | When a glyph doesn’t exist in this sprite asset, TextCore searches the fallback sprite assets list for the missing glyph. This is the local fallback list. The local fallback list has precedence over the global fallback list set in the [UITK Text Settings](UIE-text-setting-asset.html) asset. You can add or remove a sprite asset in the fallback list. You can also drag the handles on the left side of any sprit asset to reorder the list.  
**Sprite Character Table** | Manage the sprites in this asset.  
  
Click a sprite to make it active.  
  
Click **Up** or **Down** to move the sprite up or down in the list.  
  
To move the sprite to a specific position, enter the index ID of the position
in the text field and then click **Goto** to move the sprite to that position
in the list.  
  
**Note:** Moving a sprite updates its index ID and the index IDs of all
preceding sprites accordingly.  
  
Click **+** to add a copy of the sprite to the list.  
  
Click **-** to remove the sprite from the list.  
| **Index** | Unique index ID for the sprite, based on its position in the list.   
You can use it to reference the sprite in the [`<sprite>` rich text tag](UIE-
supported-tags.html#sprite).  
| **Unicode** | Unicode for the sprite. For more information, refer to [Assign and use Unicode for a sprite](UIE-sprite.html#assign-and-use-unicode-for-a-sprite).  
| **Name** | Unique name for the sprite.  
You can use it to reference the sprite in the [`<sprite>` rich text tag](UIE-
supported-tags.html#sprite).  
**Sprite Glyph Rect** | Manage the glyphs in this asset.  
| **X, Y, W, H** | Rectangular area that the character occupies in the sprite atlas.  
**Sprite Metrics** | Metrics for the sprite.  
| **W** | The width of the sprite.  
| **H** | The height of the sprite.  
| **BX, BY** | Stand for “Bearing X” and “Bearing Y,” which define the horizontal and vertical offsets from the glyph bounding box’s origin to the start of the drawings.  
| **AD** | Horizontal advance refers to the distance from the hozitontal origin of the glyph to the start of the next glyph.  
**Global Offsets & Scale** | Offsets and scale settings for all sprites in the asset.  
| **OX, OY** | Control the placement of the sprite, defined at its top-left corner relative to its origin on the baseline.  
| **ADV** | How far to advance along the baseline to place the next sprite.  
| **SF** | Adjust the size of the sprite.  
  
## Additional resources

  * [Include sprites in text](UIE-sprite.html)
  * [Rich text tags](UIE-rich-text-tags.html)

[](UIE-sprite.html)

Include sprites in text

[](UIE-color-gradient.html)

Color gradients

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

