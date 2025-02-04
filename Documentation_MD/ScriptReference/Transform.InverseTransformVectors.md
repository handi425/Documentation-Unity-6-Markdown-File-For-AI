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

#  [Transform](Transform.html).InverseTransformVectors

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

### Parameters

vectors | The vectors to be transformed, each is replaced by the transformed version.  
---|---  
  
### Description

Transforms multiple vectors from world space to local space overwriting each
original position with the transformed version. The opposite of
[Transform.TransformVectors](Transform.TransformVectors.html).

This operation is not affected by position of the transform but it is affected
by scale. The transformed vectors may have different lengths than the
originals.  
  
Additional
resources:[Transform.TransformVectors](Transform.TransformVectors.html),
[Transform.InverseTransformVector](Transform.InverseTransformVector.html),
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html),
[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html).

* * *

## Declaration

public void InverseTransformVectors(ReadOnlySpan<Vector3> vectors,
Span<Vector3> transformedVectors);

### Parameters

vectors | The vectors to be transformed, these vectors are not modified by the function unless the `transformedVectors` span overlaps.  
---|---  
transformedVectors | Receives the transformed vectors, must be the same length as `vectors` otherwise an exception will be thrown. If this span overlaps `vectors` other than representing the exact same elements the behaviour is undefined.  
  
### Description

Transforms the vector `x`, `y`, `z` from world space to local space writing
the transformed positions to a possibly different location. The opposite of
[Transform.TransformVector](Transform.TransformVector.html).

This operation is not affected by position of the transform but it is affected
by scale.The transformed vectors may have different lengths than the
originals.  
  
Additional
resources:[Transform.TransformVectors](Transform.TransformVectors.html),
[Transform.InverseTransformVector](Transform.InverseTransformVector.html),
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html),
[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html).

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

