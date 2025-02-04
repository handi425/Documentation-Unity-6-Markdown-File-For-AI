[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-rich-text-tags.html)
  * [中文](/cn/current/Manual/UIE-rich-text-tags.html)
  * [日本語](/ja/current/Manual/UIE-rich-text-tags.html)
  * [한국어](/kr/current/Manual/UIE-rich-text-tags.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-rich-text-tags.html)
  * [中文](/cn/current/Manual/UIE-rich-text-tags.html)
  * [日本語](/ja/current/Manual/UIE-rich-text-tags.html)
  * [한국어](/kr/current/Manual/UIE-rich-text-tags.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Style text with rich text tags

[](UIB-styling-ui-text.html)

Style text with USS

[](UIE-supported-tags.html)

Supported rich text tags

# Style text with rich text tags

You can use [USS to style a whole text string](UIB-styling-ui-text.html), but
what if you only want to style one word of your text string? This is difficult
with USS, but it’s simple with rich text tags.

Rich text tags are tags that you can place inside a text string to style the
text between the tags.

For all the supported tags, see [Supported tags](UIE-supported-tags.html).

**Note** : In the current release, rich text tags aren’t supported for
[TextField](UIE-uxml-element-TextField.html).

## Rich text syntax

Rich text tags are similar to HTML or XML tags, but have less strict syntax.

A simple tag can have be just its name and have no additional values or
attributes. For example, the `<b>` tag makes text bold.

Some tags have additional values or attributes like this:

  * `<tag="value">`
  * `<tag attribute="value">`

For example:

  * `<color=”red”>`: Makes text red
  * `<sprite index=3>`: Inserts the fourth sprite from the default Sprite Asset.

**Note** : In a UXML file, you must use HTML code for the following
characters:

  * `<`: `(&lt;)`
  * `>`: `(&gt;)`
  * `"`: `(&quot;)`

The following table lists possible attribute value types and example values.

**Value type** | **Example value**  
---|---  
Decimals | `0.5`  
Percentages | `25%`  
**Pixel** The smallest unit in a computer image. Pixel size depends on your
screen resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) values | `5px`  
Font units | `1.5em`  
Hex color values |  `#FFFFFF` (RGB)  
`#FFFFFFFF` (RGBA)  
`#FF` (A)  
Names | Both `<link=”ID”>` and `<link=ID>` are valid.  
  
## Tag scope and nested tags

Tags have a scope that defines how much of the text they affect. Most of the
time, a tag added to a specified point in the text affects all of the text
from that point forward.

For example, if you add the tag `<color="red">` to the beginning of the text,
it affects the entire text block: `<color="red">This text is red`.

If you add the same tag in the middle of the text block, it affects only the
text between the tag and the end of the block : `This text turns<color="red">
red`.

If you use the same tag more than once in a text block, the last tag
supersedes all previous tags of the same type: `<color="red">This text goes
from red<color="green"> to green`.

You can also use a closing tag to limit the scope of a tag, and use nested tag
within another tag: `<color=red>This text is <color=green>mostly </color>red`

The first `<color>` tag’s scope is the entire text block. The the second
`<color>` tag has a closing tag that limits its scope to one word.

When you nest tags, you don’t need to close their scopes in the same order
that you started them.

## Enable and disable rich text tags

Rich text tags are enabled by default.

To disable the rich text tag, do one of the following:

  * In **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, select the control and clear the
**Enable Rich Text** checkbox in the **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window.

  * In UXML, set the `enable-rich-text` attribute to `false`.

## Additional resources

  * [Supported tags](UIE-supported-tags.html)
  * [Style sheets](UIE-style-sheet.html)
  * [Include sprites in text](UIE-sprite.html)
  * [Color gradients](UIE-color-gradient.html)

[](UIB-styling-ui-text.html)

Style text with USS

[](UIE-supported-tags.html)

Supported rich text tags

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

