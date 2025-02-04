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

**Method group is Obsolete**  

#
[CallbackEventHandler](UIElements.CallbackEventHandler.html).ExecuteDefaultAction

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

**Obsolete** Use HandleEventBubbleUp. Before proceeding, make sure you
understand the latest changes to UIToolkit event propagation rules by visiting
Unity's manual page https://docs.unity3d.com/Manual/UIE-Events-
Dispatching.html.

## Declaration

protected void
ExecuteDefaultAction([UIElements.EventBase](UIElements.EventBase.html) evt);

### Parameters

evt | The event instance.  
---|---  
  
### Description

Executes logic after the callbacks registered on the event target have been
executed, unless the event has been marked to prevent its default behaviour.
EventBase_1.PreventDefault.

This method is designed to be overriden by subclasses. Use it to implement
event handling without registering callbacks which guarantees precedences of
callbacks registered by users of the subclass. Unlike HandleEventBubbleUp,
this method is called after both the callbacks registered on the element and
callbacks registered on its ancestors with
[TrickleDown.NoTrickleDown](UIElements.TrickleDown.NoTrickleDown.html).  
  
Use [EventInterestAttribute](UIElements.EventInterestAttribute.html) on this
method to specify a range of event types that this method needs to receive.
Events that don't fall into the specified types might not be sent to this
method.

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

