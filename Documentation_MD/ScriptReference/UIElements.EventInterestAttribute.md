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

# EventInterestAttribute

class in UnityEngine.UIElements

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

Optional attribute on overrides of
[CallbackEventHandler.HandleEventBubbleUp](UIElements.CallbackEventHandler.HandleEventBubbleUp.html)
and
[CallbackEventHandler.HandleEventTrickleDown](UIElements.CallbackEventHandler.HandleEventTrickleDown.html).
Use this attribute to specify all the event types used by the method override.
The event dispatcher can then safely skip events not needed for this method if
they are identified internally as valid candidates for performance
optimizations.

Only use this attribute for performance optimizations, not for filtering out
specific event types. All event types specified in an
[EventInterestAttribute](UIElements.EventInterestAttribute.html) on a
HandleEvent method override are guaranteed to be sent to that method. However,
event types not specified in any
[EventInterestAttribute](UIElements.EventInterestAttribute.html) might still
be sent to that method under various conditions:

  * A base class override uses it,
  * The event is part of a group that includes at least one event of interest, or
  * Event optimizations are not applied for any other reason.

  
If no [EventInterestAttribute](UIElements.EventInterestAttribute.html) is
specified, UI Toolkit assumes that the method doesn't have enough information
on necessary event types, and sends all incoming events to that method
conservatively.  
  
It is recommended to use the
[EventInterestAttribute](UIElements.EventInterestAttribute.html) attribute
because it allows UI Toolkit to optimize performance by skipping unnecessary
event-related calculations for methods that don’t use the event.

### Constructors

[EventInterestAttribute](UIElements.EventInterestAttribute-ctor.html)|  Use
this constructor when the affected method uses only specific event types that
can easily be determined at compile time. Multiple EventInterestAttribute can
be used on the same method to add more type interests.  
---|---  
  
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

