[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-color-emojis.html)
  * [中文](/cn/current/Manual/UIE-color-emojis.html)
  * [日本語](/ja/current/Manual/UIE-color-emojis.html)
  * [한국어](/kr/current/Manual/UIE-color-emojis.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-color-emojis.html)
  * [中文](/cn/current/Manual/UIE-color-emojis.html)
  * [日本語](/ja/current/Manual/UIE-color-emojis.html)
  * [한국어](/kr/current/Manual/UIE-color-emojis.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Color emojis

[](UIE-color-gradient.html)

Color gradients

[](UIE-advanced-text-generator.html)

Advanced Text Generator

# Color emojis

You can include color emojis and glyphs in text.

For Editor **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI), you can include emojis directly, and it
works because the Editor UI uses the default editor font fallbacks.

For runtime UI, you must import a font file with color emojis and set it as
the fallback emoji text asset.

![Color emojis example](../uploads/Main/font/NativeEmojiExample.png) Color
emojis example

## Set up color emojis

Create a color emojis font asset and add it to the UITK Text Settings
Fallback.

  1. In your project, import a font file that has color emojis in it.
  2. Right-click the font file, and then select **Create** > **Text Core** > **Font Asset** > **Color**. This ensures that you create the font asset with the correct shader (Sprite) and the correct atlas render mode (Color).
  3. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window of the [UITK Text
Settings](UIE-text-setting-asset.html), in the **Fallback Emoji Text Assets**
section, from the **Text Asset List** , select the color emojis font asset.

## Include emojis in text

To include emojis in text, do any of the following:

  * Include emojis in text through their Unicode value. For example, enter `\U0001F601` to represent a smile.
  * Use your operating system virtual keyboard.
  * Copy the emojis from an external text editing tool and paste them in your text field.

## Control emoji fallback search

You can prioritize searching the **Fallback Emoji Text Assets** for emojis.
For example, if a font includes black and white emojis, you can choose whether
to use emojis from the primary font or the **Fallback Emoji Text Assets**
list.

  1. In UI Builder, select the text element in the **Hierarchy** panel.

  2. In the **Inspector** panel, in the **Attributes** section, enable or disable the **Emoji Fallback Support** option:

     * **Enabled** : The system searches the **Fallback Emoji Text Assets** list first for any emoji characters.
     * **Disabled** : The system searches the primary font asset assigned to the text element first.

## Limitations

The color emojis feature doesn’t support the following:

  * Some OpenType font features, such as chain context and single substitution.
  * Apple fonts that use the AAT format, which is a predecessor to OpenType.
  * SVG color glyphs.
  * COLR Table Format version 2 (COLR v2), such as Noto Color Emoji.

Dynamic OS font asset has limited support on some iOS devices. The `Apple
Color Emoji` font file found on macOS and several iOS devices works correctly.
However, the `Apple Color Emoji-160px` found on newer iOS devices isn’t
supported. Its emojis are encoded in JPEG format, which isn’t supported by
FreeType.

## Additional resources

  * [Unicode Emojis Standard](http://unicode.org/Public/emoji/latest/)
  * [Font assets](UIE-font-asset-landing.html)
  * [Include sprites in text](UIE-sprite.html)
  * [Text Setting Asset](UIE-text-setting-asset.html)

[](UIE-color-gradient.html)

Color gradients

[](UIE-advanced-text-generator.html)

Advanced Text Generator

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

