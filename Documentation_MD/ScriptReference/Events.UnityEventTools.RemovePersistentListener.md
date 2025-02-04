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

#  [UnityEventTools](Events.UnityEventTools.html).RemovePersistentListener

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

public static void
RemovePersistentListener([Events.UnityEventBase](Events.UnityEventBase.html)
unityEvent, int index);

## Declaration

public static void
RemovePersistentListener([Events.UnityEventBase](Events.UnityEventBase.html)
unityEvent, [Events.UnityAction](Events.UnityAction.html) call);

## Declaration

public static void
RemovePersistentListener([Events.UnityEventBase](Events.UnityEventBase.html)
unityEvent, [Events.UnityAction_1](Events.UnityAction_1.html) call);

## Declaration

public static void
RemovePersistentListener([Events.UnityEventBase](Events.UnityEventBase.html)
unityEvent, [Events.UnityAction_2](Events.UnityAction_2.html) call);

## Declaration

public static void
RemovePersistentListener([Events.UnityEventBase](Events.UnityEventBase.html)
unityEvent, [Events.UnityAction_3](Events.UnityAction_3.html) call);

## Declaration

public static void
RemovePersistentListener([Events.UnityEventBase](Events.UnityEventBase.html)
unityEvent, [Events.UnityAction_4](Events.UnityAction_4.html) call);

### Parameters

unityEvent | Event to modify.  
---|---  
index | Index to remove (if specified).  
call | Function to remove (if specified).  
  
### Description

Removes the given function from the event.

You can specify either the index of the listener function to remove, or the
delegate type of the listener function to remove. If you specify the delegate
type, this method removes all occurrences of that listener function from the
event. If you specify the the index, this method only removes the listener
function at the index specified.

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

