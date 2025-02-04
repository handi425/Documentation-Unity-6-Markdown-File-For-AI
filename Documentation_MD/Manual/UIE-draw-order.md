[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-draw-order.html)
  * [中文](/cn/current/Manual/UIE-draw-order.html)
  * [日本語](/ja/current/Manual/UIE-draw-order.html)
  * [한국어](/kr/current/Manual/UIE-draw-order.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-draw-order.html)
  * [中文](/cn/current/Manual/UIE-draw-order.html)
  * [日本語](/ja/current/Manual/UIE-draw-order.html)
  * [한국어](/kr/current/Manual/UIE-draw-order.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [The visual tree](UIE-VisualTree-landing.html)
  * Draw order

[](UIE-panels.html)

Panels

[](UIE-coordinate-and-position-system.html)

Coordinate and position systems

# Draw order

The draw order of elements in the **visual tree** An object graph, made of
lightweight nodes, that holds all the elements in a window or panel. It
defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree) follows a depth-first search.
Child **visual elements** A node of a visual tree that instantiates or derives
from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) appear on top of parent
elements. **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit draws child elements in the order
of the sibling list. The draw order is the following:

  1. The top visual element.
  2. The first child element of that visual element.
  3. The child elements of the descendant element.

The diagram below shows the draw order of a visual tree:

![Visual element draw order](../uploads/Main/UIEDrawingOrder.png) Visual
element draw order

To change the draw order of visual elements in C#, use the following
functions:

  * [BringToFront()](../ScriptReference/UIElements.VisualElement.BringToFront.html)
  * [SendToBack()](../ScriptReference/UIElements.VisualElement.SendToBack.html)

To change the draw order of sibling visual elements, use the following
functions:

  * [PlaceBehind()](../ScriptReference/UIElements.VisualElement.PlaceBehind.html)
  * [PlaceInFront()](../ScriptReference/UIElements.VisualElement.PlaceInFront.html)

[](UIE-panels.html)

Panels

[](UIE-coordinate-and-position-system.html)

Coordinate and position systems

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

