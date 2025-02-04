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

#  [AnimationCurve](AnimationCurve.html).AddKey

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

public int AddKey(float time, float value);

### Parameters

time | The time at which to add the key (horizontal axis in the curve graph).  
---|---  
value | The value for the key (vertical axis in the curve graph).  
  
### Returns

**int** The index of the added key, or -1 if the key could not be added.

### Description

Add a new key to the curve.

Smooth tangents are automatically computed for the key. Returns the index of
the added key. If no key could be added because there is already another
keyframe at the same time -1 will be returned.  
  
Additional resources: [keys](AnimationCurve-keys.html) variable.

* * *

## Declaration

public int AddKey([Keyframe](Keyframe.html) key);

### Parameters

key | The key to add to the curve.  
---|---  
  
### Returns

**int** The index of the added key, or -1 if the key could not be added.

### Description

Add a new key to the curve.

Returns the index of the added key. If no key could be added because there is
already another keyframe at the same time -1 will be returned.  
  
Additional resources: [keys](AnimationCurve-keys.html) variable,
[Keyframe](Keyframe.html) struct.

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

