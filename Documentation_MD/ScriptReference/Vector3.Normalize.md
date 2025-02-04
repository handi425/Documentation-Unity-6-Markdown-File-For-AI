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

#  [Vector3](Vector3.html).Normalize

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

public void Normalize();

### Description

Makes this vector have a [magnitude](Vector3-magnitude.html) of 1.

When normalized, a vector keeps the same direction but its length is 1.0.  
  
Note that this function will change the current vector. If you want to keep
the current vector unchanged, use [normalized](Vector3-normalized.html)
variable.  
  
If this vector is too small to be normalized it will be set to zero.  
  
Additional resources: [normalized](Vector3-normalized.html) property.

* * *

## Declaration

public static [Vector3](Vector3.html) Normalize([Vector3](Vector3.html)
value);

### Parameters

value | The vector to be normalized.  
---|---  
  
### Returns

**Vector3** A new vector with the same direction as the original vector but
with a magnitude of 1.0.

### Description

Returns a normalized vector based on the given vector. The normalized vector
has a [magnitude](Vector3-magnitude.html) of 1 and is in the same direction as
the given vector. Returns a zero vector If the given vector is too small to be
normalized.

Note that this does not modify the given vector. To modify and normalize the
current vector, use the [Normalize](Vector3.Normalize.html) function without a
parameter.  
  
Additional resources: [normalized](Vector3-normalized.html) function.

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

