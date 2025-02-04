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

#  [AnimationCurve](AnimationCurve.html).MoveKey

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

public int MoveKey(int index, [Keyframe](Keyframe.html) key);

### Parameters

index | The index of the key to move.  
---|---  
key | The keyframe containing the new time and value.  
  
### Returns

**int** The index of the keyframe after moving it.

### Description

Moves the key at `index` to `key.time` and `key.value`.

This method removes the keyframe at `index` and inserts the updated `key` at
the correct sorted position in [AnimationCurve.keys](AnimationCurve-
keys.html).  
Use it to move a keyframe in two dimensions (time and value).  
  
**Notes** :  
\- In order for this method to behave as intended, you are expected to acquire
the key using [AnimationCurve.keys](AnimationCurve-keys.html), modify the
value and/or time, then invoke `MoveKey` with the updated keyframe. If used
with a completely different keyframe, this method essentially replaces the key
with a new one.  
\- Since AnimationCurve does not support having two keys with the same time,
in the event where `key.time` conflicts with the time of another keyframe,
`key` will be reinserted at the time of the keyframe at `index`, cancelling
the move operation in the time dimension but keeping the modification in the
value dimension.  
\- This method is used by the Unity curve editor to implement
[Keyframe](Keyframe.html) dragging.  
  
See Also: [AnimationCurve.keys](AnimationCurve-keys.html)

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

