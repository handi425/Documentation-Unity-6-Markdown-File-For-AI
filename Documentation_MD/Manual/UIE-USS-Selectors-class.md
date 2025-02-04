[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Selectors-class.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-class.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-class.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-class.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Selectors-class.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-class.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-class.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-class.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * Class selectors

[](UIE-USS-Selectors-name.html)

Name selectors

[](UIE-USS-Selectors-universal.html)

Universal selectors

# Class selectors

USS class selectors match elements that have specific USS classes assigned.
USS class selectors are analogous to CSS class selectors.

## Syntax

A class selector consists of the class name prefixed with a period. Class
names are case-sensitive and can’t begin with a numeral.

    
    
    .className { ... }
    

Only use a period when you write the selector in a USS file. Don’t include it
when you assign the class to an element in a UXML or C# file. For example,
don’t use `<Button class=".yellow" />`.

In general, don’t include a period in class names. Unity’s USS parser
interprets a period as the beginning of a new class. For example, if you
create a class called `yellow.button`, and create the following USS rule:
`.yellow.button{...}`. The parser interprets the selector as a [multiple
selector](UIE-USS-Selectors-multiple.html), and tries to find elements that
match both a `.yellow` class and a `.button` class.

When an element has more than one class assigned, a selector only has to match
one of them to match the element.

You can also specify multiple classes in a selector, in which case an element
must have all of those classes assigned in order to match. See [Multiple
selectors](UIE-USS-Selectors-multiple.html) for details.

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

The following name class selector style rule matches the element `container2`
and the button element `OK`, and changes their background to yellow.

    
    
    .yellow {
        background-color: yellow;
    }
    

The UI looks like the following when you apply the style:

![The container2 and the OK button with a yellow
background.](../uploads/Main/uss-selectors-class.png) The container2 and the
OK button with a yellow background.

## Additional resources

  * [Best practices for USS](UIE-USS-WritingStyleSheets.html)

[](UIE-USS-Selectors-name.html)

Name selectors

[](UIE-USS-Selectors-universal.html)

Universal selectors

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

