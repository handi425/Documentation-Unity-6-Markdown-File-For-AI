[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# GUIStyle

class in UnityEngine

/

Implemented in:[UnityEngine.IMGUIModule](UnityEngine.IMGUIModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-GUIStyle.html "Go to GUIStyle Component in
the Manual")

### Description

Styling information for GUI elements.

Most GUI functions accept an optional GUIStyle parameter to override the
default style. This allows coloring, fonts and other details to be changed and
switched for different states (eg, when the mouse is hovering over the
control). Where a consistent look-and-feel is required over a whole GUI
design, the GUISkin class is a useful way to collect a set of GUIStyle
settings and apply them all at once.

### Static Properties

[none](GUIStyle-none.html)| Shortcut for an empty GUIStyle.  
---|---  
  
### Properties

[active](GUIStyle-active.html)| Rendering settings for when the control is
pressed down.  
---|---  
[alignment](GUIStyle-alignment.html)| Text alignment.  
[border](GUIStyle-border.html)| The borders of all background images.  
[clipping](GUIStyle-clipping.html)| What to do when the contents to be
rendered is too large to fit within the area given.  
[contentOffset](GUIStyle-contentOffset.html)| Pixel offset to apply to the
content of this GUIstyle.  
[fixedHeight](GUIStyle-fixedHeight.html)| If non-0, any GUI elements rendered
with this style will have the height specified here.  
[fixedWidth](GUIStyle-fixedWidth.html)| If non-0, any GUI elements rendered
with this style will have the width specified here.  
[focused](GUIStyle-focused.html)| Rendering settings for when the element has
keyboard focus.  
[font](GUIStyle-font.html)| The font to use for rendering. If null, the
default font for the current GUISkin is used instead.  
[fontSize](GUIStyle-fontSize.html)| The font size to use (for dynamic fonts).  
[fontStyle](GUIStyle-fontStyle.html)| The font style to use (for dynamic
fonts).  
[hover](GUIStyle-hover.html)| Rendering settings for when the mouse is
hovering over the control.  
[imagePosition](GUIStyle-imagePosition.html)| How image and text of the
GUIContent is combined.  
[lineHeight](GUIStyle-lineHeight.html)| The height of one line of text with
this style, measured in pixels. (Read Only)  
[margin](GUIStyle-margin.html)| The margins between elements rendered in this
style and any other GUI elements.  
[name](GUIStyle-name.html)| The name of this GUIStyle. Used for getting them
based on name.  
[normal](GUIStyle-normal.html)| Rendering settings for when the component is
displayed normally.  
[onActive](GUIStyle-onActive.html)| Rendering settings for when the element is
turned on and pressed down.  
[onFocused](GUIStyle-onFocused.html)| Rendering settings for when the element
has keyboard and is turned on.  
[onHover](GUIStyle-onHover.html)| Rendering settings for when the control is
turned on and the mouse is hovering it.  
[onNormal](GUIStyle-onNormal.html)| Rendering settings for when the control is
turned on.  
[overflow](GUIStyle-overflow.html)| Extra space to be added to the background
image.  
[padding](GUIStyle-padding.html)| Space from the edge of GUIStyle to the start
of the contents.  
[richText](GUIStyle-richText.html)| Enable HTML-style tags for Text Formatting
Markup.  
[stretchHeight](GUIStyle-stretchHeight.html)| Can GUI elements of this style
be stretched vertically for better layout?  
[stretchWidth](GUIStyle-stretchWidth.html)| Can GUI elements of this style be
stretched horizontally for better layouting?  
[wordWrap](GUIStyle-wordWrap.html)| Should the text be wordwrapped?  
  
### Constructors

[GUIStyle](GUIStyle-ctor.html)| Constructor for empty GUIStyle.  
---|---  
  
### Public Methods

[CalcHeight](GUIStyle.CalcHeight.html)| How tall this element will be when
rendered with content and a specific width.  
---|---  
[CalcMinMaxWidth](GUIStyle.CalcMinMaxWidth.html)| Calculate the minimum and
maximum widths for this style rendered with content.  
[CalcScreenSize](GUIStyle.CalcScreenSize.html)| Calculate the size of an
element formatted with this style, and a given space to content.  
[CalcSize](GUIStyle.CalcSize.html)| Calculate the size of some content if it
is rendered with this style.  
[Draw](GUIStyle.Draw.html)| Draw this GUIStyle on to the screen, internal
version.  
[DrawCursor](GUIStyle.DrawCursor.html)| Draw this GUIStyle with selected
content.  
[DrawWithTextSelection](GUIStyle.DrawWithTextSelection.html)| Draw this
GUIStyle with selected content.  
[GetCursorPixelPosition](GUIStyle.GetCursorPixelPosition.html)| Get the pixel
position of a given string index.  
[GetCursorStringIndex](GUIStyle.GetCursorStringIndex.html)| Get the cursor
position (indexing into contents.text) when the user clicked at
cursorPixelPosition.  
  
### Operators

[GUIStyle](GUIStyle-operator_string.html)| Get a named GUI style from the
current skin.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

