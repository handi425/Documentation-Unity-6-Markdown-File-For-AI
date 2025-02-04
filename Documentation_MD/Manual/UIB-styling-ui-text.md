[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIB-styling-ui-text.html)
  * [中文](/cn/current/Manual/UIB-styling-ui-text.html)
  * [日本語](/ja/current/Manual/UIB-styling-ui-text.html)
  * [한국어](/kr/current/Manual/UIB-styling-ui-text.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIB-styling-ui-text.html)
  * [中文](/cn/current/Manual/UIB-styling-ui-text.html)
  * [日本語](/ja/current/Manual/UIB-styling-ui-text.html)
  * [한국어](/kr/current/Manual/UIB-styling-ui-text.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Work with text](UIE-work-with-text.html)
  * Style text with USS

[](UIE-get-started-with-text.html)

Get started with text

[](UIE-rich-text-tags.html)

Style text with rich text tags

# Style text with USS

You can style text with USS text properties inline in [UXML](UIE-UXML.html), a
[USS](UIE-USS.html) file, or directly in [UI Builder](UIBuilder.html). To
learn more about USS text properties, refer to [Text properties](UIE-USS-
SupportedProperties.html#unity-text).

## Style text in USS and UXML

[Text properties](UIE-USS-SupportedProperties.html#unity-text) are regular USS
style properties. You can set text style properties on any element. Unlike
most USS style properties, text style properties propagate to child elements.

The following USS example styles the `Label` text to bold and italic, and has
a font size of `39px`:

    
    
    Label {
        -unity-font-style: bold-and-italic; 
        font-size: 39px;
    }
    

The following UXML inline style example applies the same style to the `Label`
text:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements" xmlns:uie="UnityEditor.UIElements">
        <ui:VisualElement>
            <ui:Label text="Label" style="-unity-font-style: bold-and-italic; font-size: 39px;" />
        </ui:VisualElement>
    </ui:UXML>
    

## Style text in UI builder

To style text in **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) Builder, you can use the **Text** section
in a UI control’s **Inspector** A Unity window that displays information about
the currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to style text.

If the UI control is a text element that inherits from [TextElement](UIE-uxml-
element-TextElement.html), such as [Label](UIE-uxml-element-Label.html) or
[Button](UIE-uxml-element-Button.html), you can also set the following text
styles directly in the **Canvas** on selected text elements:

  * Horizontal text align
  * Vertical text align
  * Text wrap

![Text styles are exposed as toggles in the Canvas on selected
elements](../uploads/Main/UIBuilder/CanvasTextToggles.png) Text styles are
exposed as toggles in the Canvas on selected elements

## Additional resources

  * [Get started with text](UIE-get-started-with-text.html)
  * [Text effects](UIE-text-effects.html)
  * [Font assets](UIE-font-asset.html)
  * [Rich text tags](UIE-rich-text-tags.html)
  * [Style sheet assets](UIE-style-sheet.html)
  * [Include sprites in text](UIE-sprite.html)

[](UIE-get-started-with-text.html)

Get started with text

[](UIE-rich-text-tags.html)

Style text with rich text tags

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

