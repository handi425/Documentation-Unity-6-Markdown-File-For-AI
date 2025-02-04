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

#  [Transform](Transform.html).TransformVectors

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

## Declaration

public void TransformVectors(Span<Vector3> vectors);

### Parameters

vectors | The vectors to be transformed, each is replaced by the transformed version.  
---|---  
  
### Description

Transforms multiple vectors from local space to world space overwriting each
original vector with the transformed version.

This operation is not affected by the position of the transform, but it is
affected by scale. The transformed vectors may have a different length to the
original versions.  
  
If you need the inverse operation to transform from world space to local space
you can use
[Transform.InverseTransformVectors](Transform.InverseTransformVectors.html)  
  
Additional
resources:[Transform.TransformVector](Transform.TransformVector.html),
[Transform.InverseTransformVectors](Transform.InverseTransformVectors.html),
[Transform.TransformPoint](Transform.TransformPoint.html),
[Transform.TransformDirection](Transform.TransformDirection.html).

* * *

## Declaration

public void TransformVectors(ReadOnlySpan<Vector3> vectors, Span<Vector3>
transformedVectors);

### Parameters

vectors | The vectors to be transformed, these vectors are not modified by the function unless the `transformedVectors` span overlaps.  
---|---  
transformedVectors | Receives the transformed vectors, must be the same length as `vectors` otherwise an exception will be thrown. If this span overlaps `vectors` other than representing the exact same elements the behaviour is undefined.  
  
### Description

Transforms multiple vectors from local space to world space writing the
transformed versions to a possibly different location.

This operation is not affected by the position of the transform, but is is
affected by scale.The transformed vectors may have a different length to the
original versions.  
  
If you need the inverse operation to transform from world space to local space
you can use
[Transform.InverseTransformVectors](Transform.InverseTransformVectors.html)  
  
Additional
resources:[Transform.TransformVector](Transform.TransformVector.html),
[Transform.InverseTransformVectors](Transform.InverseTransformVectors.html),
[Transform.TransformPoint](Transform.TransformPoint.html),
[Transform.TransformDirection](Transform.TransformDirection.html).

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

