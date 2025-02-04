[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-advanced-text-generator.html)
  * [中文](/cn/current/Manual/UIE-advanced-text-generator.html)
  * [日本語](/ja/current/Manual/UIE-advanced-text-generator.html)
  * [한국어](/kr/current/Manual/UIE-advanced-text-generator.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-advanced-text-generator.html)
  * [中文](/cn/current/Manual/UIE-advanced-text-generator.html)
  * [日本語](/ja/current/Manual/UIE-advanced-text-generator.html)
  * [한국어](/kr/current/Manual/UIE-advanced-text-generator.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Advanced Text Generator

[](UIE-color-emojis.html)

Color emojis

[](UIE-text-setting-asset.html)

UITK Text Settings assets

# Advanced Text Generator

Advanced Text Generator is a text rendering module that employs
[Harfbuzz](https://harfbuzz.github.io/), [ICU](https://icu.unicode.org/), and
[FreeType](https://freetype.org/) to deliver comprehensive Unicode support and
text shaping capabilities.

With Advanced Text Generator, you can use a wide array of languages and
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), such as right-to-left (RTL)
languages like Arabic and Hebrew.

## Enable Advanced Text Generator

  1. From the menu, select **Edit** > **Project Settings** > **UI Toolkit**.
  2. Select the **Enable Advanced Text Generator** checkbox.

## Use Advanced Text Generator

To use Advanced Text Generator, you must use a font asset that supports the
language you want to use. For example, if you want to use Arabic, you must use
a font asset that supports Arabic. Advanced Text Generator only supports
dynamic font assets. Before using Advanced Text Generator in your project, you
must import the font into your project and [create a dynamic font asset](UIE-
get-started-with-text.html#create-a-dynamic-font-asset) from it.

### In UI Builder

To use Advanced Text Generator in **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, do the following:

  1. Select the **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) that you want to apply to.

  2. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** panel, select **Text**.

  3. From the **Advanced Text Generator** dropdown, select **Advanced**.

### In USS

To use Advanced Text Generator in USS, set `-unity-text-generator` to
`advanced`. For example:

    
    
    .labelText {
        -unity-text-generator: advanced;
    }
    

### In C# scripts

To use Advanced Text Generator in C# scripts, set
[`TextGeneratorType`](../ScriptReference/TextGeneratorType.html) to
`Advanced`. For example:

    
    
    textElement.style.unityTextGenerator = new StyleEnum<TextGeneratorType>(TextGeneratorType.Advanced);
    

## Language Direction

The Language Direction is a global UXML attribute that corresponds to the to
the [dir](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dir)
property in HTML. This attribute sets the default text direction for any
VisualElement and cascades to child elements.

The Language Direction also impacts the ellipsis position, punctuation
placement and, once support for the [:dir()](https://developer.mozilla.org/en-
US/docs/Web/CSS/:dir) pseudo-state is added, allows to apply styles
conditionally based on the text direction.

### Values

  * Inherited (default): The element inherits the text direction from its parent.
  * LTR (Left-to-Right): Forces the text within the element to flow from left to right.
  * RTL (Right-to-Left): Forces the text within the element to flow from right to left.

We also plan to support the `auto` value in future releases. The `auto` value
dynamically determines the text direction by analyzing the Unicode characters
in the text block. It counts the number of strong directional characters (LTR
or RTL) and sets the direction based on the higher count.

## Cursor Movement

This section explains how cursor movement behaves in Unity’s Input Fields when
handling **bidirectional text** (BIDI text).

### Logical Cursor Movement

Unity currently follows a `Logical Cursor Movement` approach. This means the
cursor moves through bidirectional text based on the direction of the segment
of text. For example, using the left arrow key in a sentence with Arabic and
English text, it moves right-to-left through Arabic, then jumps at the
leftmost character in the English segment and continues left-to-right until it
reaches the end of the segment.

![Logical Cursor Movement Example](../uploads/Main/font/UIE-
CursorMovement.gif) Logical Cursor Movement Example

### Visual Cursor Movement

Some application follow a `Visual Cursor Movement` approach. This means the
cursor moves to the next visual character regardless of the direction of the
text, which can sometimes feel more intuitive for users. We plan to make the
cursor movement mode an option in future releases.

## Limitations

Advanced Text Generator has the following limitations:

  * Supports only dynamic font assets.
  * Customization of glyph metrics is not available. The recommended best practice is using font editing tools to adjust metrics or trim the font as needed.

Some features are not yet supported but are planned for future releases:

  * Certain Rich Text tags, including `<sprite>`, `<size>`, `<font>`, `<space>`, `<mark>`, and a few others.
  * Spacing properties such as character, word, and paragraph spacing.

When you use Advanced Text Generator, your project includes an `icudt73l` file
that has a significant memory footprint of `4.8MB`. This will be improved in
future releases.

## Additional resources

  * [Get started with text](UIE-get-started-with-text.html)
  * [Font assets](UIE-font-asset-landing.html)

[](UIE-color-emojis.html)

Color emojis

[](UIE-text-setting-asset.html)

UITK Text Settings assets

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

