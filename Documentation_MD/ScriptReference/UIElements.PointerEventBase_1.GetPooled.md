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

#  [PointerEventBase<T0>](UIElements.PointerEventBase_1.html).GetPooled

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

## Declaration

public static T GetPooled([Event](Event.html) systemEvent);

### Parameters

systemEvent | An IMGUI mouse event.  
---|---  
  
### Returns

**T** An initialized event.

### Description

Gets an event from the event pool and initializes it with the given values.
Use this function instead of creating new events. Events obtained using this
method need to be released back to the pool. You can use `Dispose()` to
release them.

* * *

## Declaration

public static T GetPooled([Touch](Touch.html) touch,
[EventModifiers](EventModifiers.html) modifiers);

### Parameters

touch | A <see cref="Touch" /> structure from the InputManager.  
---|---  
modifiers | The modifier keys held down during the event.  
  
### Returns

**T** An initialized event.

### Description

Gets an event from the event pool and initializes it with the given values.
Use this function instead of creating new events. Events obtained using this
method need to be released back to the pool. You can use `Dispose()` to
release them.

* * *

## Declaration

public static T GetPooled([PenData](PenData.html) pen,
[EventModifiers](EventModifiers.html) modifiers);

### Parameters

pen | A <see cref="PenData" /> structure from the InputManager containing pen event information.  
---|---  
modifiers | The modifier keys held down during the event.  
  
### Returns

**T** An initialized event.

### Description

Gets a pointer event from the event pool and initializes it with the given
values. Use this function instead of creating new events. Events obtained
using this method need to be released back to the pool. You can use
`Dispose()` to release them.

* * *

## Declaration

public static T
GetPooled([UIElements.IPointerEvent](UIElements.IPointerEvent.html)
triggerEvent);

### Parameters

triggerEvent | The event that sent this event.  
---|---  
  
### Returns

**T** An initialized event.

### Description

Gets an event from the event pool and initializes it with the given values.
Use this function instead of creating new events. Events obtained using this
method need to be released back to the pool. You can use `Dispose()` to
release them.

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

