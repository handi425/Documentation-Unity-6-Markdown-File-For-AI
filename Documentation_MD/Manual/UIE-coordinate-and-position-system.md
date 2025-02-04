[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-coordinate-and-position-system.html)
  * [中文](/cn/current/Manual/UIE-coordinate-and-position-system.html)
  * [日本語](/ja/current/Manual/UIE-coordinate-and-position-system.html)
  * [한국어](/kr/current/Manual/UIE-coordinate-and-position-system.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-coordinate-and-position-system.html)
  * [中文](/cn/current/Manual/UIE-coordinate-and-position-system.html)
  * [日本語](/ja/current/Manual/UIE-coordinate-and-position-system.html)
  * [한국어](/kr/current/Manual/UIE-coordinate-and-position-system.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [The visual tree](UIE-VisualTree-landing.html)
  * Coordinate and position systems

[](UIE-draw-order.html)

Draw order

[](UIE-UXML.html)

Structure UI with UXML

# Coordinate and position systems

UI Toolkit uses a powerful layout system that automatically calculates the
position and size of individual elements based on the layout parameters in
their style properties. This is based on Flexbox, a web layout model. For more
information, see [Layout Engine](UIE-LayoutEngine.html).

## Relative and absolute positions

UI Toolkit has two types of coordinates:

  * **Relative** : Coordinates relative to the element’s calculated position. The layout system calculates the position of the element, then adds the coordinates as an offset. Parent elements can influence the size and position of the child elements, as the layout engine takes them into account when it calculates the element position. Child elements can only influence the size of the parent element.
  * **Absolute** : Coordinates relative to the parent element. This circumvents the automatic layout calculation and directly sets the position of the element. Sibling elements under the same parent have no influence on the element’s position. Similarly, the element doesn’t influence the position and size of other siblings under the same parent.

Each **visual element** A node of a visual tree that instantiates or derives
from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) determines the coordinate
system used to calculate its position. You can configure which coordinate
system to use in the element stylesheet.

The following code shows how to set the coordinate space and the position of a
visual element through code:

    
    
        var newElement = new VisualElement();
        newElement.style.position = Position.Relative;
        newElement.style.left = 15;
        newElement.style.top = 35;
    

The origin of an element is its top left corner.

The layout system computes the
[`VisualElement.layout`](../ScriptReference/UIElements.VisualElement-
layout.html) property (type `Rect`) for each element, which includes the final
position of the element. This takes the relative or absolute position of the
element into account.

The `layout.position` is expressed in points, relative to the coordinate space
of its parent.

Each `VisualElement` has a transform property (`ITransform`) you can use to
add an additional local offset to the position and rotation of an element. The
offset isn’t represented in the calculated layout property. By default, the
`transform` is the identity.

Use the [`worldBound`](../ScriptReference/UIElements.VisualElement-
worldBound.html) property to retrieve the final window space coordinates of
the `VisualElement`, taking into account both the layout position and the
transform. This position includes the height of the header of the window.

## Transformation between coordinate systems

The `VisualElement.layout.position` and `VisualElement.transform` properties
define how to transform between the local coordinate system and the parent
coordinate system.

The
[`VisualElementExtensions`](../ScriptReference/UIElements.VisualElementExtensions.html)
static class provides the following extension methods that transform points
and rectangles between coordinate systems:

  * `WorldToLocal` transforms a `Vector2` or `Rect` from `Panel` space to the referential within the element.
  * `LocalToWorld` transforms a `Vector2` or `Rect` to `Panel` space referential.
  * `ChangeCoordinatesTo` transforms `Vector2` or `Rect` from the local space of one element to the local space of another.

## Additional resource

  * [Relative and absolute positioning C# example](UIE-relative-absolute-positioning-example.html)

[](UIE-draw-order.html)

Draw order

[](UIE-UXML.html)

Structure UI with UXML

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

