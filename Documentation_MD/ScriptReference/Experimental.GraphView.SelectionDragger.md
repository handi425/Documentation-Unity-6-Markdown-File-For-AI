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

**Experimental** : this API is experimental and might be changed or removed in
the future.

# SelectionDragger

class in UnityEditor.Experimental.GraphView

/

Inherits
from:[Experimental.GraphView.Dragger](Experimental.GraphView.Dragger.html)

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

Selection dragger manipulator.

### Constructors

[SelectionDragger](Experimental.GraphView.SelectionDragger-ctor.html)|
SelectionDragger's constructor.  
---|---  
  
### Protected Methods

[OnMouseDown](Experimental.GraphView.SelectionDragger.OnMouseDown.html)|
Called on mouse down event.  
---|---  
[OnMouseMove](Experimental.GraphView.SelectionDragger.OnMouseMove.html)|
Called on mouse move event.  
[OnMouseUp](Experimental.GraphView.SelectionDragger.OnMouseUp.html)| Called on
mouse up event.  
[RegisterCallbacksOnTarget](Experimental.GraphView.SelectionDragger.RegisterCallbacksOnTarget.html)|
Called to register click event callbacks on the target element.  
[UnregisterCallbacksFromTarget](Experimental.GraphView.SelectionDragger.UnregisterCallbacksFromTarget.html)|
Called to unregister event callbacks from the target element.  
  
### Inherited Members

### Properties

[clampToParentEdges](Experimental.GraphView.Dragger-clampToParentEdges.html)|
If true, it does not allow the dragged element to exit the parent's edges.  
---|---  
[panSpeed](Experimental.GraphView.Dragger-panSpeed.html)| When elements are
dragged near the edges of the Graph, panning occurs. This controls the speed
for said panning.  
[target](UIElements.Manipulator-target.html)|  VisualElement being
manipulated.  
[activators](UIElements.MouseManipulator-activators.html)|  List of
Activationfilters.  
  
### Protected Methods

[CalculatePosition](Experimental.GraphView.Dragger.CalculatePosition.html)|
Calculate new position of the dragged element.  
---|---  
[CanStartManipulation](UIElements.MouseManipulator.CanStartManipulation.html)|
Checks whether MouseEvent satisfies all of the ManipulatorActivationFilter
requirements.  
[CanStopManipulation](UIElements.MouseManipulator.CanStopManipulation.html)|
Checks whether the MouseEvent is related to this Manipulator.  
  
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

