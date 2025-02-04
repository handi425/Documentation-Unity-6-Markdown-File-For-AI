[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-fallback-font.html)
  * [中文](/cn/current/Manual/UIE-fallback-font.html)
  * [日本語](/ja/current/Manual/UIE-fallback-font.html)
  * [한국어](/kr/current/Manual/UIE-fallback-font.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-fallback-font.html)
  * [中文](/cn/current/Manual/UIE-fallback-font.html)
  * [日本語](/ja/current/Manual/UIE-fallback-font.html)
  * [한국어](/kr/current/Manual/UIE-fallback-font.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Fallback font

[](UIE-text-setting-asset.html)

UITK Text Settings assets

[](UIE-examples.html)

Examples

# Fallback font

Each font asset has a limited number of characters. When you use a character
that isn’t in the current font asset, TextCore searches the **Fallback List**
until it finds a font asset with that character. The text element then uses
that font asset to render the character.

You can set a list of fallback fonts to distribute fonts over multiple
textures, or use different fonts for specific characters. It requires extra
computing resources to search the list for missing characters and additional
draw calls to use additional fonts.

You can use the same character for multiple font assets in the fallback list.
Match the style of the characters in the fallback list to style of the main
font asset as possible as you can.

## Fallback font usage

In general, use fallback font assets to:

  * Work with languages that have large alphabets, such as Chinese, Korean, and Japanese. Use fallback fonts to distribute an alphabet across several assets.
  * Include special characters from other alphabets in your text.

**Tips** : Dynamic OS font assets are great candidates for fallback font
assets.

## Fallback font chain

You can create local and global fallback font asset lists. Set local font
asset lists in the [Font Assets property](UIE-font-asset-properties.html) and
set global font asset lists in [UITK Text Settings](UIE-text-setting-
asset.html). In addition to the fallback fonts, TextCore searches other
assets, such as the default **sprite** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) asset, for missing glyphs. Together,
these assets form the fallback chain.

The following is the asset order in the fallback chain:

  1. Local fallback font assets list
  2. Global fallback font assets list
  3. Default sprite asset
  4. Dynamic OS fallback
  5. Missing glyphs character

## Additional resources

  * [Font assets](UIE-font-asset.html)
  * [Include sprites in text](UIE-sprite.html)

[](UIE-text-setting-asset.html)

UITK Text Settings assets

[](UIE-examples.html)

Examples

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

