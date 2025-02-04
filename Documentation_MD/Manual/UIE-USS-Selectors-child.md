[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-Selectors-child.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-child.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-child.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-child.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-Selectors-child.html)
  * [中文](/cn/current/Manual/UIE-USS-Selectors-child.html)
  * [日本語](/ja/current/Manual/UIE-USS-Selectors-child.html)
  * [한국어](/kr/current/Manual/UIE-USS-Selectors-child.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS selectors](UIE-USS-Selectors.html)
  * Child selectors

[](UIE-USS-Selectors-descendant.html)

Descendant selectors

[](UIE-USS-Selectors-multiple.html)

Multiple selectors

# Child selectors

USS child selectors match elements that are the child of another element in
the [visual tree](UIE-VisualTree.html)An object graph, made of lightweight
nodes, that holds all the elements in a window or panel. It defines every UI
you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree).

## Syntax

A child selector consists of multiple simple selectors separated by `>`.

    
    
    selector1 > selector2 {...}
    

You can include the wildcard selector in complex selectors. For example, the
following USS rule uses the wildcard selector in a [child selector](UIE-USS-
Selectors-child.html). This USS rule matches buttons that are children of
elements that are children of an element with the USS class `yellow` assigned
to it.

    
    
    .yellow > * > Button{..}
    

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

The following child selector style rule matches only the inner element.
Element `#OK` with the `.yellow` class is a child of element `#container2`.
`#container2` is child of element `#container1`. However, because `#OK` is not
a direct descendant of `#container1`, it doesn’t match the `.yellow` selector
when applied with a child selector from `#container1`.

    
    
    #container1 > .yellow {
      background-color: yellow;
    }
    

The UI looks like the following when you apply the style:

![The container2 has a yellow background color.](../uploads/Main/uss-
selectors-child.png) The container2 has a yellow background color.

## Additional resources

  * [Best practices for USS](UIE-USS-WritingStyleSheets.html)

[](UIE-USS-Selectors-descendant.html)

Descendant selectors

[](UIE-USS-Selectors-multiple.html)

Multiple selectors

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

