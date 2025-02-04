[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Selectors-type.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-type.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-type.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-type.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Selectors-type.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-type.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-type.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-type.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * Type selectors

[](UIE-USS-Selectors.html)

USS selectors

[](UIE-USS-Selectors-name.html)

Name selectors

# Type selectors

USS type selectors match elements based on their element types. USS type
selectors are analogous to CSS type selectors that match HTML tags. For
example, `Button {...}` in USS matches any [Button](UIE-uxml-element-
Button.html) elements in the same way that `p {...}` in CSS matches any
paragraph (`<p>`) tag.

## Syntax

The following is the syntax for a type selector:

    
    
    TypeName { ... }
    

When you write type selectors, specify only the concrete object type. Don’t
include the namespace in the type name.

For example, this selector is valid:

    
    
    Button { ... }
    

This selector is invalid:

    
    
    UnityEngine.UIElements.Button { ... }
    

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

The following type selector style rule matches the two `Button` elements:

    
    
    Button {
      border-radius: 8px;
      width: 100px;
      }
    

The UI looks like the following when you apply the style:

![Example buttons with border radius and specific width.](../uploads/Main/uss-
selectors-csharp-type.png) Example buttons with border radius and specific
width.

## Additional resources

  * [Best practices for USS](UIE-USS-WritingStyleSheets.html)

[](UIE-USS-Selectors.html)

USS selectors

[](UIE-USS-Selectors-name.html)

Name selectors

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

