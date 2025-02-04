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

# CallbackEventHandler

class in UnityEngine.UIElements

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

Leave feedback

  

Implements interfaces:[IEventHandler](UIElements.IEventHandler.html)

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

Interface for classes capable of having callbacks to handle events.

### Public Methods

[HasBubbleUpHandlers](UIElements.CallbackEventHandler.HasBubbleUpHandlers.html)|
Return true if event handlers for the event propagation BubbleUp phase have
been attached to this object.  
---|---  
[HasTrickleDownHandlers](UIElements.CallbackEventHandler.HasTrickleDownHandlers.html)|
Returns true if event handlers, for the event propagation TrickleDown phase,
are attached to this object.  
[RegisterCallback](UIElements.CallbackEventHandler.RegisterCallback.html)|
Adds an event handler to the instance. If the event handler has already been
registered for the same phase (either TrickleDown or BubbleUp) then this
method has no effect.  
[RegisterCallbackOnce](UIElements.CallbackEventHandler.RegisterCallbackOnce.html)|
Adds an event handler to the instance. If the event handler has already been
registered for the same phase (either TrickleDown or BubbleUp) then this
method has no effect. The event handler is automatically unregistered after it
has been invoked exactly once.  
[SendEvent](UIElements.CallbackEventHandler.SendEvent.html)|  Sends an event
to the event handler.  
[UnregisterCallback](UIElements.CallbackEventHandler.UnregisterCallback.html)|
Remove callback from the instance.  
  
### Protected Methods

[HandleEventBubbleUp](UIElements.CallbackEventHandler.HandleEventBubbleUp.html)|
Executes logic on this element during the BubbleUp phase, immediately before
this element's BubbleUp callbacks. Calling StopPropagation will prevent
further invocations of this method along the propagation path.  
---|---  
[HandleEventTrickleDown](UIElements.CallbackEventHandler.HandleEventTrickleDown.html)|
Executes logic on this element during the TrickleDown phase, immediately after
this element's TrickleDown callbacks. Calling StopPropagation will prevent
further invocations of this method along the propagation path.  
[NotifyPropertyChanged](UIElements.CallbackEventHandler.NotifyPropertyChanged.html)|
Informs the data binding system that a property of a control has changed.  
  
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

