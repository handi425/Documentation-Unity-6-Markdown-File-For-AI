[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-style-sheet.html)
  * [中文](/cn/current/Manual/UIE-style-sheet.html)
  * [日本語](/ja/current/Manual/UIE-style-sheet.html)
  * [한국어](/kr/current/Manual/UIE-style-sheet.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-style-sheet.html)
  * [中文](/cn/current/Manual/UIE-style-sheet.html)
  * [日本語](/ja/current/Manual/UIE-style-sheet.html)
  * [한국어](/kr/current/Manual/UIE-style-sheet.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Style sheets

[](UIE-text-effects.html)

Text effects

[](UIE-sprite.html)

Include sprites in text

# Style sheets

If you want to reuse a style, create a custom style sheet for it, and apply it
to text through the [`<style>` rich text tag](UIE-supported-tags.html#style).

A custom style can include opening and closing rich text tags, and leading and
trailing text.

For example, you might want headings in your text to be big, red, bold, with
an asterisk to either side and a line break at the end.

Instead of typing this for every heading:

`<font-weight=700><size=2em><color=#FF0000>*Heading*</color></size></font-
weight><br>`

You can create a style, called `H1` that includes all of that formatting, and
then apply the style to your headings.

For instructions on how to create a custom style sheet, see [Style-with-style-
sheets in Get started with text](UIE-get-started-with-text.html#style-with-
style-sheets)

To use a custom style sheet in the rich text tag, reference the style sheet
asset name and the style name: `<style="assetName" name="styleName">`.

For runtime UI, if you have set a style sheet as the default style sheet in
the [UITK Text Settings](UIE-text-setting-asset.html), you can omit the asset
name: `<style="styleName">`. For example: `<style="H1">This is heading
1</style>`.

## Additional resources

  * [Rich text tags](UIE-rich-text-tags.html)

[](UIE-text-effects.html)

Text effects

[](UIE-sprite.html)

Include sprites in text

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

