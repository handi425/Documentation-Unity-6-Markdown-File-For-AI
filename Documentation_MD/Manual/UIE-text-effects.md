[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-text-effects.html)
  * [中文](/cn/current/Manual/UIE-text-effects.html)
  * [日本語](/ja/current/Manual/UIE-text-effects.html)
  * [한국어](/kr/current/Manual/UIE-text-effects.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-text-effects.html)
  * [中文](/cn/current/Manual/UIE-text-effects.html)
  * [日本語](/ja/current/Manual/UIE-text-effects.html)
  * [한국어](/kr/current/Manual/UIE-text-effects.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Text effects

[](UIE-font-creator-properties.html)

Font Asset Creator properties reference

[](UIE-style-sheet.html)

Style sheets

# Text effects

You can apply text effects to enhance the visual appearance of the text.
However, these effects are only supported for font assets with [SDF rendering
mode](UIE-font-asset.html#sdf-fonts) and not for bitmap. The range of the text
effects is limited by the padding defined for the font asset. Therefore, to
increase the size of the effect, you must increase the padding.

You can use text effects to:

  * Apply text shadows
  * Apply text outlines

## Apply text shadows

To apply shadows to the text, set the `text-shadow` property in a USS file,
inline in UXML, or a C# script.

`text-shadow` is a shorthand property that sets the following properties:

  * `text-shadow-offset-x`: Horizontal shadow displacement. Positive values move the shadow to the right, while negative values move it to the left.
  * `text-shadow-offset-y`: Vertical shadow displacement. Positive values move the shadow down, while negative values move it up.
  * `text-shadow-blur-radius`: The blur intensity of the shadow. Higher values result in more blur shadows, while 0 creates a sharp shadow.
  * `text-shadow-color`: The color of the shadow, either as a hex code or in RGBA format.

The following example applies a shadow to a `Label` element:

![Text shadow example](../uploads/Main/uitk/text-shadow.png) Text shadow
example

    
    
    Label {
        text-shadow: 6.1px -2.4px 0px rgb(144, 31, 32);
    }
    

## Apply text outlines

To apply outlines to text, set the `unity-text-outline` property in a USS
file, inline in UXML, or a C# script.

`unity-text-outline` is a shorthand property that sets the following
properties:

  * `-unity-text-outline-width`: The width of the outline.
  * `-unity-text-outline-color`: The color of the outline, either as a hex code or in RGBA format.

The following example applies an outline to a `Label` element:

![Text outline example](../uploads/Main/uitk/text-outline.png) Text outline
example

    
    
    Label {
        text-outline: 6px rgb(144, 31, 32);
    }
    

## Additional resources

  * [Get started with text](UIE-get-started-with-text.html)
  * [Font assets](UIE-font-asset.html)
  * [Text properties](UIE-USS-SupportedProperties.html#unity-text)
  * [Style text with USS](UIB-styling-ui-text.html)

[](UIE-font-creator-properties.html)

Font Asset Creator properties reference

[](UIE-style-sheet.html)

Style sheets

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

