[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Selectors-name.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-name.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-name.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-name.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Selectors-name.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-name.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-name.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-name.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * Name selectors

[](UIE-USS-Selectors-type.html)

Type selectors

[](UIE-USS-Selectors-class.html)

Class selectors

# Name selectors

USS name selectors match elements based on the name of an element. USS Name
selectors are analogous to CSS ID selectors that match elements with a
specific `id` attribute.

To set the name of an element:

  * In C# script, use `VisualElement.name`.
  * In UXML, use the `name` attribute. For example: `<VisualElement name="my-nameName">`.

To avoid unexpected matches, make element names unique within a panel.

## Syntax

A name selector consists of an element’s assigned name prefixed with a number
sign (`#`).

    
    
    #ElementName { ... }
    

**Note** : Only use the number sign (`#`) when you write the selector in a USS
file. Don’t use it when you assign the name to an element in a UXML or C#
file. An element name that includes the number sign is invalid. For example
`<Button name="#OK" />` is invalid.

## Example

To demonstrate how simple selectors match elements, here is an example
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Document.

    
    
    <UXML xmlns="UnityEngine.UIElements">
      <VisualElement name="container1">
        <VisualElement name="container2" class="yellow">
          <Button name="OK" class="yellow" text="OK" />
          <Button name="Cancel" text="Cancel" />
        </VisualElement>
      </VisualElement>
    </UXML>
    

With no styles applied, the UI looks like the following:

![Example buttons with margins and thin blue borders.](../uploads/Main/uss-
selectors-nostyle.png) Example buttons with margins and thin blue borders.

The following name selector style rule matches the second `Button` element.

    
    
    #Cancel {
        border-width: 2px;
        border-color: DarkRed;
        background-color: pink;
    }
    

The UI looks like the following when you apply the style:

![The Cancel button has a dark red border and a pink
background.](../uploads/Main/uss-selectors-name.png) The Cancel button has a
dark red border and a pink background.

## Additional resources

  * [Best practices for USS](UIE-USS-WritingStyleSheets.html)

[](UIE-USS-Selectors-type.html)

Type selectors

[](UIE-USS-Selectors-class.html)

Class selectors

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

