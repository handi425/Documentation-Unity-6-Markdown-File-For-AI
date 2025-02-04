[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Selectors-multiple.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-multiple.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-multiple.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-multiple.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Selectors-multiple.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-multiple.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-multiple.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-multiple.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * Multiple selectors

[](UIE-USS-Selectors-child.html)

Child selectors

[](UIE-USS-Selectors-list.html)

Selector lists

# Multiple selectors

A multiple selector is an combination of multiple simple selectors. It selects
any elements that match all the simple selectors.

## Syntax

A multiple selector consists of multiple simple selector without anything to
separate them:

    
    
    selector1selector2 {...}
    

The USS parser can’t parse a multiple selector if it can’t distinguish each
selector in the combination.

For example, the following USS rule combines two type selectors: `ListView`,
and `Button`.

    
    
    ListViewButton{...}
    

The USS parser can’t separate the two element types, it interprets them as a
single class called ListViewButton, which might not be the desired result.

You can combine [USS class selectors](UIE-USS-Selectors-class.html) and [name
selectors](UIE-USS-Selectors-name.html) into multiple selectors. Because
they’re are with the period (.) and number sign (#) respectively, the parser
can clearly identify them. Type selectors have no identifying character, so
you can only use one of them in a multiple selector, and it must be the first
selector in the combination. For example:

    
    
    ListView.yellow#vertical-list{...}
    

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

The following name selector style rule matches the first button.

    
    
    Button.yellow {
      background-color: yellow;
    }
    

The UI looks like the following when you apply the style:

![The OK button has a yellow background color.](../uploads/Main/uss-selectors-
multiple.png) The OK button has a yellow background color.

## Additional resources

  * [Best practices for USS](UIE-USS-WritingStyleSheets.html)

[](UIE-USS-Selectors-child.html)

Child selectors

[](UIE-USS-Selectors-list.html)

Selector lists

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

