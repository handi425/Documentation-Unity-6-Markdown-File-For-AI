[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Selectors-descendant.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-descendant.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-descendant.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-descendant.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Selectors-descendant.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-descendant.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-descendant.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-descendant.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * Descendant selectors

[](UIE-USS-Selectors-universal.html)

Universal selectors

[](UIE-USS-Selectors-child.html)

Child selectors

# Descendant selectors

USS descendant selectors match elements that are the descendant of another
element in the [visual tree](UIE-VisualTree.html)An object graph, made of
lightweight nodes, that holds all the elements in a window or panel. It
defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree).

## Syntax

A descendant selector consists of multiple simple selectors separated by a
space:

    
    
    selector1 selector2 {...}
    

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

The following descendant selector style rule matches both the inner element
and the first button.

    
    
    #container1 .yellow {
      background-color: yellow;
    }
    

The UI looks like the following when you apply the style:

![The container2 and the OK button have a yellow
background.](../uploads/Main/uss-selectors-descendant.png) The container2 and
the OK button have a yellow background.

**Note** : Heavy use of descendant selectors could negatively affect
performance. For more performance guidelines, see [Best practices for
USS](UIE-USS-WritingStyleSheets.html).

## Additional resources

  * [Best practices for USS](UIE-USS-WritingStyleSheets.html)

[](UIE-USS-Selectors-universal.html)

Universal selectors

[](UIE-USS-Selectors-child.html)

Child selectors

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

