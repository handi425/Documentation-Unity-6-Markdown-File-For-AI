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

# Clickable

class in UnityEngine.UIElements

/

Inherits
from:[UIElements.PointerManipulator](UIElements.PointerManipulator.html)

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

[ ]()

### Description

Manipulator that tracks Mouse events on an element and callbacks when the
elements is clicked.

### Properties

[active](UIElements.Clickable-active.html)|  This property tracks the
activation of the manipulator. Set it to true when the manipulator is
activated.  
---|---  
[lastMousePosition](UIElements.Clickable-lastMousePosition.html)|  Specifies
the mouse position saved during the last mouse event on the target Element.  
  
### Constructors

[Clickable](UIElements.Clickable-ctor.html)|  Constructor.  
---|---  
  
### Protected Methods

[Invoke](UIElements.Clickable.Invoke.html)|  Invokes a click action.  
---|---  
[OnPointerDown](UIElements.Clickable.OnPointerDown.html)|  This method is
called when a PointerDownEvent is sent to the target element.  
[OnPointerMove](UIElements.Clickable.OnPointerMove.html)|  This method is
called when a PointerMoveEvent is sent to the target element.  
[OnPointerUp](UIElements.Clickable.OnPointerUp.html)|  This method is called
when a PointerUpEvent is sent to the target element.  
[ProcessCancelEvent](UIElements.Clickable.ProcessCancelEvent.html)|  This
method processes the up cancel sent to the target Element.  
[ProcessDownEvent](UIElements.Clickable.ProcessDownEvent.html)|  This method
processes the down event sent to the target Element.  
[ProcessMoveEvent](UIElements.Clickable.ProcessMoveEvent.html)|  This method
processes the move event sent to the target Element.  
[ProcessUpEvent](UIElements.Clickable.ProcessUpEvent.html)|  This method
processes the up event sent to the target Element.  
[RegisterCallbacksOnTarget](UIElements.Clickable.RegisterCallbacksOnTarget.html)|
Called to register mouse event callbacks on the target element.  
[UnregisterCallbacksFromTarget](UIElements.Clickable.UnregisterCallbacksFromTarget.html)|
Called to unregister event callbacks from the target element.  
  
### Events

[clicked](UIElements.Clickable-clicked.html)|  Callback triggered when the
target element is clicked.  
---|---  
[clickedWithEventInfo](UIElements.Clickable-clickedWithEventInfo.html)|
Callback triggered when the target element is clicked, including event data.  
  
### Inherited Members

### Properties

[target](UIElements.Manipulator-target.html)|  VisualElement being
manipulated.  
---|---  
[activators](UIElements.MouseManipulator-activators.html)|  List of
Activationfilters.  
  
### Protected Methods

[CanStartManipulation](UIElements.MouseManipulator.CanStartManipulation.html)|
Checks whether MouseEvent satisfies all of the ManipulatorActivationFilter
requirements.  
---|---  
[CanStopManipulation](UIElements.MouseManipulator.CanStopManipulation.html)|
Checks whether the MouseEvent is related to this Manipulator.  
[CanStartManipulation](UIElements.PointerManipulator.CanStartManipulation.html)|
Checks whether PointerEvent satisfies all of the ManipulatorActivationFilter
requirements.  
[CanStopManipulation](UIElements.PointerManipulator.CanStopManipulation.html)|
Checks whether the PointerEvent is related to this Manipulator.  
  
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

