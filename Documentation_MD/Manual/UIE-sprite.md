[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-sprite.html)
  * [中文](/cn/current/Manual/UIE-sprite.html)
  * [日本語](/ja/current/Manual/UIE-sprite.html)
  * [한국어](/kr/current/Manual/UIE-sprite.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-sprite.html)
  * [中文](/cn/current/Manual/UIE-sprite.html)
  * [日本語](/ja/current/Manual/UIE-sprite.html)
  * [한국어](/kr/current/Manual/UIE-sprite.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Include sprites in text

[](UIE-style-sheet.html)

Style sheets

[](UIE-sprite-asset-properties.html)

Sprite Asset properties reference

# Include sprites in text

To use sprites in your rich text tags, such as emojis, you need a **sprite** A
2D graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) asset. You create sprite assets from
atlas [textures](Textures.html)An image used when rendering a GameObject,
Sprite, or UI element. Textures are often applied to the surface of a mesh to
give it visual detail. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) that contain a set of sprites.

![An example atlas texture](../uploads/Main/font/sprite-asset.png) An example
atlas texture

You can use as many sprite atlases and assets as you want. However, if you use
multiple atlases per text object results in multiple draw calls for that
object and consumes more system resources. As a rule, when you import multiple
sprites, pack them into a single atlas to reduce draw calls. Make sure the
**sprite atlas** A utility that packs several sprite textures tightly together
within a single texture known as an atlas. [More
info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas) has a suitable resolution for
your target platform.

Use the [`<sprite>` rich text tag](UIE-supported-tags.html#sprite) to include
sprites in your text.

See information for all the [Sprite asset properties](UIE-sprite-asset-
properties.html).

## Create a sprite asset

You create sprite assets from atlas textures. Although sprite assets and their
source textures are separate entities, you must keep the source textures in
the project after you’ve created the sprite assets.

To create a sprite asset:

  1. [Import the sprite atlas](sprite/sprite-landing.html).

  2. Select the atlas and change the following texture options in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window:

     * Set the **Texture Type** to **Sprite (2D and UI)**.
     * Set the **Sprite Mode** to **Multiple**.
  3. Select **[Sprite Editor](sprite/sprite-editor/sprite-editor-landing.html)** and divide the texture into individual sprites.

  4. Right-click the sprite and select **Create** > **Text Core** > **Sprite Asset**. This creates a new sprite asset.

  5. From the Inspector window, you can further customize the appearance and names of each glyph. Refer to [Sprite Asset properties](UIE-sprite-asset-properties.html) for more information.

  6. Place the sprite asset to the path set in the [UITK Text Settings](UIE-text-setting-asset.html).

Once you’ve created the sprite asset, you can revert the atlas texture’s
**Texture Type** to its original setting.

## Use a sprite asset

To use sprites in the rich text tag, reference the sprite asset name and the
sprite name as `<sprite="assetName" name="spriteName">` or by index as
`<sprite="assetName" index=1>`.

You can add the `tint=1` attribute to the tag to tint the sprite with the text
object’s vertex color. You can also choose a different color by adding a color
attribute to the tag, for example: `<sprite="assetName" index=1
color=#55FF55FF>`.

For runtime UI, if you have set a sprite asset as the default in the [UITK
Text Settings](UIE-text-setting-asset.html), you can omit the asset name as
`<sprite index=1>` (or shorthand `<sprite=1>`), or `<sprite
name="spriteName">`.

## Assign and use Unicode for a sprite

You can assign a Unicode to a sprite and use the Unicode directly in your text
object instead of the `<sprite>` tag.

For example, the Unicode for a smiling face emoji is `U+1F60A`. To assign it
to a sprite in your sprite asset:

  1. In the sprite asset’s Inspector window, find the glyph in the **Sprite Character Table**. You can browse or search by index or name.
  2. Click the glyph to enable the edit mode.
  3. In the Unicode box, enter `+1F60A`.
  4. Click the **Unicode** label to save your changes. The Unicode changes to `0xF1F60A`.

To use the smiling face emoji in your text object, enter `\U00F1F60A`.

## Additional resources

  * [Sprite asset properties](UIE-sprite-asset-properties.html)
  * [Rich text tags](UIE-rich-text-tags.html)

[](UIE-style-sheet.html)

Style sheets

[](UIE-sprite-asset-properties.html)

Sprite Asset properties reference

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

